#!/usr/bin/env python

from setuptools import setup, find_packages, Extension

setup(
	name = 'Unicorn Hat',
	version = '1.0.0',
	author = 'Philip Howard',
	author_email = 'phil@pimoroni.com',
	url = '',
	description = """The Python library for UnicornHat a matrix of 64, eye-burning, ws2812 LEDs!""",
	long_description=open('README').read() + open('CHANGELOG').read(),
	py_modules = [ 'UnicornHat' ],
	install_requires = ['ws2812'],
)
