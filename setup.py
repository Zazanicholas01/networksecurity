from setuptools import find_packages, setup
from typing import List

def get_requirements():
    """Returns list of requirements"""

    requirement_list = []
    try:
        with open('requirements.txt', 'r') as file:

            lines = file.readlines() # Read lines from requirements.txt

            for line in lines:
                requirement = line.strip()

                # Ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_list

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Zazanicholas01",
    author_email="matteoesposito12.me@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
