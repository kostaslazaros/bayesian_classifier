FROM python:alpine

RUN pip install sklearn pandas flask flask_cors && \
    mkdir bayesclass

COPY . /bayesclass

RUN chmod +x /bayesclass/start.sh

WORKDIR /bayesclass

EXPOSE 8000

CMD ["/bayesclass/start.sh"]
