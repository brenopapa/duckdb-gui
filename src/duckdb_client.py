import duckdb
import pandas as pd

class duckdb_client:
    def __init__(self):
        self.db = duckdb.connect("database/persistent_database_files.db")

    def health(self):
        return self.db.sql('''SELECT 1''')
    
    def query(self, query_string: str, return_df: bool = True):
        
        result = self.db.sql(f'''{query_string}''')

        if result is None:
            return pd.DataFrame(columns=['message'], data=[['Executed Successfully - The response of query was empty.']])
        
        if return_df:
            return result.df().reset_index(drop=True)
        
        return result
