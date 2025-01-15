import streamlit as st
import src.duckdb_client as ddb

from src.custom_elements import table

st.session_state.db = ddb.duckdb_client()

st.set_page_config(page_title="DuckDB GUI - Home", page_icon="🦆")

st.write(""" # 🦆 DuckDB GUI - Home """)

with st.form("Input SQL"):
    query = st.text_area(label='Input SQL', label_visibility='hidden', placeholder='Input SQL', height=300)

    submit = st.form_submit_button("Submit")

    if submit:
        with st.spinner("Checking DuckDB..."):
            try: 
                st.session_state.db.health()
            except Exception as e:
                st.error(f"Error!  - Exception: {e}")
                
        with st.spinner("Querying..."):
            try:
                st.table(st.session_state.db.query(query))
            except Exception as e:
                st.error(f"Error!  - Exception: {e}")
