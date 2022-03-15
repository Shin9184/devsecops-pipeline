FROM fintu/python3.7

COPY flask ./my-flask
WORKDIR ./my-flask
RUN pip3 install --upgrade pip
RUN pip3 install Flask
RUN pip3 install pymysql