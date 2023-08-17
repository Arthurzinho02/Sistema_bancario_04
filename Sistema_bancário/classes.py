
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
        self.dicionario = {}
        
    def adicionar_clientes(self, nome, rg, cep, saldo):
        cliente = Clientes(nome, rg, cep)
        self.dicionario[cliente] = saldo
        
    def excluir_clientes(self, nome):
        p = 0
        for cliente in self.dicionario:
            if cliente.nome == nome:
                p = 1
                self.dicionario.pop(cliente)
                break
            
        if p != 1:
            print("Cliente não encontrado")

    def getnome(self, nome):
        for cliente in self.dicionario:
            if cliente.nome == nome:
                cliente
    
    def setnome(self,nome):
        
        
    


    

