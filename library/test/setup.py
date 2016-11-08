#!/usr/bin/env python

try:
    from setuptools import setup, find_packages, Extension
except ImportError:
    from distutils.core import setup, find_packages, Extension

setup(
    name            = 'Unicorn Hat',
    version         = '1.0.0',
    author          = 'Philip Howard',
    author_email    = 'phil@pimoroni.com',
    url             = '',
    description     = """Python library for Unicorn HAT""",
    long_description=open('README.txt').read() + open('CHANGELOG.txt').read(),
    py_modules      = [ 'UnicornHat' ]
)
