# setup.py
from setuptools import setup, find_packages

setup(
    name='project_two',
    version='0.5',
    packages=find_packages(where='src\my_package'),
    package_dir={'': 'src\my_package'},
    install_requires=[
        'pandas',
        'requests',
        'beautifulsoup4'
    ]
)