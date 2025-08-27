# Substitua psycopg2 por pg8000
import pg8000

# Mesma funcionalidade, sem dependências C
conn = pg8000.connect(
    host="seu_host", port=5432, database="seu_db", user="usuario", password="senha"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM tabela")
rows = cursor.fetchall()
