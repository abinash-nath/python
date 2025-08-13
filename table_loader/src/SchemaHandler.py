class SchemaHandler:
    @staticmethod
    def normalize_columns(df):
        for col in df.columns:
            df = df.withColumnRenamed(col, col.lower().strip())
        return df
