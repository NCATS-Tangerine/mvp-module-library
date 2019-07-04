from setuptools import setup, find_packages

VERSION = '0.0.2'

requires = [
    'ontobio',
    'mygene',
    'pandas',
    'typing',
    'graphviz',
]

setup(
    name='mvp-module-library',
    version= VERSION,
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/NCATS-Tangerine/mvp-module-library',
    install_requires = requires,
    python_requires='>=3.7',
    description='A collection of modules for executing MVP Workflows'
)
