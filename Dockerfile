FROM fintu/python3.7

COPY . /flask
WORKDIR ./flask
RUN pip3 install --upgrade pip
RUN pip3 install Flask
RUN pip3 install pymysql

CMD ["python3", "run2.py"]
