#!/usr/bin/env bash
apt-get update

#get fuse and unzip it
wget https://github.com/libfuse/libfuse/releases/download/fuse_2_9_5/fuse-2.9.5.tar.gz
tar -xzf fuse-2.9.5.tar.gz
cd fuse-2.9.5/
#install fuse
apt-get install -y make
sed -i 's/2:9:4/2:9:5/' lib/Makefile.in &&

./configure --prefix=/usr    \
            --disable-static \
            INIT_D_PATH=/tmp/init.d &&

make

#install python fuse bindings and html request libraries
apt-get install -y python3
apt-get install -y python3-pip
mkdir /home/vagrant/tmp
pip3 install fusepy
pip3 install requests