#!/usr/bin/env python

from setuptools import setup, find_packages, Extension

setup(
	name = 'unicornhat',
	version = '1.1.0',
	author = 'Philip Howard',
	author_email = 'phil@pimoroni.com',
	url = 'https://github.com/pimoroni/ws2812-RPi/',
	description = """The Python library for UnicornHat a matrix of 64, eye-burning, ws2812 LEDs!""",
	long_description=open('README').read() + open('CHANGELOG').read(),
	py_modules = [ 'unicornhat' ],
	install_requires = ['ws2812 >= 1.1.0'],
)
