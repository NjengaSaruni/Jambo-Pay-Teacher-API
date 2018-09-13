FROM python:2

MAINTAINER njengasaruni@gmail.com
LABEL author="Njenga Saruni"

RUN apt-get update && \
    apt-get clean && rm -rf var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip install --upgrade pip

ENV PYTHONUNBUFFERED 1
RUN mkdir /var/www && \
    mkdir /var/www/riverlearn-api

COPY /requirements.txt /var/www/riverlearn-api/

WORKDIR  /var/www/riverlearn-api/
RUN pip install -r requirements.txt

COPY . /var/www/riverlearn-api/

EXPOSE 8000
ENTRYPOINT ["/var/www/riverlearn-api/docker/api/docker-entrypoint.sh"]