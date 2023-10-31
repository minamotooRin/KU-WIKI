FROM python:3.10
USER root

RUN apt-get update

WORKDIR /root/KU-WIKI

COPY requirements.txt /root/KU-WIKI

RUN pip install -r requirements.txt