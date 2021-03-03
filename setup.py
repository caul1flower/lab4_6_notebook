from setuptools import setup

with open("README", 'r') as f:
    long_description = f.read()

setup(
   name='Notebook',
   version='1.0',
   description='A useful module for taking notes',
   license="MIT",
   long_description=long_description,
   author='Anita Hrodzytska',
   author_email='hrodzytska@ucu.edu.ua',
   url="-",
   packages=['Notebook'],
   install_requires=['menu', 'notebook', 'command_option'],
)