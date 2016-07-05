#!/usr/bin/env python
# Python wrapper for the rpi_ws281x library.
# Author: Tony DiCola (tony@tonydicola.com)
from setuptools import setup, find_packages, Extension
from setuptools.command.build_py import build_py
import subprocess

class CustomInstallCommand(build_py):
    """Customized install to run library Makefile"""
    def run(self):
        print("Compiling ws281x library...")
        subprocess.Popen(["make","-Clib","lib"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        build_py.run(self)

setup(name              = 'rpi_ws281x',
      version           = '2.0.2',
      author            = 'Jeremy Garff',
      author_email      = 'jer@jers.net',
      description       = 'Userspace Raspberry Pi PWM library for WS281X LEDs.',
      license           = 'MIT',
      url               = 'https://github.com/jgarff/rpi_ws281x/',
      cmdclass          = {'build_py':CustomInstallCommand},
      py_modules        = ['neopixel'],
      ext_modules       = [Extension('_rpi_ws281x', 
                                     sources=['rpi_ws281x_wrap.c'],
                                     include_dirs=['lib/'],
                                     library_dirs=['lib/'],
                                     libraries=['ws2811'])])
