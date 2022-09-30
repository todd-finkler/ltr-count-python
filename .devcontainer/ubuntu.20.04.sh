#!/bin/bash

apt-get update -y
apt-get install -y python3.8-dev python3-pip gcc gdb
pip3 install -r requirements.txt