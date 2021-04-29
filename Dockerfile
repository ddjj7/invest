FROM python:3.7
ENV PATH /usr/local/bin:$PATH
ADD . /code
WORKDIR /code
#RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 627220E7
#RUN echo 'deb http://archive.scrapy.org/ubuntu scrapy main' | tee /etc/apt/sources.list.d/scrapy.list
#RUN apt-get update && apt-get install -y scrapy
