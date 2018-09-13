FROM python:2

MAINTAINER Njenga Saruni
RUN apt-get -y update && apt-get install -y \
   git \
   nginx

RUN pip install virtualenv
# Clone the workforce gitlab repo

WORKDIR /var/www
RUN mkdir api
COPY requirements.txt /var/www/api
WORKDIR /var/www/api
RUN pip install -r requirements.txt
COPY . /var/www/api

EXPOSE 80

COPY ./docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
