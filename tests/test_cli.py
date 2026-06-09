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
