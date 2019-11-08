# rtamt
Specification-based real-time monitoring library

# Install
## Install back-ends
```
$ sudo apt install libboost-all-dev
$ sudo apt install python-dev
$ sudo apt install python-pip
```
If your work for TL development, following package is needed in addition. 
```
$ sudo apt install antlr4
```
## Build the tool
### clone the repository
```
$ git clone https://github.com/nickovic/rtamt
```
### build cpp libs
```
$ cd rtamt/rtamt
$ mkdir build
$ cd build
$ cmake ../
$ make
```
### install rtamt tool
```
$ cd rtamt/
$ sudo pip install .
```

# Run
## online-STL example
```
$ cd rtamt/example
$ ./monitor_basic.py 
time=0 rob=-98.0
time=1 rob=-98.0
time=2 rob=-98.0
```

## offline-STL example
```
$ cd rtamt/example
$ ./monitor_offline.py 
Robustness: -98.0

```

## Io-STL example
```
$ cd rtamt/example
$ ./monitor_iostl.py 
time=0 rob=-98.0
time=1 rob=-98.0
time=2 rob=-98.0
```
