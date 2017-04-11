#!/usr/bin/env python

from setuptools import setup, find_packages, Extension

cpu = open('/proc/cpuinfo','r').read()

define = []

if 'ARMv7' in cpu:
  define = [('RPI2',''),('PERI_BASE','0x3F000000')]

_ws2812 = Extension(
    '_ws2812',
    define_macros = define,
    library_dirs= [ 'lib/' ],
    include_dirs= [ 'lib/' ],
    sources     = [
    'lib/ws2812-RPi.c',
    'ws2812-RPi_wrap.c' ]
)

setup(
    name        = 'ws2812',
    version     = '1.1.0',
    author      = 'Philip Howard',
    author_email= 'phil@pimoroni.com',
    url         = 'https://github.com/pimoroni/ws2812-RPi/',
    description = """A python interface to ws2812 RPi""",
    long_description=open('README').read(),
    ext_modules = [ _ws2812 ],
    py_modules  = [ 'ws2812' ],
    install_requires = [],
    headers     = [ 'lib/ws2812-RPi.h' ]
)
