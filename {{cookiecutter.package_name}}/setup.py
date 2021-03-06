#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from pathlib import Path


setup(
    name="{{ cookiecutter.package_name }}",
    version="{{ cookiecutter.package_version }}",
    url="{{ cookiecutter.package_url }}",
    license='MIT',

    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.author_email }}",

    description="{{ cookiecutter.package_description }}",
    long_description=Path('README.md').open().read(),
    long_description_content_type="text/markdown",

    packages=["{{ cookiecutter.package_name }}"],

    # Derive version from git. If HEAD is at the tag, the version will be the tag itself.
    version_config={
        "version_format": "{tag}.dev{sha}",
        "starting_version": "0.0.1"
    },
    setup_requires=Path('requirements.txt').open().read(),

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    zip_safe=False,
)
