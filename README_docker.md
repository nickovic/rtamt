# docker

## docker install

<https://docs.docker.com/engine/install/ubuntu/>

## docker run

build image

```bash
docker build -t rtamt .
```

run container & run example

```bash
docker run -it rtamt bash
/rtamt# cd examples/offline_monitors/
/rtamt# python3 offline_monitor_dense_time.py 
```
