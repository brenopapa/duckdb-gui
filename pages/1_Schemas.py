import streamlit as st

st.set_page_config(page_title="DuckDB GUI - Schemas", page_icon="🦆")

st.write(""" # 🦆 DuckDB GUI - Schemas """)

with open('sql/schemas.sql', 'r') as file:
    sql = file.read()

result = st.session_state.db.query_df(sql)

st.dataframe(result, hide_index=True)

        # CREATE OR REPLACE TABLE financial AS 
        # SELECT * FROM read_csv('./data/data.csv',
        #             delim = ',',
        #             header = true,
        #             columns = {
        #                 'id': 'INTEGER',
        #                 'signal': 'VARCHAR',
        #                 'category': 'VARCHAR',
        #                 'value': 'FLOAT',
        #                 'date': 'DATE'
        #             });