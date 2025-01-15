import duckdb

class duckdb_client:
    def __init__(self):
        self.db = duckdb.connect("database/persistent_database_files.db")

    def health(self):
        return self.db.sql('''SELECT 1''')
    
    def query_df(self, query_string: str):
        return self.db.sql(f'''{query_string}''').df().reset_index(drop=True)

    def query_raw(self, query_string: str):
        return self.db.sql(f'''{query_string}''')
