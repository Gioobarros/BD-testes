class Cliente:
    def __init__(self, nome, email, telefone, data_cadastro):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.data_cadastro = data_cadastro

    def __str__(self):
            return f"Cliente: {self.nome}, Email: {self.email}, Telefone: {self.telefone}, Data de cadastro {self.data_cadastro}"
