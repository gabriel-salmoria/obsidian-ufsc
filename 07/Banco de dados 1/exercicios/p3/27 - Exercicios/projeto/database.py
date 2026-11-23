import psycopg2


def conectar():
    conexao = psycopg2.connect(
        host="localhost",
        database="cadastro_db",
        user="postgres",
        password="liic08"
    )

    return conexao