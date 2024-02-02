import streamlit as st
import psycopg2

st.title("Hello")
connection_string = st.secrets.db_credentials.DATABASE_URL
connection = psycopg2.connect(connection_string, sslmode='verify-full', sslrootcert='/path/to/root.crt')

cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS farmer(id int PRIMARY KEY, name varchar(20));"
cursor.execute(create_table)
connection.commit()

select_query = "SELECT * FROM farmer;"
cursor.execute(select_query)

rows = cursor.fetchall()
for row in rows:
    st.write(row)

print("Success")

