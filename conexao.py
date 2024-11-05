import psycopg2

class Conexao:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                dbname="loja_virtual",
                user="postgres",
                password="postgres",
                host="localhost",
                port="5432"
            )
            print("Conexão bem-sucedida.")
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            self.conn = None

    def executar_consulta(self, query, params=None):
        if not self.conn:
            print("Conexão não estabelecida.")
            return None
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(query, params)
                return cursor.fetchall()
        except Exception as e:
            print(f"Erro ao executar consulta: {e}")
            return None

    def listar_pedidos_cliente(self, cliente_id):
        query = "SELECT * FROM pedidos WHERE cliente_id = %s"
        return self.executar_consulta(query, (cliente_id,))

    def listar_itens_pedido(self, pedido_id):
        query = """
            SELECT itens.nome, itens_pedido.quantidade, itens_pedido.preco_unitario
            FROM itens_pedido
            JOIN itens ON itens.id = itens_pedido.item_id
            WHERE pedido_id = %s
        """
        return self.executar_consulta(query, (pedido_id,))

    def listar_clientes_por_data(self, data_inicio, data_fim):
        query = """
            SELECT DISTINCT clientes.id, clientes.nome, clientes.email
            FROM pedidos
            JOIN clientes ON clientes.id = pedidos.cliente_id
            WHERE data_pedido BETWEEN %s AND %s
        """
        return self.executar_consulta(query, (data_inicio, data_fim))

    def listar_pedidos_e_clientes(self):
        query = """
            SELECT pedidos.id, clientes.nome, pedidos.data_pedido, pedidos.status
            FROM pedidos
            JOIN clientes ON clientes.id = pedidos.cliente_id
        """
        return self.executar_consulta(query)

    def listar_itens_por_vendedor(self, vendedor_id):
        query = """
            SELECT itens.nome, itens_pedido.quantidade, pedidos.data_pedido
            FROM itens_pedido
            JOIN pedidos ON pedidos.id = itens_pedido.pedido_id
            JOIN itens ON itens.id = itens_pedido.item_id
            WHERE pedidos.vendedor_id = %s
        """
        return self.executar_consulta(query, (vendedor_id,))
