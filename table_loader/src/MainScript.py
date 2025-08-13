from pyspark.sql import SparkSession
from config.settings import BUCKET_NAME
from src.gcs_connector import GCSConnector
from src.data_reader import DataReader
from src.schema_handler import SchemaHandler
from src.data_cleaner import DataCleaner
from src.column_caster import ColumnCaster
from src.pipeline import Pipeline

if __name__ == "__main__":
    spark = SparkSession.builder.appName("GCS PySpark Pipeline").getOrCreate()

    gcs_connector = GCSConnector(BUCKET_NAME)
    data_reader = DataReader(spark)
    schema_handler = SchemaHandler()
    data_cleaner = DataCleaner()
    column_caster = ColumnCaster()

    pipeline = Pipeline(gcs_connector, data_reader, schema_handler, data_cleaner, column_caster)
    pipeline.run(prefix="incoming/")
