FROM ubuntu:20.04

RUN apt-get update \
    && apt-get install -y python3-pip python3-dev\
    && cd /usr/local/bin \
    && ln -s /usr/bin/python3 python \
    && pip3 install --upgrade pip

RUN mkdir /code
WORKDIR /code
COPY  . /code/
RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]