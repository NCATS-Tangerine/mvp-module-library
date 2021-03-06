from setuptools import setup, find_packages

VERSION = '0.1.0'

with open("README.md", "r") as fh:
    long_description = fh.read()

requires = [
    'ontobio',
    'mygene',
    'pandas',
    'typing',
    'graphviz',
]

setup(
    name='mvp-module-library',
    version=VERSION,
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/NCATS-Tangerine/mvp-module-library',
    install_requires=requires,
    python_requires='>=3.6',
    description='A collection of modules for executing MVP Workflows',
    long_description=long_description,
    long_description_content_type="text/markdown"
)
