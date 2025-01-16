import streamlit as st
import src.queries as queries

st.set_page_config(page_title="DuckDB GUI - Catalog", page_icon="🦆")

st.write(""" # 🦆 DuckDB GUI - Catalog """)

with st.spinner("Loading DuckDB Catalog..."):
    try: 
        result = st.session_state.db.query_df(queries.catalog())

        tables = result['table_name'].unique()

        for table in tables:
            with st.expander(f"## {table}"):

                tab1, tab2, tab3 = st.tabs(["Columns", "Data Preview", "Lineage"])

                with tab1:
                    fields = st.session_state.db.query_df(queries.table_fields(table))
                    st.dataframe(fields, hide_index=True)
                with tab2:
                    size = st.session_state.db.query_df(queries.estimated_rows(table))
                    st.markdown(f"**Total estimated size:** {size.iloc[0]['size']}")
                    st.table(st.session_state.db.query_df(queries.data_preview(table)))
                with tab3:
                    st.header("TBD")

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