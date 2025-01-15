import streamlit as st

st.set_page_config(page_title="DuckDB GUI - Volumes", page_icon="🦆")

st.write(""" # 🦆 DuckDB GUI - Volumes """)

with open('sql/volumes.sql', 'r') as file:
    sql = file.read()

result = st.session_state.db.query_df(sql)

st.bar_chart(result, x='table_name', y='estimated_size', use_container_width=True)

st.dataframe(result, hide_index=True)

