from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)-> List[str]:
    """
    THis function will return the list of requriemnts
    """
    req = []
    with open(file_path) as file:
        req = file.readlines()
        req = [i.replace("\n","") for i in req]
        
        if "-e ." in req:
            req.remove("-e .")

    return req


setup(
    name = "ML Proeject",
    version="0.0.1",
    author="Rajan",
    author_email="rshukla2k@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')

)
