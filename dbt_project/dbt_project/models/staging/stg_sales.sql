{{ config(materialized='view') }}

SELECT
    sale_id,
    product_id,
    product_name,
    category,
    quantity,
    price,
    customer_id,
    customer_name,
    region,
    sale_date,
    payment_method
FROM 's3://sales-data/sales.csv'
