FROM ubuntu:18.04
WORKDIR /rtamt
COPY . ./
RUN apt-get update && apt-get install -y \
    libboost-all-dev \
    python3.6 \
    python3-dev \
    python3-pip
# for cmake
RUN apt-get install -y \
    libssl-dev \
    wget
RUN wget https://github.com/Kitware/CMake/releases/download/v3.19.3/cmake-3.19.3.tar.gz && \
    tar -zxvf cmake-3.19.3.tar.gz
RUN cd cmake-3.19.3 && \
    ./bootstrap && \
    make && \
    make install
# for rtamt C++ build
RUN cd /rtamt && mkdir -p rtamt/build && \
    cd rtamt/build && \
    cmake -DPythonVersion=3 ../ && \
    make
# install rtamt
RUN pip3 install .