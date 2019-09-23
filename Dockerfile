FROM python:3.7 

ENV PYTHONUNBUFFERED 1

RUN mkdir /Music_Hack

WORKDIR /Music_Hack

ADD . /Music_Hack/

RUN pip install -r requirement.txt

EXPOSE 8000
