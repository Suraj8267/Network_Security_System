from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """
    This function will return the list of requirements
    """
    requirement_list:List[str] = []
    try:
        with open('requirements.txt', 'r') as file_obj:
            ## Read lines from the file
            lines = file_obj.readlines()
            ## Process each line
            for line in lines:
                requirement = line.strip()  ## strip() is used for removing \n and starting and ending extra zeros
                ## igrore empty lines and -e .
                if requirement and requirement != '-e.':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_list


## setup the metadata
setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Suraj Singh",
    author_email="singhsuraj182005@gmail.com",
    packages= find_packages(),
    install_requires= get_requirements()
)