FROM ubuntu:18.04

LABEL maintainer="CC-3 Machine Structures <cc3.staff@gmail.com>"

# General dependencies
RUN apt-get update && apt-get upgrade -y && \
    apt-get install --no-install-recommends build-essential make \
    python3-dev python3-pip python3-setuptools python3-wheel -y && \
    pip3 install tabulate pycrypto psutil pycparser && \
    apt-get --purge remove openjdk* && \
    echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true" | debconf-set-selections && \
    echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" > /etc/apt/sources.list.d/webupd8team-java-trusty.list && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 && \
    apt-get update && \
    apt-get install -y --no-install-recommends oracle-java8-installer oracle-java8-set-default && \
    apt-get clean all && \
    rm -rf /var/lib/apt/lists/*

CMD ["/usr/bin/bash"]
