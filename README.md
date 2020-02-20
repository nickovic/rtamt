# rtamt

Specification-based real-time monitoring library

## Install

### Install back-ends

```bash
sudo apt install libboost-all-dev
sudo apt install python-dev
sudo apt install python-pip
```

If your work for TL development, following package is needed in addition.

```bash
sudo apt install antlr4
```

### Build the tool

#### clone the repository

```bash
git clone https://github.com/nickovic/rtamt
```

#### build cpp libs (required only if you want to use CPP backend)

```bash
cd rtamt/rtamt
mkdir build
cd build
cmake ../
make
```

#### install rtamt tool

```bash
cd rtamt/
sudo pip install .
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
