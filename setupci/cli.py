import os
import sys
import argparse
from pathlib import Path
import importlib.resources
import questionary

def copy_template(src_traversable, dest_path):
    """
    Recursively copy files from a Traversable (packaged resource) to a local Path.
    """
    if src_traversable.is_dir():
        dest_path.mkdir(parents=True, exist_ok=True)
        for item in src_traversable.iterdir():
            # Skip python internal caches
            if item.name == "__pycache__":
                continue
            copy_template(item, dest_path / item.name)
    elif src_traversable.is_file():
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        content = src_traversable.read_bytes()
        dest_path.write_bytes(content)

def main():
    parser = argparse.ArgumentParser(description="setupci - Python Project Bootstrapper")
    
    subparsers = parser.add_subparsers(dest="command")
    init_parser = subparsers.add_parser("init", help="Initialize a new project")
    init_parser.add_argument("path", nargs="?", default=".", help="Target directory for initialization")
    
    args = parser.parse_args()
    
    # If no command or wrong command, show help
    if args.command != "init":
        parser.print_help()
        sys.exit(1)
        
    target_dir = Path(args.path).resolve()
    
    print("\n🚀 Welcome to setupci Project Bootstrapper!")
    print("=" * 45)
    
    # 1. Ask for framework
    framework_choice = questionary.select(
        "Which framework would you like to use?",
        choices=[
            "FastAPI",
            "Flask",
            "Django",
            "General Python"
        ]
    ).ask()
    
    if not framework_choice:
        print("❌ Initialization cancelled.")
        sys.exit(1)
        
    # Map to directory name
    framework_map = {
        "FastAPI": "fastapi",
        "Flask": "flask",
        "Django": "django",
        "General Python": "general"
    }
    framework = framework_map[framework_choice]
    
    # 2. Ask for project type
    type_choice = questionary.select(
        "Which project type would you like to build?",
        choices=[
            "Backend (Professional API / App Structure)",
            "Simple (Basic starting script / setup)"
        ]
    ).ask()
    
    if not type_choice:
        print("❌ Initialization cancelled.")
        sys.exit(1)
        
    # Map to directory name
    type_map = {
        "Backend (Professional API / App Structure)": "backend",
        "Simple (Basic starting script / setup)": "simple"
    }
    project_type = type_map[type_choice]
    
    # 3. Confirm target directory
    print(f"\n📂 Target directory: {target_dir}")
    if target_dir.exists() and any(target_dir.iterdir()):
        confirm = questionary.confirm(
            "⚠️  Target directory is not empty. Do you want to continue?",
            default=False
        ).ask()
        if not confirm:
            print("❌ Initialization cancelled.")
            sys.exit(0)
            
    # 4. Perform the copy
    print(f"\n⚡ Creating {framework_choice} ({project_type}) project...")
    
    try:
        # Load the resource path using importlib.resources
        src_path = importlib.resources.files("setupci.templates") / framework / project_type
        
        if not src_path.exists():
            print(f"❌ Error: Template {framework}/{project_type} does not exist.")
            sys.exit(1)
            
        copy_template(src_path, target_dir)
        
        print("\n✨ Project initialized successfully!")
        print("=" * 45)
        print("Next steps:")
        print(f"  1. Navigate to: cd {args.path}")
        print("  2. Read the README.md for instructions on running the project.")
        print("=" * 45)
        
    except Exception as e:
        print(f"❌ Error occurred during project creation: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
