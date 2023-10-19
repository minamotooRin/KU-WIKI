FROM python:3.10
USER root

RUN apt-get update

WORKDIR /root


COPY requirements.txt /root/


RUN pip install -r /root/requirements.txt

RUN python -m mkdocs build

RUN python -m mkdocs serve -a 0.0.0.0:8000