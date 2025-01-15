import streamlit as st
import src.queries as queries

st.set_page_config(page_title="DuckDB GUI - Schemas", page_icon="🦆")

st.write(""" # 🦆 DuckDB GUI - Schemas """)

with st.spinner("Loading DuckDB Schemas..."):
    try: 
        result = st.session_state.db.query_df(queries.schemas())

        tables = result['table_name'].unique()

        for table in tables:
            st.write(f"## {table}")

            st.write(f"### Columns")
            fields = st.session_state.db.query_df(queries.table_fields(table))
            st.dataframe(fields, hide_index=True)

            st.write(f"### Data Preview")

            st.table(st.session_state.db.query_df(queries.data_preview(table)))

            st.divider()

    except Exception as e:
        st.error(f"Error!  - Exception: {e}")

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