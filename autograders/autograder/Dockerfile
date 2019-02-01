FROM ubuntu:18.04

LABEL maintainer="CC-3 Machine Structures <cc3.staff@gmail.com>"

# General dependencies
RUN apt-get update && apt-get upgrade -y && \
    apt-get install --no-install-recommends build-essential make \
    python3-dev python3-pip python3-setuptools python3-wheel -y && \
    pip3 install tabulate pycrypto psutil pycparser && \
    rm -rf /var/lib/apt/lists/*

CMD ["/usr/bin/bash"]
