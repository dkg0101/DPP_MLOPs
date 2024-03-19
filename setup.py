from setuptools import setup, find_packages
from typing import List

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()     
   

__version__ = "0.0.1"
REPO_NAME = "DPP_MLOPs"
PKG_NAME= "DPP_MLOPs"
AUTHOR_USER_NAME = "dkg0101"
AUTHOR_EMAIL = "dkgurav0101@gmail.com"
HYPEN_E_DOT = '-e .'

def get_requirements(filepath:str):
    requirements= []
    with open(filepath) as file:
        requirements = file.readlines()
        requirements = [req.replace('\n','') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements



setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for predicting DIAMOND Prices.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},

    install_requires = get_requirements('./requirements_dev.txt')
    )