import banco

def cadastro_venda(cliente: dict, venda: dict):
    cli = banco.recupera_cliente_documento(cliente['documento'])
    if not cli:
        banco.insere_clinte(cliente)
        venda['id_cliente'] = cliente['id']
    else:
        venda['id_cliente'] = cli[0]
    

if __name__ == "__main__":
    cli = {'nome': 'next', 'email': 'next@fiap.br', 'documento': '111' }
    ven = {'valor': 25_000, 'data': '26-10-2024'}
    cadastro_venda(cli, ven)
    print(cli)
    print(ven)