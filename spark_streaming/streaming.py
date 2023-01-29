from pyspark.sql.functions import *
from pyspark.sql import SparkSession
from pyspark.sql.streaming import *
from pyspark.sql.types import *


def parse_json(df):
    schema = StructType([
        StructField("CLIENTNUM", IntegerType(), True),
        StructField("Attrition_Flag", StringType(), True),
        StructField("Customer_Age", IntegerType(), True),
        StructField("Gender", StringType(), True),
        StructField("Dependent_count", IntegerType(), True),
        StructField("Education_Level", StringType(), True),
        StructField("Marital_Status", StringType(), True),
        StructField("Income_Category", StringType(), True),
        StructField("Card_Category", StringType(), True),
        StructField("Months_on_book", IntegerType(), True),
        StructField("Total_Relationship_Count", IntegerType(), True),
        StructField("Months_Inactive_12_mon", IntegerType(), True),
        StructField("Contacts_Count_12_mon", IntegerType(), True),
        StructField("Credit_Limit", IntegerType(), True),
        StructField("Total_Revolving_Bal", IntegerType(), True),
        StructField("Avg_Open_To_Buy", IntegerType(), True),
        StructField("Total_Amt_Chng_Q4_Q1", DoubleType(), True),
        StructField("Total_Trans_Amt", IntegerType(), True),
        StructField("Total_Trans_Ct", IntegerType(), True),
        StructField("Total_Ct_Chng_Q4_Q1", DoubleType(), True),
        StructField("Avg_Utilization_Ratio", DoubleType(), True),
        StructField("Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1", DoubleType(), True),
        StructField("Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2", DoubleType(), True)
    ])

    parsed_df = df \
        .withColumn("json_data", from_json(col("value"), schema)) \
        .select("json_data.*")

    parsed_df = parsed_df \
        .withColumnRenamed('Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1', 'Flag_Education_Level_Months_Inactive_12_mon_1') \
        .withColumnRenamed('Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2', 'Flag_Education_Level_Months_Inactive_12_mon_2')

    return parsed_df


def process_data(df, batch_id):
    df.write.format("jdbc") \
        .option("url", "jdbc:postgresql://172.20.0.4:5432/postgres") \
        .option("driver", "org.postgresql.Driver")\
        .option("dbtable", "credit_card_customers") \
        .option("user", "zahar")\
        .option("password", "zahar")\
        .save()


spark = SparkSession \
    .builder \
    .appName("Spark Kafka Streaming") \
    .master("local[2]") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.0") \
    .config("spark.jars", "/opt/spark/jars/postgresql-42.2.5.jar") \
    .getOrCreate()

df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "data") \
    .option("startingOffsets", "earliest") \
    .load()

df = df \
    .selectExpr("CAST(value AS STRING) AS value")

df_parsed = parse_json(df)

df_filtered = df_parsed \
    .where('Income_Category != "Unknown"')

query = df_filtered \
    .writeStream \
    .outputMode("append") \
    .foreachBatch(process_data) \
    .start()

query.awaitTermination()

