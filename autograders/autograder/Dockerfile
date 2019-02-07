FROM ubuntu:18.04

LABEL maintainer="CC-3 Machine Structures <cc3.staff@gmail.com>"

# General dependencies
RUN sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
    apt-get update && apt-get upgrade -y && \
    apt-get install --no-install-recommends build-essential make software-properties-common \
    python3-dev python3-pip python3-setuptools curl python3-wheel -y && \
    pip3 install tabulate pycrypto psutil pycparser && \
    echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
    add-apt-repository -y ppa:webupd8team/java && \
    apt-get update && \
    apt-get install -y oracle-java8-installer && \
    apt-get install -y oracle-java8-set-default && \
    curl $(curl -S https://api.github.com/repos/andrescv/V-Sim/releases/latest | grep 'browser_download_url' | cut -d '"' -f 4) -L -o vsim.jar && \
    mv vsim.jar /opt && printf '#!/bin/bash\njava -jar /opt/vsim.jar $@' > '/usr/bin/vsim' && chmod +x usr/bin/vsim && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /var/cache/oracle-jdk8-installer

CMD ["/usr/bin/bash"]
