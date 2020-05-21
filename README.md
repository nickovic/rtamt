# rtamt

Specification-based real-time monitoring library

## Install

### Install prerequisites for RTAMT installation

```bash
sudo apt install libboost-all-dev
sudo apt install python-dev
sudo apt install python-pip
```

If your want to extend the specification language, you may need the ANTLR4 parser generator.

```bash
sudo apt install antlr4
```

You will also need CMake version 3.12 or higher if you need to build the CPP backend.

```bash
sudo apt install cmake
```

### Build the tool

#### clone the repository

```bash
git clone https://github.com/nickovic/rtamt
```

#### build CPP libraries for Python 2 
#### (This step is needed only if you want to use the CPP backend)
#### (This step can be skipped if you want to use pure Python monitors)

```bash
cd rtamt/rtamt
mkdir build
cd build
cmake -DPythonVersion=2 ../
make
```

#### install RTAMT for Python 2

```bash
cd rtamt/
sudo pip2 install .
```

#### build CPP libraries for Python 3 
#### (This step is needed only if you want to use the CPP backend)
#### (This step can be skipped if you want to use pure Python monitors)

```bash
cd rtamt/rtamt
mkdir build
cd build
cmake -DPythonVersion=3 ../
make
```

#### install RTAMT for Python 3

```bash
cd rtamt/
sudo pip3 install .
```

#### uninstall RTAMT (Python 2)

```bash
sudo pip2 uninstall rtamt
```

#### uninstall RTAMT (Python 3)

```bash
sudo pip3 uninstall rtamt
```

## Run examples

### online-STL example

```bash
cd rtamt/examples/basic
$ python monitor_basic.py
time=0 rob=122.0
time=1 rob=3.0
time=2 rob=-10.0
```

### offline-STL example

```bash
cd rtamt/examples/basic
$ python monitor_offline.py
Robustness: -98.0
```

### Io-STL example

```bash
cd rtamt/examples/offline_monitors
$ python offline_monitor_dt.py
Example (a) - standard robustness: 3.0
Example (a) - output robustness: 3.0
Example (a) - input vacuity: 0
Example (b) - standard robustness: 1.0
Example (b) - output robustness: inf
Example (b) - input vacuity: 1.0
Example (c) - standard robustness: -2.0
Example (c) - output robustness: -2.0
Example (c) - input vacuity: 0
Example (d) - standard robustness: -1.0
Example (d) - output robustness: -2.0
Example (d) - input vacuity: 0
```
