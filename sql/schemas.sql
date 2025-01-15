SELECT 
    t.table_name,
    c.column_name,
    c.data_type
FROM 
    information_schema.tables t
JOIN 
    information_schema.columns c
ON 
    t.table_name = c.table_name
WHERE 
    t.table_schema = 'main'
ORDER BY 
    t.table_name, c.ordinal_position;