FROM fintu/python3.7

RUN mkdir ./flask-app
COPY . flask-app
WORKDIR ./flask-app

CMD ["python3", "run2.py"]
