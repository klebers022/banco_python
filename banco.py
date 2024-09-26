import oracledb


def get_conexao():
    return oracledb.connect(user='rm557887', password='210106',
                            dsn='oracle.fiap.com.br/orcl')
def recupera_cliente_documento(doc:str):
    sql = '''select id, nome, email, documento from t_cliente
                where documento=:doc'''
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, {'doc': doc})
            return cur.fetchone()

def insere_clinte(cli: dict):
    sql = '''insert into t_cliente(nome, email, documento)
            values(:nome, :email, :documento) returning id into :id'''
    with get_conexao() as con:
        with con.cursor() as cur:

            novo_id = cur.var(oracledb.NUMBER)
            cli['id'] = novo_id
            cur.execute(sql, cli)
            cli['id'] = novo_id.getvalue()
        con.commit()

if __name__ == "__main__":
    cliente = {'nome': 'FIAP', 'email': 'compras@fiap.com',
               'documento': '56.771.568-86'}
    insere_clinte(cliente)
    print(cliente)