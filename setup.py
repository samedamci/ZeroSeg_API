#!/usr/bin/env python3

from setuptools import setup, find_packages
import os

with open("README.md", "r") as readme:
    long_description = readme.read()


def read(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()


setup(
    name="ZeroSeg-API",
    version="0.3",
    author="samedamci",
    author_email="samedamci@disroot.org",
    description=("REST API for ZeroSeg Improved library."),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/samedamci/ZeroSeg_API",
    project_urls={"Issue tracker": "https://github.com/samedamci/ZeroSeg_API/issues"},
    packages=find_packages(),
    license="ISC",
    keywords="raspberry pi rpi led max7219 matrix seven segment zeroseg api",
    python_requires=">=3.6",
    install_requires=read('requirements.txt').splitlines(),
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Operating System :: POSIX :: Linux",
    ],
)
