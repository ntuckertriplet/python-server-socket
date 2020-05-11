FROM python:3.8

WORKDIR /srv

COPY . /srv/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

CMD ["python", "/srv/first_server.py"]
