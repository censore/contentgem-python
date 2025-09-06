#!/usr/bin/env python3
"""
Build and publish script for ContentGem Python SDK
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path


def run_command(command: str, description: str) -> bool:
    """Run a command and return success status."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"   Command: {command}")
        print(f"   Error: {e.stderr}")
        return False


def clean_build() -> None:
    """Clean build artifacts."""
    print("🧹 Cleaning build artifacts...")
    dirs_to_clean = ["build", "dist", "*.egg-info"]
    for pattern in dirs_to_clean:
        for path in Path(".").glob(pattern):
            if path.is_dir():
                shutil.rmtree(path)
                print(f"   Removed {path}")
    
    # Clean Python cache
    for path in Path(".").rglob("__pycache__"):
        if path.is_dir():
            shutil.rmtree(path)
            print(f"   Removed {path}")


def build_package() -> bool:
    """Build the package."""
    commands = [
        ("python3 -m pip install --upgrade build", "Installing build tools"),
        ("python3 -m build", "Building package"),
    ]
    
    for command, description in commands:
        if not run_command(command, description):
            return False
    
    return True


def check_package() -> bool:
    """Check the built package."""
    commands = [
        ("python3 -m pip install --upgrade twine", "Installing twine"),
        ("python3 -m twine check dist/*", "Checking package"),
    ]
    
    for command, description in commands:
        if not run_command(command, description):
            return False
    
    return True


def publish_package(test: bool = True) -> bool:
    """Publish the package to PyPI."""
    if test:
        repository = "testpypi"
        print("🧪 Publishing to Test PyPI...")
    else:
        repository = "pypi"
        print("🚀 Publishing to PyPI...")
    
    command = f"python3 -m twine upload --repository {repository} dist/*"
    return run_command(command, f"Publishing to {repository}")


def main():
    """Main function."""
    if len(sys.argv) > 1 and sys.argv[1] == "--help":
        print("""
ContentGem Python SDK Build Script

Usage:
    python build.py [options]

Options:
    --clean     Clean build artifacts only
    --build     Build package only
    --check     Check built package only
    --test      Publish to Test PyPI
    --publish   Publish to PyPI
    --all       Clean, build, check, and publish to Test PyPI
    --release   Clean, build, check, and publish to PyPI

Examples:
    python build.py --clean
    python build.py --build
    python build.py --test
    python build.py --release
        """)
        return
    
    # Default action
    action = sys.argv[1] if len(sys.argv) > 1 else "--all"
    
    if action == "--clean":
        clean_build()
        return
    
    if action == "--build":
        clean_build()
        if not build_package():
            sys.exit(1)
        return
    
    if action == "--check":
        if not check_package():
            sys.exit(1)
        return
    
    if action == "--test":
        clean_build()
        if not build_package():
            sys.exit(1)
        if not check_package():
            sys.exit(1)
        if not publish_package(test=True):
            sys.exit(1)
        return
    
    if action == "--publish":
        clean_build()
        if not build_package():
            sys.exit(1)
        if not check_package():
            sys.exit(1)
        if not publish_package(test=False):
            sys.exit(1)
        return
    
    if action == "--all":
        clean_build()
        if not build_package():
            sys.exit(1)
        if not check_package():
            sys.exit(1)
        if not publish_package(test=True):
            sys.exit(1)
        return
    
    if action == "--release":
        clean_build()
        if not build_package():
            sys.exit(1)
        if not check_package():
            sys.exit(1)
        if not publish_package(test=False):
            sys.exit(1)
        return
    
    print(f"❌ Unknown action: {action}")
    print("Use --help for usage information")
    sys.exit(1)


if __name__ == "__main__":
    main()
