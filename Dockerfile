# Credits to cnstark for the pytorch installation
# Here is the link to the repository I based this Dockerfile on: https://github.com/cnstark/pytorch-docker/

FROM ubuntu:22.04

RUN apt update && \
    apt install -y \
        wget build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev \
        libreadline-dev libffi-dev libsqlite3-dev libbz2-dev liblzma-dev && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

RUN cd /tmp && \
    wget https://www.python.org/ftp/python/3.10.14/Python-3.10.14.tgz && \
    tar -xvf Python-3.10.14.tgz && \
    cd Python-3.10.14 && \
    ./configure --enable-optimizations && \
    make && make install && \
    cd .. && rm Python-3.10.14.tgz && rm -r Python-3.10.14 && \
    ln -s /usr/local/bin/python3 /usr/local/bin/python && \
    ln -s /usr/local/bin/pip3 /usr/local/bin/pip && \
    python -m pip install --upgrade pip && \
    rm -r /root/.cache/pip

RUN pip install \
    	torch==2.3.1+cpu \
	torchvision==0.18.1+cpu \
    	-f https://download.pytorch.org/whl/cpu/torch_stable.html && \
    pip install \
    	numpy \
    	pillow \
    	eventlet \
    	flask \
   	python-socketio==4.2.1 && \
    rm -r /root/.cache/pip

WORKDIR /workspace
