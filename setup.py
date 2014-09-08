#!/usr/bin/env python

from setuptools import setup, find_packages, Extension

_ws2812 = Extension(
	'_ws2812',
	library_dirs=[
		'.'
	],
	sources=[
		'ws2812-RPi.c',
		'ws2812-RPi_wrap.c'
	]
)

setup(
	name = 'ws2812',
	version = '1.0.0',
	author = 'Philip Howard',
	author_email = 'phil@pimoroni.com',
	url = '',
	description = """A python interface to ws2812 RPi""",
	long_description=open('README').read(),
	ext_modules = [ _ws2812 ],
	py_modules = [ 'ws2812' ],
	install_requires = [],
	headers = [
		'ws2812-RPi.h'
	]
)
