
class Endereco:
    def __init__(self, rua, cidade, estado, cep, cliente_id):
        self.rua = rua
        self.cliente_id = cliente_id
        self.cidade = cidade
        self.estado = estado
        self.cep = cep

    def __str__(self):
        return f"{self.rua} - {self.cidade}/{self.estado}, CEP: {self.cep}, Cliente ID= {self.cliente_id}"
