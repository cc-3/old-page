FROM ubuntu:18.04

LABEL maintainer="CC-3 Machine Structures <cc3.staff@gmail.com>"

# General dependencies
RUN apt-get update && apt-get upgrade -y
RUN apt-get install build-essential git -y

# Python 3
RUN apt-get install python3-dev python3-pip libssl-dev libffi-dev -y
COPY requirements.txt /
RUN pip3 install -r requirements.txt
RUN rm -f requirements.txt

# Supervisor
RUN apt-get install supervisor -y
COPY config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Setup Nginx
RUN apt-get install nginx -y
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY config/autograders.conf /etc/nginx/sites-available
RUN ln -s /etc/nginx/sites-available/autograders.conf /etc/nginx/sites-enabled
RUN rm -f /etc/nginx/sites-enabled/default

# Setup App
COPY key.json /
ENV FIREBASE_DB='https://cc-3-autograders.firebaseio.com/'
ENV FIREBASE_KEY=/key.json
ADD server /opt/server
WORKDIR /opt/server

# production
EXPOSE 80
# dev
EXPOSE 5000

CMD ["/usr/bin/supervisord"]
