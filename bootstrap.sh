#!/usr/bin/env bash
apt-get update
apt-get install -y python-pip
pip install fusepy

#install fuse
# apt-get install make
# cd /vagrant/fuse
# tar -xf fuse-2.9.5.tar
# cd fuse-2.9.5/
# ./configure
# make -j8
# make install