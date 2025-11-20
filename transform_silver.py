import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import *

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

acc = spark.read.parquet("s3://traffic-sp/silver/accidents/")
flow = spark.read.parquet("s3://traffic-sp/silver/traffic_flow/")

gold = acc.join(flow, "location", "left") \
          .groupBy("location") \
          .agg(
              countDistinct("accident_id").alias("accidents"),
              avg("speed").alias("avg_speed")
          )

gold.write.mode("overwrite").parquet("s3://traffic-sp/gold/traffic_summary/")

job.commit()
