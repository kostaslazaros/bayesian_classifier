FROM python:3.7-slim

RUN mkdir bayesclass

COPY . /bayesclass

RUN pip install -r /bayesclass/requirements.txt

RUN chmod +x /bayesclass/start.sh

WORKDIR /bayesclass

EXPOSE 5000 8000

CMD ["/bayesclass/start.sh"]
