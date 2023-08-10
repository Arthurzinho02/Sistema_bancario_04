
class Clientes:
    def __init__ (self, nome, rg, cep):
        self.nome = nome
        self.rg = rg
        self.cep = cep
        
class conta:
    def __init__(self, saldo):
        self.saldo = saldo

class Banco_Brasil:

    def __init__(self):
        self._lista = []
        
    def adicionar_clientes(self, nome, rg, cep):
        cliente = Clientes(nome, rg, cep)
        self._lista.append(cliente)
        
    def excluir_clientes(self, ):
        self._lista.pop()
        

    def atualizar_clientes(self):
    
    def transferência(self):

    def saque(self):

    def depósito(self):

