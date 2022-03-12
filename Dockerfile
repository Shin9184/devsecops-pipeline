FROM fintu/python3.7

WORKDIR ./flask
RUN pip3 install -r requirements.txt

CMD ["python3", "run2.py"]
