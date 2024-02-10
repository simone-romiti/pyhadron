#!/bin/bash

sudo apt-get -y install r-base r-base-core # (check that you don't have 2 or more versions installed)
sudo apt-get -y install libpoppler-cpp-dev
sudo apt-get -y install libxml2-dev
sudo apt-get -y install libmagick++-dev
sudo apt-get -y install openjdk-11-jdk openjdk-11-jre

sudo R CMD javareconf

pip install pyyaml
python3 gen_scripts.py # generation of installation scripts

bash deps.sh # dependencies (some are unnecessary, but useful for .Rmd files)
bash hadron_inst.sh # installation
bash manual.sh # documentation

rm -rf hadron_github/