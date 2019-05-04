FROM ubuntu:latest
MAINTAINER Facundo Sanchez
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install flask
COPY app.py app.py
ENTRYPOINT ["python3","app.py"]