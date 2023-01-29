FROM python:3.9.6-alpine3.14
RUN apk update \
  && apk add \
    build-base \
    postgresql \
    postgresql-dev \
    libpq
RUN apk --no-cache add gcc musl-dev librdkafka-dev
RUN mkdir /producer
WORKDIR /producer
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
# python3 ./main.py --file_path /producer/CreditCardCustomers.csv --topic_name data --file_format csv --type_of_producer kafka