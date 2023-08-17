
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
        print (f"{nome} adicionado")
        
    def excluir_clientes(self, nome):
        p = 0
        for cliente in self.dicionario:
            if cliente.nome == nome:
                p = 1
                self.dicionario.pop(cliente)
                print(f"{cliente.nome} excluido")
                break
            
        if p != 1:
            print("Cliente não encontrado")

    def getnome(self, nome):
        p = 0
        for cliente in self.dicionario:
            if cliente.nome == nome:
                p = 1
                return cliente.nome
        if p != 1:
            print("Cliente não encontrado")
    
    def setnome(self,nome, x):
        p = 0
        for cliente in self.dicionario:
            if cliente.nome == nome:
                p = 1
                cliente.nome = x
                print(f"O nome novo é {cliente.nome}")
                break
        if p != 1:
            print("Cliente não encontrado")
        
    def getrg(self, rg):
        p = 0
        for cliente in self.dicionario:
            if cliente.rg == rg:
                p = 1
                return cliente.rg
        if p != 1:
            print("Cliente não encontrado")


    def setrg(self, rg, x):
        p = 0
        for cliente in self.dicionario:
            if cliente.rg == rg:
                p = 1
                cliente.rg = x
                print(f"O RG novo é {cliente.rg}")
                break
        if p != 1:
            print("Cliente não encontrado")

    def getcep(self, cep):
        p = 0
        for cliente in self.dicionario:
            if cliente.cep == cep:
                p = 1
                return cliente.cep
        if p != 1:
            print("Cliente não encontrado")


    def setcep(self, cep, x):
        p = 0
        for cliente in self.dicionario:
            if cliente.cep == cep:
                p = 1
                cliente.cep = x
                print(f"O CEP novo é {cliente.cep}")
                break
        if p != 1:
            print("Cliente não encontrado")
