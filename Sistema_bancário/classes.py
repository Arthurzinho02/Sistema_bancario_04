class Clientes:
    def __init__ (self, nome, rg, cep, saldo=0):
        self.nome = nome
        self.rg = rg
        self.cep = cep
        self.saldo = saldo

    def getSaldo(self):
        return self.saldo
    
    def setSaldo(self, x):
        self.saldo = x
     
    def getNome(self):
        return self.nome
    
    def setNome(self, x):
        self.nome = x
    
    def getCep(self):
        return self.cep
    
    def setCep(self, x):
        self.cep = x
    
    def getRg(self):
        return self.rg
    
    def setRg(self, x):
        self.rg = x
    

class Banco_Brasil:

    def __init__(self):
        self.dicionario = {}
        self.ADM = ADM("MASTER", 123)
        self.listaAdm = [self.ADM]
        

    def listarAdms(self):
        cont = 0
        for i in self.listaAdm:
            cont += 1
            print(f"{cont}- Nome: {i.getNomeA()}")
    
    def excluiradms(self, vetor):
        self.listaAdm.pop(vetor - 1)

    def adicionarAdm(self, nome, senha):
        adm = ADM(nome, senha)
        self.listaAdm.append(adm)

    def LoginAdm(self, nome, senha):
        for i in self.listaAdm:
            if i.getNomeA() == nome and i.getSenhaA() == senha:
                return 1          
        

    def loginCliente(self, id, nome):
        for chave, valor in self.dicionario.items():
            if chave == id and valor.getNome() == nome:
                return 1
        
    def getCliente(self, id):
        for chave, valor in self.dicionario.items():
            if chave == id:
                valor.getSaldo()


    def adicionar_clientes(self, nome, rg, cep, id):
        saldo = 0
        cliente = Clientes(nome, rg, cep, saldo)
        self.dicionario[id] = cliente
        print (f"{nome} adicionado, o id é {id}")


    def listarClientes(self):
        cont = 0
        for chave, valor in self.dicionario.items():
            cont += 1
            print(f"{cont}- Nome: {valor.getNome()} | Id: {chave} | RG: {valor.getRg()} | CEP: {valor.getCep()} ")
        
    def excluir_clientes(self, id):
        p = 0
        for chave, valor in self.dicionario.items():
            if chave == id:
                p = 1
                print(f"{valor.getNome()} excluido")
                self.dicionario.pop(chave)
                break            
        if p != 1:
            print("Cliente não encontrado")

    def getnome(self, id):
        p = 0
        for chave, valor in self.dicionario.items():
            if chave == id:
                p = 1
                return valor.getNome()
        if p != 1:
            print("Cliente não encontrado")
    
    def setnome(self, id, x):
        p = 0
        for chave, valor in self.dicionario.items():
            if chave == id:
                p = 1
                valor.setNome(x)
                print(f"O nome novo é {valor.getNome()}")
                break
        if p != 1:
            print("Cliente não encontrado")
        
    def getrg(self, id):
        p = 0
        for chave, valor in self.dicionario.items():
            if chave == id:
                p = 1
                return valor.getRg()
        if p != 1:
            print("Cliente não encontrado")


    def setrg(self, id, x):
        p = 0
        for chave, valor in self.dicionario.items():
            if chave == id:
                p = 1
                valor.setRg(x)
                print(f"O RG novo é {valor.getRg()}")
                break
        if p != 1:
            print("Cliente não encontrado")

    def getcep(self, id):
        p = 0
        for chave, valor in self.dicionario.items():
            if chave == id:
                p = 1
                return valor.getCep()
        if p != 1:
            print("Cliente não encontrado")


    def setcep(self, id, x):
        p = 0
        for chave, valor in self.dicionario.items():
            if chave == id:
                p = 1
                valor.setCep(x)
                print(f"O CEP novo é {valor.getCep()}")
                break
        if p != 1:
            print("Cliente não encontrado")

    def getsaldo(self, id):
        p = 0
        for chave, valor in self.dicionario.items():
            if chave == id:
                p = 1
                return valor.getSaldo()
        if p != 1:
            print("Cliente não encontrado")

    def depósito(self, id, x):
        p = 0
        for chave, valor in self.dicionario.items():
            if chave == id:
                p = 1
                x = valor.getSaldo() + x
                valor.setSaldo(x)
                print(f"O Valor do saldo atual é de: R${valor.getSaldo()}")
                break
        if p != 1:
            print("Cliente não encontrado")

    def saque(self,id, x):
        p = 0
        for chave, valor in self.dicionario.items():
            if chave == id:
                p = 1
                if valor.getSaldo() >= 0 and x <= valor.getSaldo():    
                    x1 = valor.getSaldo() - x
                    valor.setSaldo(x1)
                    print(f"O Valor do saldo atual é de: R${valor.getSaldo()}, você sacou {x}")
                    break
                else:
                    print("Saldo insuficiente")                
        if p != 1:
            print("Cliente não encontrado")
        
    def transferencia(self, id, id_t , x):
        p = 0
        for chave, valor in self.dicionario.items():
            if chave == id:
                p = 1
                if valor.getSaldo() >= 0 and x <= valor.getSaldo():    
                    x1 = valor.getSaldo() - x
                    valor.setSaldo(x1)
                    q = 0
                    for chave, valor in self.dicionario.items():
                        if chave == id_t:
                            q = 1
                            x1 = valor.getSaldo() + x
                            valor.setSaldo(x1)
                            print("O valor foi transferido")
                    if q != 1:
                        x1 = valor.getSaldo + x
                        valor.setSaldo(x1)
                        print("cliente não encontrado")
                else:
                    print("Saldo insuficiente")      
        if p != 1:
            print("Cliente não encontrado")  

class ADM:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

    def getNomeA(self):
        return self.nome
    
    def getSenhaA(self):
        return self.senha


    


    



