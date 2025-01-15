def schemas():
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
    estimated_size
FROM duckdb_tables()
ORDER BY 
    estimated_size desc;
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
                    LIMIT 10
            '''.format(table=table)
    return query