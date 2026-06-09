import importlib.resources
from pathlib import Path
import pytest
from setupci.cli import copy_template

FRAMEWORKS = ["fastapi", "flask", "django", "general"]
TYPES = ["simple", "backend"]

@pytest.mark.parametrize("framework", FRAMEWORKS)
@pytest.mark.parametrize("project_type", TYPES)
def test_templates_exist_and_copy(tmp_path, framework, project_type):
    # Get template path
    src_path = importlib.resources.files("setupci.templates") / framework / project_type
    
    # Assert template directory exists
    assert src_path.exists(), f"Template {framework}/{project_type} does not exist!"
    
    # Copy template to temporary directory
    target_dir = tmp_path / framework / project_type
    copy_template(src_path, target_dir)
    
    # Assert directory is created and not empty
    assert target_dir.exists()
    assert any(target_dir.iterdir()), f"Template {framework}/{project_type} copied an empty directory!"
    
    # Verify standard files exist in the output directory
    readme_file = target_dir / "README.md"
    gitignore_file = target_dir / ".gitignore"
    
    assert readme_file.is_file(), f"README.md not found in {framework}/{project_type}"
    assert gitignore_file.is_file(), f".gitignore not found in {framework}/{project_type}"
    
    # Additional specific checks
    if framework == "fastapi" and project_type == "backend":
        assert (target_dir / "app" / "main.py").is_file()
        assert (target_dir / "requirements.txt").is_file()
    elif framework == "fastapi" and project_type == "simple":
        assert (target_dir / "main.py").is_file()
        assert (target_dir / "requirements.txt").is_file()
    elif framework == "flask" and project_type == "backend":
        assert (target_dir / "wsgi.py").is_file()
        assert (target_dir / "app" / "__init__.py").is_file()
    elif framework == "django" and project_type == "backend":
        assert (target_dir / "manage.py").is_file()
        assert (target_dir / "config" / "settings.py").is_file()
        assert (target_dir / "apps" / "items" / "models.py").is_file()
    elif framework == "general" and project_type == "backend":
        assert (target_dir / "pyproject.toml").is_file()
        assert (target_dir / "src" / "main.py").is_file()

def test_configure_database_sqlite(tmp_path):
    # Setup mock files
    req_file = tmp_path / "requirements.txt"
    env_file = tmp_path / ".env.example"
    
    req_file.write_text("fastapi\nsqlalchemy\npsycopg2-binary>=2.9.0\n", encoding="utf-8")
    env_file.write_text('PROJECT_NAME="Test"\nDATABASE_URL="postgresql://user:password@localhost:5432/dbname"\n', encoding="utf-8")
    
    from setupci.cli import configure_database
    configure_database(tmp_path, "fastapi", "SQLite")
    
    # Assert psycopg2-binary removed
    req_content = req_file.read_text(encoding="utf-8")
    assert "psycopg2" not in req_content
    
    # Assert DATABASE_URL updated
    env_content = env_file.read_text(encoding="utf-8")
    assert 'DATABASE_URL="sqlite:///./sql_app.db"' in env_content
    
    # Assert .env file created
    actual_env = tmp_path / ".env"
    assert actual_env.is_file()
    assert 'DATABASE_URL="sqlite:///./sql_app.db"' in actual_env.read_text(encoding="utf-8")

def test_configure_database_mysql(tmp_path):
    # Setup mock files
    req_file = tmp_path / "requirements.txt"
    env_file = tmp_path / ".env.example"
    
    req_file.write_text("fastapi\nsqlalchemy\npsycopg2-binary>=2.9.0\n", encoding="utf-8")
    env_file.write_text('PROJECT_NAME="Test"\nDATABASE_URL="postgresql://user:password@localhost:5432/dbname"\n', encoding="utf-8")
    
    from setupci.cli import configure_database
    configure_database(tmp_path, "fastapi", "MySQL")
    
    # Assert psycopg2-binary replaced by pymysql and cryptography
    req_content = req_file.read_text(encoding="utf-8")
    assert "psycopg2" not in req_content
    assert "pymysql>=1.1.0" in req_content
    assert "cryptography>=41.0.0" in req_content
    
    # Assert DATABASE_URL updated
    env_content = env_file.read_text(encoding="utf-8")
    assert 'DATABASE_URL="mysql+pymysql://user:password@localhost:3306/dbname"' in env_content

def test_cli_main_flow(tmp_path):
    from unittest.mock import patch
    import sys
    from setupci.cli import main

    target_dir = tmp_path / "my_project"
    
    # Mock sys.argv
    test_args = ["setupci", "init", str(target_dir)]
    
    with patch.object(sys, 'argv', test_args), \
         patch('questionary.select') as mock_select, \
         patch('questionary.confirm') as mock_confirm:
         
         # Mock framework selection -> FastAPI
         # Mock project type selection -> Backend
         # Mock database selection -> MySQL
         mock_select.return_value.ask.side_effect = ["FastAPI", "Backend", "MySQL"]
         mock_confirm.return_value.ask.return_value = True
         
         main()
         
    # Verify files created
    assert target_dir.exists()
    assert (target_dir / "app" / "main.py").is_file()
    assert (target_dir / "requirements.txt").is_file()
    assert (target_dir / ".env").is_file()
    
    # Verify MySQL driver added
    req_content = (target_dir / "requirements.txt").read_text(encoding="utf-8")
    assert "pymysql>=1.1.0" in req_content
    assert "psycopg2" not in req_content
    
    # Verify MySQL URL in .env
    env_content = (target_dir / ".env").read_text(encoding="utf-8")
    assert 'DATABASE_URL="mysql+pymysql://user:password@localhost:3306/dbname"' in env_content


