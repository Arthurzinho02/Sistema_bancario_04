import random
class Clientes:
    def __init__ (self, nome, rg, cep, saldo):
        self.nome = nome
        self.rg = rg
        self.cep = cep
        self.saldo = saldo

class Banco_Brasil:

    def __init__(self):
        self.dicionario = {}
        
    def adicionar_clientes(self, nome, rg, cep, saldo):
        cliente = Clientes(nome, rg, cep, saldo)
        id = random.randint(1000,5000)
        self.dicionario[id] = cliente
        print (f"{nome} adicionado, o id é {id}")
        
    def excluir_clientes(self, id):
        p = 0
        for chave, valor in self.dicionario():
            if chave == id:
                p = 1
                self.dicionario.pop(chave)
                print(f"{valor.nome} excluido")
                break
            
        if p != 1:
            print("Cliente não encontrado")

    def getnome(self, id):
        p = 0
        for chave, valor in self.dicionario():
            if chave == id:
                p = 1
                return valor.nome
        if p != 1:
            print("Cliente não encontrado")
    
    def setnome(self, id, x):
        p = 0
        for chave, valor in self.dicionario():
            if chave == id:
                p = 1
                valor.nome = x
                print(f"O nome novo é {valor.nome}")
                break
        if p != 1:
            print("Cliente não encontrado")
        
    def getrg(self, id):
        p = 0
        for chave, valor in self.dicionario():
            if chave == id:
                p = 1
                return valor.rg
        if p != 1:
            print("Cliente não encontrado")


    def setrg(self, id, x):
        p = 0
        for chave, valor in self.dicionario():
            if chave == id:
                p = 1
                valor.rg = x
                print(f"O RG novo é {valor.rg}")
                break
        if p != 1:
            print("Cliente não encontrado")

    def getcep(self, id):
        p = 0
        for chave, valor in self.dicionario():
            if chave == id:
                p = 1
                return valor.cep
        if p != 1:
            print("Cliente não encontrado")


    def setcep(self, id, x):
        p = 0
        for chave, valor in self.dicionario():
            if chave == id:
                p = 1
                valor.cep = x
                print(f"O CEP novo é {valor.cep}")
                break
        if p != 1:
            print("Cliente não encontrado")

    def getsaldo(self, id):
        p = 0
        for chave, valor in self.dicionario():
            if chave == id:
                p = 1
                return valor.saldo
        if p != 1:
            print("Cliente não encontrado")

    def depósito(self, id, x):
        p = 0
        for chave, valor in self.dicionario():
            if chave == id:
                p = 1
                valor.saldo = valor.saldo + x
                print(f"O Valor do saldo atual é de: R${valor.saldo}")
                break
        if p != 1:
            print("Cliente não encontrado")

    def saque(self,id, x):
        p = 0
        for chave, valor in self.dicionario():
            if chave == id:
                p = 1
                if valor.saldo >= 0 and x <= valor.saldo:    
                    valor.saldo = valor.saldo - x
                    print(f"O Valor do saldo atual é de: R${valor.saldo}, você sacou {x}")
                    break
                else:
                    print("Saldo insuficiente")                
        if p != 1:
            print("Cliente não encontrado")
        
    def transferencia(self, id, id_t , x):
        p = 0
        for chave, valor in self.dicionario():
            if chave == id:
                p = 1
                if valor.saldo >= 0 and x <= valor.saldo:    
                    valor.saldo = valor.saldo - x
                    q = 0
                    for chave, valor in self.dicionario():
                        if chave == id_t:
                            q = 1
                            valor.saldo = valor.saldo + x
                            print("O valor foi transferido")
                    if q != 1:
                        valor.saldo = valor.saldo + x
                        print("cliente não encontrado")
                else:
                    print("Saldo insuficiente")      
        if p != 1:
            print("Cliente não encontrado")  


    


    



