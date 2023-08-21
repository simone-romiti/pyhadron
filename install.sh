#!/bin/bash

cp info.yaml pyhadron/

pip3 install .



echo "cleaning up"
rm -r build/ pyhadron.egg-info/
