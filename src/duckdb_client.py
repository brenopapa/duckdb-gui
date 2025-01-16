import duckdb
import pandas as pd
import uuid
import time
import re


class duckdb_client:
    def __init__(self):
        self.db = duckdb.connect("database/persistent_database_files.db")

    def health(self):
        return self.db.sql('''SELECT 1''')
    
    # def audit(self, query_data: dict):
    #     try:
    #         self.db.sql(f'''SELECT * FROM audit LIMIT 1''')
    #     except Exception as e:
    #         self.db.sql(f'''CREATE TABLE IF NOT EXISTS audit (id VARCHAR PRIMARY KEY, took FLOAT)''')
    #     finally:
    #         self.db.sql(f'''INSERT INTO audit VALUES ('{query_data['id']}', {query_data['took']})''')
        
    #     return True

    def query(self, query_string: str, return_df: bool = True):
        
        start_time = time.time()

        result = self.db.sql(f'''{query_string}''')

        end_time = time.time()

        query_data = {
            'id': uuid.uuid4(),
            'took': end_time - start_time
        }

        # self.audit(query_data)

        if result is None:
            return pd.DataFrame(columns=['message'], data=[['Executed Successfully - The response of query was empty.']])
        
        if return_df:
            return result.df().reset_index(drop=True)
        
        return result
