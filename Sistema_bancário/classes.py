
class Clientes:
    def __init__ (self, nome, rg, cep):
        self.nome = nome
        self.rg = rg
        self.cep = cep

class Banco_Brasil:

    def __init__(self):
        self.lista = []
        
    def adicionar_clientes(self, nome, rg, cep):
        cliente = Clientes(nome, rg, cep)
        self.lista.append(cliente)

    def excluir_clientes(self):


    def atualizar_clientes(self):
    
    def transferência(self):

    def saque(self):

    def depósito(self):
