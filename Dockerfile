FROM python:3.7-slim

copy requirements.txt /tmp/

RUN pip install -r requirements.txt && \
    mkdir bayesclass

COPY . /bayesclass

RUN chmod +x /bayesclass/start.sh

WORKDIR /bayesclass

EXPOSE 8000

CMD ["/bayesclass/start.sh"]
