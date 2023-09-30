import io
import os
import re
from setuptools import setup, find_packages

scriptFolder = os.path.dirname(os.path.realpath(__file__))
os.chdir(scriptFolder)

# Find version info from module (without importing the module):
with open("src/morellet/__init__.py", "r") as fileObj:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fileObj.read(), re.MULTILINE
    ).group(1)

# Use the README.md content for the long description:
with io.open("README.md", encoding="utf-8") as fileObj:
    long_description = fileObj.read()

setup(
    name="Francois Morellet Generator",
    version=version,
    url="https://github.com/asweigart/morellet",
    author="Al Sweigart",
    author_email="al@inventwithpython.com",
    description=("""Generates art in the style of the 1960 piece by Francois Morellet, "Random Distribution of 40,000 Squares Using the Odd and Even Numbers of a Telephone Directory"."""),
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    test_suite="tests",
    install_requires=["pillow"],
    keywords="",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
