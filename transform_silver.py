import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import boto3

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Caminhos
bronze_path = "s3://traffic-sp/bronze/"
silver_path = "s3://traffic-sp/silver/"

# Lista somente arquivos .json reais
s3 = boto3.client("s3")
bucket = "traffic-sp"
prefix = "bronze/"

response = s3.list_objects_v2(Bucket=bucket, Prefix=prefix)

json_files = [
    obj["Key"].replace("bronze/", "")
    for obj in response.get("Contents", [])
    if obj["Key"].endswith(".json")
]

print("Arquivos detectados:", json_files)

for file in json_files:
    df = (
        spark.read
            .option("multiline", "true")
            .json(bronze_path + file)
    )

    table_name = file.replace(".json", "")

    df.write.mode("overwrite").parquet(f"{silver_path}{table_name}/")

job.commit()
