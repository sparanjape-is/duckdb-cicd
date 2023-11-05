import duckdb
duckdb.sql("""ATTACH 'csv_db.db' as csv_db;
                CREATE SCHEMA IF NOT EXISTS csv_db.jaffle_shop;
                USE csv_db.jaffle_shop;
                CREATE TABLE IF NOT EXISTS customers AS SELECT * from 'raw_customers.csv';
                CREATE TABLE IF NOT EXISTS orders AS SELECT * from 'raw_orders.csv';
                CREATE TABLE IF NOT EXISTS payments AS SELECT * from 'raw_payments.csv';
            """)
# Show statements
# duckdb.sql("SELECT * from customers ").show()
# duckdb.sql("SELECT * from payments ").show()
df = duckdb.sql("""select first_name,last_name 
           from customers c
           inner join orders o
           on o.user_id = c.id
           inner join payments p
           on o.id = p.order_id
           where p.amount > 2500;
           """).fetchdf()

print(df.shape)
print(df)
# duckdb.sql("CREATE SCHEMA csv_db.jaffle_shop;")