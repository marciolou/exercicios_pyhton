import psycopg2

try:
    conn = psycopg2.connect(host = "localhost", port = "5433", database = "postgres", user = "marcio", password = "031060@Ma")
    print('Você está conectado!')
except:
    print('Você não se conectou')

if conn == None:
    print('Sua conexão está estável')

cursor = conn.cursor()

cursor.execute("CREATE TABLE teste(id serial PRIMARY KEY, nome VARCHAR(15), sobrenome VARCHAR(15));")

print('Tabela Criada')
conn.commit()
cursor.close()
conn.close()
