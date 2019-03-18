FROM python:3.7

RUN mkdir /server
WORKDIR /server

ADD requirements.txt ./

RUN pip install -r requirements.txt

ADD ./server ./

CMD gunicorn -b 0.0.0.0:8000 run:app