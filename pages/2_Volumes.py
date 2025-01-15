import streamlit as st

st.set_page_config(page_title="DuckDB GUI - Volumes", page_icon="🦆")

st.write(""" # 🦆 DuckDB GUI - Volumes """)

with st.spinner("Loading DuckDB Volumes..."):
    try: 
        with open('src/sql/volumes.sql', 'r') as file:
            sql = file.read()
        result = st.session_state.db.query_df(sql)

        selected = st.multiselect('Select tables:', result['table_name'].unique(), default=result['table_name'].unique())

        st.bar_chart(result[result['table_name'].isin(selected)], x='table_name', y='estimated_size', use_container_width=True)
        st.dataframe(result[result['table_name'].isin(selected)], hide_index=True)

    except Exception as e:
        st.error(f"Error!  - Exception: {e}")
