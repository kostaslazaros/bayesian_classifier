FROM python:alpine

RUN apk --no-cache add build-base python-dev && \ 
    pip install sklearn pandas flask flask_cors gunicorn && \
    apk del build-base python-dev && \
    mkdir bayesclass

COPY . /bayesclass

RUN chmod +x /bayesclass/start.sh

WORKDIR /bayesclass

EXPOSE 8000

CMD ["/bayesclass/start.sh"]
