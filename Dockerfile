FROM shin9184/flask
WORKDIR /
COPY ./flask/ /tmp
RUN copy -r /tmp/ /app
