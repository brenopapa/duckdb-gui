select
    table_name,
    estimated_size
from duckdb_tables()
order by estimated_size desc;
