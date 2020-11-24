#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup, find_packages


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding="utf-8").read()


setup(
    name="pytest-factoryboy-state",
    entry_points={
        "pytest11": [
            "factoryboy-state = pytest_factoryboy_state",
        ],
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    version="0.1.0",
    author="Holger Rother",
    author_email="hrother@hrother.org",
    maintainer="Holger Rother",
    maintainer_email="hrother@hrother.org",
    license="MIT",
    url="https://github.com/hrother/pytest-factoryboy-state",
    description="Simple factoryboy random state management",
    long_description=read("README.rst"),
    py_modules=["pytest_factoryboy_state"],
    python_requires=">=3.5",
    install_requires=["pytest>=5.0"],
    use_scm_version={"write_to": "src/pytest_factoryboy_state/_version.py"},
    setup_requires=["setuptools_scm"],
    extras_require={"dev": ["pre-commit", "tox"]},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Pytest",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
)
