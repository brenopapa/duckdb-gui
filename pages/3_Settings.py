import streamlit as st
import src.queries as queries

st.set_page_config(page_title="DuckDB GUI - Settings", page_icon="🦆")

st.write(""" # 🦆 DuckDB GUI - Settings """)

result = st.session_state.db.query_raw(queries.settings())

for row in result.df().itertuples():
        st.text_input(key=f'input_{row.name}', label=f'{row.name} - {row.description} ({row.input_type})', value=row.value, placeholder=row.value)
        if st.button(key=f'button_{row.name}', label='Update'):
            with st.spinner(f"Updating DuckDB setting {row.name}..."):
                try:
                    st.session_state.db.query(f"SET {row.name} = '{st.session_state.get(f'input_{row.name}')}'")
                    st.success(f"Setting '{row.name}' updated!")
                except Exception as e:
                    st.error(f"Error updating config: {e}")
        st.divider()
