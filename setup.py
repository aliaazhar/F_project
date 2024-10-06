from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirment(file_path:str)->list[str]:
    """Returns a list of requirements from a requirements.txt file."""
    requirments=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        requirments= [req.replace("\n","") for req in requirments] 

        if HYPHEN_E_DOT in requirments:
            requirments.remove(HYPHEN_E_DOT)

        return requirments
setup(
    name='my_package',
    version='1.0.0',
    author='Azhar Ali',
    author_email='azharali@gmail.com',
    packages=find_packages(),   
    install_requires=get_requirment('requirmrnts.txt')

)