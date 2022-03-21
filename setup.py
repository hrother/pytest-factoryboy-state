#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import annotations

from setuptools import find_packages
from setuptools import setup


setup(
    name="pytest-factoryboy-state",
    entry_points={
        "pytest11": [
            "factoryboy-state = pytest_factoryboy_state",
        ],
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.7",
    install_requires=["pytest>=5.0", "factory_boy>=3.1.0"],
    use_scm_version={"write_to": "src/pytest_factoryboy_state/_version.py"},
    setup_requires=["setuptools_scm"],
    author="Holger Rother",
    author_email="hrother@hrother.org",
    maintainer="Holger Rother",
    maintainer_email="hrother@hrother.org",
    license="MIT",
    url="https://github.com/hrother/pytest-factoryboy-state",
    description="Simple factoryboy random state management",
    long_description=open("README.rst", encoding="utf-8").read(),
    py_modules=["pytest_factoryboy_state"],
    extras_require={"dev": ["pre-commit", "tox"]},
    keywords="pytest factoryboy",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Pytest",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
)
