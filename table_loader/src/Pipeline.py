class Pipeline:
    def __init__(self, gcs_connector, data_reader, schema_handler, data_cleaner, column_caster):
        self.gcs_connector = gcs_connector
        self.data_reader = data_reader
        self.schema_handler = schema_handler
        self.data_cleaner = data_cleaner
        self.column_caster = column_caster

    def run(self, prefix=None):
        file_paths = self.gcs_connector.list_files(prefix)
        for path in file_paths:
            df = self.data_reader.read_file(path)
            df = self.schema_handler.normalize_columns(df)
            df = self.data_cleaner.clean(df)
            df = self.column_caster.cast_date_columns(df)
            df.show()
