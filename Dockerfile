FROM shin9184/flask
COPY ./flask/ ./copy
CMD ["cp", "-r", "./copy/*", "./"] 
