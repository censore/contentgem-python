from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="gemcontent-python",
    version="1.0.0",
    author="GemContent Team",
    author_email="support@gemcontent.com",
    description="Official Python SDK for GemContent API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gemcontent/gemcontent-python",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Text Processing :: Markup :: HTML",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.25.0",
        "typing-extensions>=3.7.4;python_version<'3.8'",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "pytest-asyncio>=0.14.0",
            "black>=21.0.0",
            "flake8>=3.8.0",
            "mypy>=0.800",
            "sphinx>=3.0.0",
            "sphinx-rtd-theme>=0.5.0",
        ]
    },
    keywords="gemcontent, api, sdk, python, content-generation, ai",
    project_urls={
        "Bug Reports": "https://github.com/gemcontent/gemcontent-python/issues",
        "Source": "https://github.com/gemcontent/gemcontent-python",
        "Documentation": "https://docs.gemcontent.com/api",
    },
) 