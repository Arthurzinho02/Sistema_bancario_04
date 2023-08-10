
class Clientes:
    def __init__ (self, nome, rg, cep, saldo):
        self.nome = nome
        self.rg = rg
        self.cep = cep
        self.saldo = saldo

    # def transferência(self):

    # def saque(self):

    # def depósito(self):

    

class Banco_Brasil:

    def __init__(self):
        self._lista = []
        
    def adicionar_clientes(self, nome, rg, cep, saldo):
        cliente = Clientes(nome, rg, cep)
        self._lista.append(cliente)
        
    def excluir_clientes(self, nome):
        for cliente in self._lista:
            if cliente.nome == nome:
                self._lista.pop(cliente)
                break
        

            


        

    # def atualizar_clientes(self):
    

