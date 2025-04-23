from setuptools import setup, find_packages
import unittest

def discover_tests():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    return test_suite

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read().splitlines()

setup(
    name="remind",
    version="0.1.0",
    author="Vladimir Syerik",
    author_email="vladimir@syerik.net",
    description="A toolkit for analyzing personal journal entries",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vsyerik/remind",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=requirements,
    include_package_data=True,
    package_data={
        "src": ["config.yaml"],  # updated to match your actual package folder
    },
    entry_points={
        "console_scripts": [
            "remind-pulse=src.pulse:main",  # updated to match your actual package/module
        ],
    },
    test_suite='setup.discover_tests',
)
