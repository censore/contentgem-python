# Publishing ContentGem Python SDK

This document explains how to publish the ContentGem Python SDK to PyPI.

## Prerequisites

1. **PyPI Account**: Create an account at [PyPI](https://pypi.org) and [Test PyPI](https://test.pypi.org)
2. **API Tokens**: Generate API tokens for both PyPI and Test PyPI
3. **Build Tools**: Install required build tools

```bash
pip install --upgrade build twine
```

## Configuration

### 1. Configure PyPI Credentials

Create `~/.pypirc` file:

```ini
[distutils]
index-servers = pypi testpypi

[pypi]
username = __token__
password = pypi-your-api-token-here

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-your-test-api-token-here
```

### 2. Environment Variables (Alternative)

Instead of `~/.pypirc`, you can use environment variables:

```bash
export TWINE_USERNAME=__token__
export TWINE_PASSWORD=pypi-your-api-token-here
export TWINE_REPOSITORY_URL=https://upload.pypi.org/legacy/
```

## Publishing Process

### 1. Test Build

First, test the build process:

```bash
python build.py --build
```

### 2. Check Package

Verify the built package:

```bash
python build.py --check
```

### 3. Test on Test PyPI

Publish to Test PyPI first:

```bash
python build.py --test
```

### 4. Test Installation from Test PyPI

```bash
pip install --index-url https://test.pypi.org/simple/ contentgem-python
```

### 5. Publish to PyPI

Once tested, publish to production PyPI:

```bash
python build.py --publish
```

## Manual Publishing

If you prefer manual steps:

### 1. Clean and Build

```bash
# Clean previous builds
rm -rf build/ dist/ *.egg-info/

# Build package
python -m build
```

### 2. Check Package

```bash
python -m twine check dist/*
```

### 3. Upload to Test PyPI

```bash
python -m twine upload --repository testpypi dist/*
```

### 4. Upload to PyPI

```bash
python -m twine upload dist/*
```

## Version Management

### Update Version

1. Update version in `contentgem/__init__.py`:

   ```python
   __version__ = "1.2.1"
   ```

2. Update version in `setup.py`:

   ```python
   version="1.2.1",
   ```

3. Update `CHANGELOG.md` with new features/fixes

### Semantic Versioning

Follow [Semantic Versioning](https://semver.org/):

- **MAJOR**: Incompatible API changes
- **MINOR**: New functionality in a backwards compatible manner
- **PATCH**: Backwards compatible bug fixes

## Post-Publication

### 1. Verify Installation

```bash
pip install contentgem-python
python -c "import contentgem; print(contentgem.__version__)"
```

### 2. Test CLI

```bash
contentgem --help
```

### 3. Update Documentation

- Update README.md if needed
- Update API documentation
- Update examples

## Troubleshooting

### Common Issues

1. **Package already exists**: Increment version number
2. **Authentication failed**: Check API tokens in `~/.pypirc`
3. **Build failed**: Check for syntax errors and missing dependencies
4. **Upload failed**: Check network connection and PyPI status

### Useful Commands

```bash
# Check package contents
tar -tzf dist/contentgem-python-*.tar.gz

# Test local installation
pip install dist/contentgem-python-*.whl

# Uninstall for testing
pip uninstall contentgem-python
```

## Security Notes

- Never commit API tokens to version control
- Use environment variables or `~/.pypirc` for credentials
- Test on Test PyPI before production release
- Keep API tokens secure and rotate them regularly
