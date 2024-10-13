from setuptools import setup, find_packages

setup(
    name="Text-Summarizer",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
    ],
)

with open("Readme.md","r",encoding="utf-8") as f:
    long_description = f.read()

__version__="0.0.0"

REPO_NAME="Text-Summarizer"
Author_USER_NAME="virend3rp"
SRC_REPO="Text-Summarizer"
AUTHOR_eMAIL="parasariyav@gmail.com"

