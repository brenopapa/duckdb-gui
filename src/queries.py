def catalog():
    query = """
    SELECT
        t.table_name,
        c.column_name,
        c.data_type
    FROM
        information_schema.tables AS t
    INNER JOIN
        information_schema.columns AS c
        ON
            t.table_name = c.table_name
    WHERE
        t.table_schema = 'main'
    ORDER BY
        t.table_name, c.ordinal_position;
    """
    return query

def settings():
    query = """
    SELECT
        name,
        value,
        description,
        input_type,
        scope
    FROM duckdb_settings();
    """
    return query


def volumes():
    query = """
SELECT
    table_name,
    estimated_size as estimated_rows,
    ROUND((estimated_size * 100.0) / total_size, 2) || '%' AS percentage_of_total
FROM (
    SELECT
        table_name,
        estimated_size,
        SUM(estimated_size) OVER () AS total_size
    FROM duckdb_tables()
) t
ORDER BY 
    estimated_size DESC;
    """
    return query

def table_fields(table):

    query = '''
                    SELECT
                        c.column_name,
                        c.data_type
                    FROM
                        information_schema.tables AS t
                    INNER JOIN
                        information_schema.columns AS c
                        ON
                            t.table_name = c.table_name
                    WHERE
                        t.table_schema = 'main'
                        AND t.table_name = '{table}'
                    ORDER BY
                        t.table_name, c.ordinal_position;
            '''.format(table=table)
    return query

def data_preview(table):

    query = '''
                    SELECT *
                    FROM
                        {table} AS t
                    USING SAMPLE 10
            '''.format(table=table)
    return query

def estimated_rows(table):

    query = '''
SELECT
    CONCAT(
    estimated_size, ' rows (',
    ROUND((estimated_size * 100.0) / total_size, 2), '%', ' of total database)') as size
FROM (
    SELECT
        table_name,
        estimated_size,
        SUM(estimated_size) OVER () AS total_size
    FROM duckdb_tables()
    
) t
WHERE table_name = '{table}'
ORDER BY 
    estimated_size DESC;
            '''.format(table=table)
    return query

def ingestion_timeline(table, ingestion_field):

    ingestion_field = '_ingestionDateTime' if ingestion_field is None else ingestion_field

    query = '''
        SELECT 
        CAST({ingestion_field} AS DATE) as _ingestionDate,
        COUNT(*) AS rows
        FROM {table}
        GROUP BY _ingestionDate
        '''.format(table=table, ingestion_field=ingestion_field)
    return query