#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='inpval',
    version='1.0',
    description='Input Validation Tool',
    author='Justin Paro',
    author_email='justin.paro@gmail.com',
    packages=find_packages(include=['inpval*'])
)