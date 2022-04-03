FROM python:3

WORKDIR /app

ADD . /app
RUN python3 -m pip install -U pip
RUN pip3 install flask uwsgi pymysql

CMD ["uwsgi","uwsgi.ini"]
