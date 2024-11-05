class Pedido:
    def __init__(self, cliente_id, vendedor_id, forma_pagamento, status, endereco_entrega_id, data_pedido):
        self.cliente_id = cliente_id
        self.vendedor_id = vendedor_id
        self.forma_pagamento = forma_pagamento
        self.status = status
        self.endereco_entrega_id = endereco_entrega_id
        self.data_pedido = data_pedido
        self.itens = []

    def adicionar_item(self, item_pedido):
        self.itens.append(item_pedido)

    def total(self):
        return sum(item.total() for item in self.itens)

    def __str__(self):
        itens_str = "\n".join(str(item) for item in self.itens)
        return (f"Pedido:\n{itens_str}\nTotal: R$ {self.total():.2f}\n"
                f"Cliente: {self.cliente_id}\nVendedor: {self.vendedor_id}\n"
                f"Forma de Pagamento: {self.forma_pagamento}\n"
                f"Status: {self.status}\n"
                f"Endereço de Entrega ID: {self.endereco_entrega_id}\n"
                f"Data do Pedido: {self.data_pedido}")
