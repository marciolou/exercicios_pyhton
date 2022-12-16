SECRET_KEY = 'today'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
    SGBD = 'postgresql',
    usuario = "marcio",
    senha = "031060@Ma",
    servidor = "localhost",
    database = "postgres"
)