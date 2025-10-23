"""
GrowFit - Smart fitness app setup configuration.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="growfit",
    version="0.1.0",
    author="Ismael",
    description="Smart fitness app that grows with you - AI-powered workout recommendations and adaptive progression tracking",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/IRF1991/GrowFit",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Games/Entertainment",
        "Topic :: Multimedia",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
        ],
        "ml": [
            "scikit-learn>=1.3.0",
            "numpy>=1.24.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "growfit=growfit.app:run_app",
        ],
    },
    include_package_data=True,
    package_data={
        "growfit": ["data/*.csv"],
    },
)