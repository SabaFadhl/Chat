FROM python:3.9
RUN apt-get update;

ENV PYTHONUNBUFFERED 1
RUN mkdir /ChatApp

ADD requirements.txt /ChatApp

WORKDIR /ChatApp

ADD entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD . /ChatApp
EXPOSE 8000