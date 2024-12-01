FROM python:latest

WORKDIR /usr/src/app

RUN pip install requests

CMD ["tail", "-f", "/dev/null"]