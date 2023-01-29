FROM apache/spark-py:v3.3.0
USER root
RUN apt-get update -y &&\
    apt-get install -y python3
RUN apt-get install -y postgresql
RUN apt-get install wget -y
RUN wget https://jdbc.postgresql.org/download/postgresql-42.2.5.jar -P /opt/spark/jars
RUN mkdir /spark_streaming
WORKDIR /spark_streaming
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
# python3 ./streaming.py