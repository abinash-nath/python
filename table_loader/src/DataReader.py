from pyspark.sql import SparkSession

class DataReader:
    def __init__(self, spark: SparkSession):
        self.spark = spark

    def read_file(self, file_path):
        if file_path.endswith(".csv"):
            return self.spark.read.option("header", True).csv(file_path)
        elif file_path.endswith(".json"):
            return self.spark.read.json(file_path)
        elif file_path.endswith(".parquet"):
            return self.spark.read.parquet(file_path)
        else:
            raise ValueError(f"Unsupported file type: {file_path}")
