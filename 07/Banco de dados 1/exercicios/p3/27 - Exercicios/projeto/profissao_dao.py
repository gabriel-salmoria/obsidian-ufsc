from database import conectar


def listar_profissoes():
    """
    Busca todas as profissões cadastradas no banco.
    Retorna uma lista de tuplas no formato:
    [(1, 'Professor'), (2, 'Programador'), ...]
    """

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, nome
        FROM profissao
        ORDER BY nome;
    """)

    profissoes = cursor.fetchall()

    cursor.close()
    conexao.close()

    return profissoes