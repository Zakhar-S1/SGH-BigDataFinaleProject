FROM python:3.9.6-alpine3.14
RUN apk update \
  && apk add \
    build-base \
    postgresql \
    postgresql-dev \
    libpq
RUN mkdir /analytics
WORKDIR /analytics
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
# python3 ./main.py