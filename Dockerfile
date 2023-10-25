FROM python:3.10
USER root

RUN apt-get update

WORKDIR /root/KU-WIKI

RUN pip install -r requirements.txt

RUN python -m mkdocs build

RUN python -m mkdocs serve -a 0.0.0.0:8000