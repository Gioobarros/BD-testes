class Contato:
    def __init__(self, nome, email, telefone, data_nascimento):
        self._nome = nome
        self._email = email
        self._telefone = telefone
        self._data_nascimento = data_nascimento

    # @property
    # def id(self):
    #     return self.id
    
    # @id.setter
    # def id(self, novo_id):
    #     self.id = novo_id

    # @property
    # def nome(self):
    #     return self.nome
    
    # @nome.setter
    # def nome(self, novo_nome):
    #     self.nome = novo_nome

    # @property
    # def email(self):
    #     return self.email
    
    # @email.setter
    # def email(self, novo_email):
    #     self.email = novo_email

    # @property
    # def telefone(self):
    #     return self.telefone
    
    # @telefone.setter
    # def telefone(self, novo_telefone):
    #     self.telefone = novo_telefone 

    # @property
    # def data_nascimento(self):
    #     return self.data_nascimento
    
    # @data_nascimento.setter
    # def data_nascimento(self, novo_data_nascimento):
    #     self.data_nascimento = novo_data_nascimento

    def __str__(self):
            return f"Contato: {self.nome}, Email: {self.email}, Telefone: {self.telefone}, Data de nascimento {self.data_nascimento}"
