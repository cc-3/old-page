FROM ubuntu:18.04

LABEL maintainer="CC-3 Machine Structures <cc3.staff@gmail.com>"

# General dependencies
RUN apt-get update && apt-get upgrade -y && \
    apt-get install --no-install-recommends build-essential \
    python3-dev python3-pip python3-setuptools libssl-dev libffi-dev \
    supervisor nginx -y && \
    echo "daemon off;" >> /etc/nginx/nginx.conf && \
    rm -f /etc/nginx/sites-enabled/default && \
    mkdir -p /root/.aws

# Python 3 requirements
COPY requirements.txt /
RUN pip3 install -r requirements.txt && rm -f requirements.txt

# Supervisor
COPY config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Setup Nginx
COPY config/autograders.conf /etc/nginx/sites-enabled

# Firebase credentials
COPY config/key.json /

# AWS S3 Bucket credentials
COPY config/config /root/.aws/
COPY config/credentials /root/.aws/

# SSL certificate
COPY config/cc3.key /etc/ssl/cc3.key
COPY config/cc3.pem /etc/ssl/cc3.pem

# Environment vars
ENV FIREBASE_KEY=/key.json
ENV FIREBASE_DB='https://test-autograders.firebaseio.com/'
ENV S3_BUCKET='autograders'

# Setup project
ADD server /opt/server
WORKDIR /opt/server

# production
EXPOSE 443

# dev
EXPOSE 5000

CMD ["/usr/bin/supervisord"]
