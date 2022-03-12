FROM fintu/python3.7

WORKDIR ./flask
RUN /usr/local/bin/python3 -m pip3 install --upgrade pip3
RUN pip3 install -r requirements.txt

CMD ["python3", "run2.py"]
