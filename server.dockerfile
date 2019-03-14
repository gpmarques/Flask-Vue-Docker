FROM python:3.7

RUN mkdir /server
WORKDIR /server

ADD requirements.txt ./

RUN pip install -r requirements.txt

ADD ./server ./

CMD python run.py