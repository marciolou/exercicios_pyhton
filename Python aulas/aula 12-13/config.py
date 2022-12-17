SECRET_KEY = 'today'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
    SGBD = 'postgresql',
    usuario = "marcio",
    senha = "031060",
    servidor = "localhost:5433",
    database = "postgres"
)