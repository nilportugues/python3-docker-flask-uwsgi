FROM ubuntu:16.04
LABEL Description="A container for the production hosting of a flask application"

RUN apt-get update && apt-get upgrade -y

# Install nginx
RUN apt-get install -y nginx

## Python 3 installation and required packages
RUN apt-get install libterm-readline-perl-perl apt-utils -y
RUN apt-get install -y python3 python3-pip python3-virtualenv mlocate
RUN pip3 install --upgrade pip
RUN pip3 install flask uwsgi


COPY ./flask_app_example-0.1.tar.gz /tmp/build.tar.gz
RUN pip3 install /tmp/build.tar.gz --upgrade

## Copy files for uwsgi
RUN mkdir -p /opt/uwsgi/
COPY ./uwsgi/uwsgi.ini /opt/uwsgi/uwsgi.ini
COPY ./uwsgi/app.wsgi /var/www/app.wsgi

## Copy files for nginx
COPY ./nginx/conf/app.conf /etc/nginx/sites-enabled/app.conf
RUN rm /etc/nginx/sites-enabled/default

# Exposed ports
EXPOSE 80

## Copy over the entrypoint
COPY ./entrypoint.sh /usr/bin/entrypoint.sh
RUN chmod +x /usr/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]
