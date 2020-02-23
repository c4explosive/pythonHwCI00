FROM jenkins:latest
USER root
RUN mkdir /hw_app
WORKDIR /hw_app
COPY requirements.txt /hw_app
RUN pwd
RUN ls -la
RUN apt-get update
RUN apt-get install -y python-pip
