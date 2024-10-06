# from setuptools import find_packages,setup
# from typing import List

# HYPHEN_E_DOT = '-e .'
# def get_requirements(file_path:str)->list[str]:
#     """Returns a list of requirements from a requirements.txt file."""
#     requirements=[]
#     with open(file_path) as file_obj:
#         requirements=file_obj.readlines()
#         requirements= [req.replace("\n","") for req in requirments] 

#         if HYPHEN_E_DOT in requirements:
#             requirements.remove(HYPHEN_E_DOT)

#         return requirements
# setup(
#     name='my_package',
#     version='1.0.0',
#     author='Azhar Ali',
#     author_email='azharali@gmail.com',
#     packages=find_packages(),   
#     install_requires=get_requirements('requirements.txt')

# )




from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """Returns a list of requirements from a requirements.txt file."""
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and req.strip() != HYPHEN_E_DOT]
    return requirements

setup(
    name='my_package',
    version='1.0.0',
    author='Azhar Ali',
    author_email='azharali@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
