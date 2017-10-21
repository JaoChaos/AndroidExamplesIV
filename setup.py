"""Setup file."""

# external imports
from setuptools import setup

# long description
with open("README.md", 'r') as f:
    long_description = f.read()

# requirements
requeriments = []

setup(
    name='AndroidExamplesIV',
    version='0.1',
    description='An app to help understand how different technologies work together.',
    long_description=long_description,
    license="GPLv3",
    author='Juan Anaya Ortiz',
    author_email='juan.anaya.ortiz@gmail.com',
    url="https://github.com/JaoChaos/AndroidExamplesIV",
    install_requires=requirements, )
