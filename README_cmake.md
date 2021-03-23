# cmake install

This would be needed for Ubuntu 18.04 and 16.04 to satisfy cmake version 3.12 or grater.
This document is based on [cmake install guid page](https://cmake.org/install/)

## install needed packages

```bash
apt-get install libssl-dev
apt-get install wget
```

## cmake download & install

```bash
wget https://github.com/Kitware/CMake/releases/download/v3.19.3/cmake-3.19.3.tar.gz
tar -zxvf cmake-3.19.3.tar.gz
cd cmake-3.19.3
./bootstrap
make -j $(nproc)
sudo make install
```
