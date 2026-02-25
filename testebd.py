import psycopg2

conn = psycopg2.connect(
    host="127.0.0.1",
    port=5432,
    dbname="testdb",
    user="postgres",
    password="Eric1234/"
)

print("Conectado com sucesso")
conn.close()