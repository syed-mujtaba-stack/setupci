import os
import sys
import argparse
import importlib.resources
from pathlib import Path

import questionary
from questionary import Style
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich import box
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich.columns import Columns
from rich.align import Align

console = Console()

# ─── Custom questionary style ─────────────────────────────────────────────────
custom_style = Style([
    ("qmark",        "fg:#7c3aed bold"),
    ("question",     "bold fg:#e2e8f0"),
    ("answer",       "fg:#34d399 bold"),
    ("pointer",      "fg:#7c3aed bold"),
    ("highlighted",  "fg:#7c3aed bold"),
    ("selected",     "fg:#34d399"),
    ("separator",    "fg:#4b5563"),
    ("instruction",  "fg:#6b7280 italic"),
])

# ─── ASCII Banner ──────────────────────────────────────────────────────────────
BANNER = r"""
 ███████╗███████╗████████╗██╗   ██╗██████╗  ██████╗██╗
 ██╔════╝██╔════╝╚══██╔══╝██║   ██║██╔══██╗██╔════╝██║
 ███████╗█████╗     ██║   ██║   ██║██████╔╝██║     ██║
 ╚════██║██╔══╝     ██║   ██║   ██║██╔═══╝ ██║     ██║
 ███████║███████╗   ██║   ╚██████╔╝██║     ╚██████╗██║
 ╚══════╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝      ╚═════╝╚═╝
"""

# ─── Framework info table ─────────────────────────────────────────────────────
FRAMEWORK_INFO = {
    "FastAPI":        ("⚡", "Async Python API framework — Blazing fast, auto OpenAPI docs"),
    "Flask":          ("🌶️ ", "Lightweight WSGI micro-framework — Simple and flexible"),
    "Django":         ("🎸", "Batteries-included web framework — Full-stack powerhouse"),
    "General Python": ("🐍", "Pure Python project — Library, script, or CLI tool"),
}

TYPE_INFO = {
    "Backend": ("🏗️ ", "Professional structure — Clean architecture, Docker, env config"),
    "Simple":  ("⚡", "Quick start — Minimal boilerplate, single-file setup"),
}

def print_banner():
    """Print the welcome banner."""
    banner_text = Text(BANNER, style="bold #7c3aed")
    console.print(Align.center(banner_text))
    console.print(
        Align.center(
            Text("Python Project Bootstrapper", style="bold #e2e8f0") +
            Text("  •  ", style="#4b5563") +
            Text("v0.1.2", style="#7c3aed")
        )
    )
    console.print()

def print_framework_table():
    """Print available frameworks as a styled table."""
    table = Table(
        box=box.ROUNDED,
        border_style="#4b5563",
        show_header=True,
        header_style="bold #7c3aed",
        padding=(0, 1),
        expand=False,
    )
    table.add_column("Framework",    style="bold #e2e8f0", min_width=16)
    table.add_column("Description",  style="#94a3b8")

    for name, (icon, desc) in FRAMEWORK_INFO.items():
        table.add_row(f"{icon}  {name}", desc)

    console.print(Align.center(table))
    console.print()

def print_files_table(target_dir: Path):
    """Print generated files as a styled list."""
    files = []
    for f in sorted(target_dir.rglob("*")):
        if f.is_file() and "__pycache__" not in str(f):
            relative = f.relative_to(target_dir)
            files.append(str(relative))

    if not files:
        return

    table = Table(
        box=box.SIMPLE,
        show_header=True,
        header_style="bold #7c3aed",
        border_style="#4b5563",
        padding=(0, 1),
    )
    table.add_column("📁 Generated Files", style="#94a3b8")

    for f in files:
        parts = f.replace("\\", "/").split("/")
        if len(parts) > 1:
            table.add_row(f"  [#4b5563]{'/' .join(parts[:-1])}/[/#4b5563][#e2e8f0]{parts[-1]}[/#e2e8f0]")
        else:
            table.add_row(f"  [#e2e8f0]{f}[/#e2e8f0]")

    console.print(Panel(table, border_style="#4b5563", padding=(0, 1)))

def copy_template(src_traversable, dest_path):
    """Recursively copy files from a Traversable resource to a local Path."""
    if src_traversable.is_dir():
        dest_path.mkdir(parents=True, exist_ok=True)
        for item in src_traversable.iterdir():
            if item.name == "__pycache__":
                continue
            copy_template(item, dest_path / item.name)
    elif src_traversable.is_file():
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        content = src_traversable.read_bytes()
        dest_path.write_bytes(content)

def main():
    parser = argparse.ArgumentParser(
        description="setupci — Python Project Bootstrapper",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command")
    init_parser = subparsers.add_parser("init", help="Initialize a new project")
    init_parser.add_argument("path", nargs="?", default=".", help="Target directory (default: .)")

    args = parser.parse_args()

    if args.command != "init":
        parser.print_help()
        sys.exit(1)

    target_dir = Path(args.path).resolve()

    # ── Welcome Screen ───────────────────────────────────────────────────────
    console.clear()
    print_banner()
    print_framework_table()

    console.print(
        Panel(
            "[#94a3b8]Answer a few questions and your project structure will be ready in seconds.[/#94a3b8]",
            title="[bold #7c3aed]🚀 Getting Started[/bold #7c3aed]",
            border_style="#7c3aed",
            padding=(0, 2),
        )
    )
    console.print()

    # ── Step 1: Framework Selection ──────────────────────────────────────────
    framework_choice = questionary.select(
        "  Which framework would you like to use?",
        choices=[
            questionary.Choice(f"⚡  FastAPI        — Async Python API framework",        value="FastAPI"),
            questionary.Choice(f"🌶️   Flask          — Lightweight micro-framework",        value="Flask"),
            questionary.Choice(f"🎸  Django         — Full-stack web framework",           value="Django"),
            questionary.Choice(f"🐍  General Python — Library, script, or CLI project",   value="General Python"),
        ],
        style=custom_style,
    ).ask()

    if not framework_choice:
        console.print("\n[bold red]✗  Initialization cancelled.[/bold red]")
        sys.exit(1)

    # ── Step 2: Project Type Selection ───────────────────────────────────────
    console.print()
    type_choice = questionary.select(
        "  Which project type would you like?",
        choices=[
            questionary.Choice("🏗️   Backend  — Professional structure, Docker, env config", value="Backend"),
            questionary.Choice("⚡  Simple   — Minimal boilerplate, quick start",            value="Simple"),
        ],
        style=custom_style,
    ).ask()

    if not type_choice:
        console.print("\n[bold red]✗  Initialization cancelled.[/bold red]")
        sys.exit(1)

    # Map to directory names
    framework = {
        "FastAPI": "fastapi", "Flask": "flask",
        "Django": "django", "General Python": "general"
    }[framework_choice]

    project_type = {"Backend": "backend", "Simple": "simple"}[type_choice]

    # ── Step 3: Confirm if directory not empty ───────────────────────────────
    console.print()
    if target_dir.exists() and any(target_dir.iterdir()):
        console.print(
            Panel(
                f"[yellow]⚠️  Directory is not empty:[/yellow] [bold]{target_dir}[/bold]",
                border_style="yellow",
                padding=(0, 2),
            )
        )
        confirm = questionary.confirm(
            "  Continue anyway?",
            default=False,
            style=custom_style,
        ).ask()
        if not confirm:
            console.print("\n[bold red]✗  Initialization cancelled.[/bold red]")
            sys.exit(0)

    # ── Summary Panel ────────────────────────────────────────────────────────
    console.print()
    summary = Table.grid(padding=(0, 2))
    summary.add_column(style="bold #7c3aed")
    summary.add_column(style="#e2e8f0")
    summary.add_row("Framework:", framework_choice)
    summary.add_row("Type:",      type_choice)
    summary.add_row("Location:",  str(target_dir))

    console.print(
        Panel(summary, title="[bold #7c3aed]📋 Project Summary[/bold #7c3aed]",
              border_style="#4b5563", padding=(0, 1))
    )
    console.print()

    # ── Copy Files with Spinner ───────────────────────────────────────────────
    try:
        src_path = importlib.resources.files("setupci.templates") / framework / project_type

        if not src_path.exists():
            console.print(f"\n[bold red]✗  Template not found:[/bold red] {framework}/{project_type}")
            sys.exit(1)

        with Progress(
            SpinnerColumn(spinner_name="dots", style="#7c3aed"),
            TextColumn("[bold #e2e8f0]Generating project files..."),
            transient=True,
            console=console,
        ) as progress:
            progress.add_task("", total=None)
            copy_template(src_path, target_dir)

        # ── Success Message ───────────────────────────────────────────────────
        console.print(
            Panel(
                f"[bold #34d399]✓  Your {framework_choice} {type_choice.lower()} project is ready![/bold #34d399]",
                border_style="#34d399",
                padding=(0, 2),
            )
        )
        console.print()

        # ── Generated Files ───────────────────────────────────────────────────
        print_files_table(target_dir)
        console.print()

        # ── Next Steps ────────────────────────────────────────────────────────
        next_steps = Table.grid(padding=(0, 1))
        next_steps.add_column(style="bold #7c3aed", min_width=4)
        next_steps.add_column(style="#e2e8f0")

        steps = [
            ("1.", f"cd {args.path}"),
            ("2.", "python -m venv venv  &&  venv\\Scripts\\activate"),
            ("3.", "pip install -r requirements.txt"),
            ("4.", "Read README.md for framework-specific run instructions"),
        ]
        for num, step in steps:
            next_steps.add_row(num, step)

        console.print(
            Panel(
                next_steps,
                title="[bold #7c3aed]📌 Next Steps[/bold #7c3aed]",
                border_style="#4b5563",
                padding=(0, 1),
            )
        )
        console.print()
        console.print(Align.center(Text("Happy Coding! 🎉", style="bold #7c3aed")))
        console.print()

    except Exception as e:
        console.print(f"\n[bold red]✗  Error:[/bold red] {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
