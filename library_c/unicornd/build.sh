#!/bin/bash
git submodule update --init
sudo apt install scons
cd rpi_ws281x
scons
cd ../
make

