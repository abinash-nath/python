from pyspark.sql.types import DateType
from pyspark.sql.functions import col

class ColumnCaster:
    @staticmethod
    def cast_date_columns(df):
        for column in df.columns:
            if column.endswith("_dt"):
                df = df.withColumn(column, col(column).cast(DateType()))
        return df
