import psycopg2

try:
    conn =psycopg2.connect(host = 'localhost',
    port = '5433',
    database = 'postgres',
    user = 'marcio',
    password = '031060@Ma')
    print('Você está conectado...')

except Exception:
    print('Você está sem conexão...')

if conn is not None:
    
    print('Sua Conexao está estabilizada!')

    cursor = conn.cursor()
    
    cursor.execute('CREATE TABLE  jogos (id serial, nome VARCHAR(15)NOT NULL, categoria VARCHAR(15)NOT NULL, console varchar(15) NOT NULL, PRIMARY KEY(id));')
    print('Sua tabela jogos foi criada!')

    cursor.execute('CREATE TABLE usuarios  (nome VARCHAR(15) NOT NULL, nickname VARCHAR(30)NOT NULL, senha VARCHAR(30)NOT NULL,  PRIMARY KEY(nickname) );')
    print('Sua tabela usuario foi criada!')

    conn.commit()
    cursor.close()
    conn.close()
