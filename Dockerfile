FROM fintu/python3.7

WORKDIR ./flask
RUN pip3 freeze > requirements.txt
RUN pip install -r requirements.txt

CMD ["python3", "run2.py"]
