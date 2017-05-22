# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='flask_app_example',
    version='0.1',
    description='A demo app on how to deploy Python apps developed with the Flask framework',
    author='Nil Portugués Calderó',
    author_email='contact@nilportugues.com',
    url='http://nilportugues.com/',
    license='BSD',
    packages=find_packages(exclude=('tests', 'docs')), 
    install_requires=[
        'flask'
    ],
    include_package_data=True, 
)

# EOF
