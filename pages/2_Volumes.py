import streamlit as st
import src.queries as queries

st.set_page_config(page_title="DuckDB GUI - Volumes", page_icon="🦆")

st.write(""" # 🦆 DuckDB GUI - Volumes """)

with st.spinner("Loading DuckDB Volumes..."):
    try: 
        result = st.session_state.db.query(queries.volumes())

        selected = st.multiselect('Select tables:', result['table_name'].unique(), default=result['table_name'].unique())
        
        st.divider()

        ingestion_data = {}

        for table in result['table_name'].unique():
            try:
                timeline = st.session_state.db.query(queries.ingestion_timeline(table, st.session_state.get(f'input_ingestion_field')))['rows'].tolist()            
                result.loc[result['table_name'] == table, 'ingestion_timeline'] = str(timeline)
            except Exception as e:
                timeline = []

        st.bar_chart(result[result['table_name'].isin(selected)], x='table_name', y='estimated_rows', use_container_width=True)
        st.dataframe(result[result['table_name'].isin(selected)], hide_index=True, column_config={"ingestion_timeline": st.column_config.LineChartColumn("ingestion_timeline")})

    except Exception as e:
        st.error(f"Error!  - Exception: {e}")
