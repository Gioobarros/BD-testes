from conexao.conexao import Conexao

def menu():
    conn = Conexao()
    if not conn.conn:
        print("Não foi possível estabelecer uma conexão com o banco.")
        return

    while True:
        print("Menu:")
        print("1 - Listar todos os pedidos de um cliente")
        print("2 - Listar todos os itens de um pedido")
        print("3 - Listar clientes que fizeram pedidos em um intervalo de datas")
        print("4 - Listar todos os pedidos e clientes")
        print("5 - Listar itens vendidos por um vendedor")
        print("6 - Sair")

        opcao = input("Escolha uma opção (1-6): ")
        
        if opcao == '1':
            cliente_id = input("ID do cliente: ")
            pedidos = conn.listar_pedidos_cliente(cliente_id)
            print(pedidos if pedidos else "Nenhum pedido encontrado.")

        elif opcao == '2':
            pedido_id = input("ID do pedido: ")
            itens = conn.listar_itens_pedido(pedido_id)
            print(itens if itens else "Nenhum item encontrado nesse pedido.")

        elif opcao == '3':
            data_inicio = input("Data de início (YYYY-MM-DD): ")
            data_fim = input("Data de fim (YYYY-MM-DD): ")
            clientes = conn.listar_clientes_por_data(data_inicio, data_fim)
            print(clientes if clientes else "Nenhum cliente encontrado entre essas datas.")

        elif opcao == '4':
            pedidos_clientes = conn.listar_pedidos_e_clientes()
            print(pedidos_clientes if pedidos_clientes else "Nenhum pedido encontrado.")

        elif opcao == '5':
            vendedor_id = input("ID do vendedor: ")
            itens_vendedor = conn.listar_itens_por_vendedor(vendedor_id)
            print(itens_vendedor if itens_vendedor else "Nenhum item encontrado para eesse vendedor.")

        elif opcao == '6':
            print("Saindo.")
            break

        else:
            print("Não há essa opção.")

if __name__ == "__main__":
    menu()
