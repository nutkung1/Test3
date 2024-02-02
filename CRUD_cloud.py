import streamlit as st
import psycopg2
from psycopg2 import sql

st.title("Hello")

# Get the database URL from Streamlit secrets
connection_string = st.secrets.db_credentials.DATABASE_URL

# Connect to the database
connection = psycopg2.connect(connection_string, sslmode='verify-ca', sslrootcert='path/to/root.crt')
cursor = connection.cursor()

# Create the 'farmer' table if it doesn't exist
create_table_query = sql.SQL("CREATE TABLE IF NOT EXISTS farmer (id SERIAL PRIMARY KEY, name VARCHAR(20));")
cursor.execute(create_table_query)
connection.commit()

# Insert a sample record into the 'farmer' table
insert_query = sql.SQL("INSERT INTO farmer (name) VALUES (%s) RETURNING id;")
cursor.execute(insert_query, ('John Doe',))
connection.commit()

# Retrieve and display all records from the 'farmer' table
select_query = sql.SQL("SELECT * FROM farmer;")
cursor.execute(select_query)
rows = cursor.fetchall()

for row in rows:
    st.write(row)

# Close the database connection
cursor.close()
connection.close()

