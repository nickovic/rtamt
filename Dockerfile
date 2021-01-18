FROM ubuntu:18.04
WORKDIR /rtamt
COPY . ./
RUN apt-get update && apt-get install -y \
    libboost-all-dev \
    python3.6 \
    python3-dev \
    python3-pip
RUN pip3 install .