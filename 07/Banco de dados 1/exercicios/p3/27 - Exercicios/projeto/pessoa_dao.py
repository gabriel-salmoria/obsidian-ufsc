from database import conectar


def cadastrar_pessoa(nome, idade, email, profissao_id):
    """
    Cadastra uma pessoa na tabela pessoa
    e depois cria o relacionamento dela com uma profissão
    na tabela pessoa_profissao.
    """

    conexao = conectar()
    cursor = conexao.cursor()

    try:
        # 1. Insere a pessoa na tabela pessoa
        cursor.execute("""
            INSERT INTO pessoa (nome, idade, email)
            VALUES (%s, %s, %s)
            RETURNING id;
        """, (nome, idade, email))

        pessoa_id = cursor.fetchone()[0]

        # 2. Insere o relacionamento na tabela pessoa_profissao
        cursor.execute("""
            INSERT INTO pessoa_profissao (pessoa_id, profissao_id)
            VALUES (%s, %s);
        """, (pessoa_id, profissao_id))

        conexao.commit()

    except Exception as erro:
        conexao.rollback()
        raise erro

    finally:
        cursor.close()
        conexao.close()


def listar_pessoas():
    """
    Lista as pessoas cadastradas junto com suas profissões.
    Usa JOIN para juntar dados de várias tabelas.
    """

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT 
            p.id,
            p.nome,
            p.idade,
            p.email,
            pr.nome AS profissao
        FROM pessoa p
        JOIN pessoa_profissao pp 
            ON p.id = pp.pessoa_id
        JOIN profissao pr 
            ON pr.id = pp.profissao_id
        ORDER BY p.id;
    """)

    pessoas = cursor.fetchall()

    cursor.close()
    conexao.close()

    return pessoas