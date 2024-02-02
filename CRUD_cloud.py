import streamlit as st
import psycopg2
st.title("Hello")
connection_string = st.secrets.db_credentials.DATABASE_URL
# print(st.secrets.db_credentials.db_url)
connection = psycopg2.connect(connection_string)
cursor = connection.cursor()
create_table = "CREATE TABLE IF NOT EXISTS farmer(id int PRIMARY KEY, name varchar(20));"
cursor.execute(create_table)
connection.commit()

# insert_query = "INSERT INTO farmer (id, name) VALUES (%s, %s);"
# val = (1, "John Doe")
# cursor.execute(insert_query,val)
# connection.commit()

select_query = "SELECT * FROM farmer;"
cursor.execute(select_query)

rows = cursor.fetchall()
for row in rows:
    st.write(row)
print("Success")
