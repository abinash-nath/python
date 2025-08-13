import 

blob = ' path: ' \
client= gcsstorage.Client()
list_blobs = client.list_blobs('your-bucket-name', prefix='path/to/bronze/layer/', blob)

for blob in list_blobs:
    if blob.name.endswith('.csv'):
        df = spark.read.csv(blob.public_url, header=True, inferSchema=True)
        
        # Cast columns ending with _dt to date type
        for column in df.columns:
            if column.endswith('_dt'):
                df = df.withColumn(column, df[column].cast('date'))
        
        # Perform additional data cleaning as needed
        # For example, removing null values or duplicates
        df_cleaned = df.dropna().dropDuplicates()
        
        # Write cleaned data back to a new location
        cleaned_blob_path = 'path/to/cleaned/data/' + blob.name.split('/')[-1]
        df_cleaned.write.csv(cleaned_blob_path, header=True)


def class ColumnDataTypeChecker:
    def __init__(self, df):
        self.df = df

    def check_column_types(self):
        column_types = {}
        for column in self.df.columns:
            column_types[column] = str(self.df.schema[column].dataType)
        return column_types