######################################################################
### author = Rafael Zamora 
### copyright = Copyright 2020-2022, Next Project 
### date = 25/04/2022
### license = PSF
### version = 3.3.0
### maintainer = Rafael Zamora 
### email = rafa.zamora.ram@gmail.com 
### status = Production
######################################################################

#System Packages
import os

#Local Packages
import src.version_next

#Dependencies Packages
from setuptools import setup

def long_description_file():
    """Genrete long descriptions

    Returns:
        str: long description
    """
    # Get current Directory
    this_dir = os.getcwd()
    
    # Read file README.md
    with open(this_dir + '/README.md', encoding='utf-8') as f:
        long_description = f.read()
    return long_description

setup(
    # Name to find the package in PyPi
    name = 'next-pm',
    
    # Directory of code
    packages = ['src'],
    
    # Import files without extension .py
    include_package_data=True,
    
    # Version Current of Next
    version = src.version_next.VERSION,
    
    # Short description
    description = 'Next es un administrador de proyectos de C/C++, es diseñado como una solucion a la administracion que requieren este tipo de proyectos.)',
    
    # long description
    long_description=long_description_file(),
    
    # Name of Author
    author='Rafael Zamora',
    
    # email of Author
    author_email="rafa.zamora.ram@gmail.com",
    
    # License of proyect
    license="PSF",
    
    # Link of GitHub repository
    url="https://github.com/reitmas32/Next",
    
    # Classifiers of PyPi
    classifiers = ["Programming Language :: Python :: 3",\
        "License :: OSI Approved :: Python Software Foundation License",\
        "Development Status :: 5 - Production/Stable", "Intended Audience :: Developers", \
        "Operating System :: OS Independent", \
        "Topic :: Software Development :: Build Tools"],
    
    # Keywords 
    keywords=['C/C++', 'package', 'libraries', 'developer', 'manager',
              'dependency', 'tool', 'c', 'c++', 'cpp'],
    
    # Entry points
    entry_points={
        'console_scripts': [
            'next=src.main:main'
        ],
    }
    
)