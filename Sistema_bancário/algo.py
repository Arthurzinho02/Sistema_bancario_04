from classes import *
import os

def Main():
    banco = Banco_Brasil()
    while True:
        try:
            print("Você está no banco do Brasil!")
            print("Vocé é:")
            print("1. Cliente\n2. Administrador")
            opção = int(input("Qual valor deseja? > "))
            os.system("cls")

            match opção:
                case 1:
                    print("Esse é o Menu destinado aos Clientes")
                    print("1. Transferência\n2. Saque\n3. Depósito")
                    função = input("O que você deseja fazer? ")
                    os.system("cls")

                    if função == "1":
                        print("Essa é a área de TRANSFERÊNCIA")
                        destinatário = int(input("Digite o nome do destinário que você deseja enviar o valor: "))
                        valor = float(input("Digite o valor que deseja transferir: "))
                        banco.transferencia(destinatário, valor)
                    
                    elif função == "2":
                        print("Essa é a área de SAQUE")
                        valor = float(input("Digite o valor que deseja sacar: "))
                        banco.saque(valor)
                    
                    elif função == "3":
                        print("Essa é a área de DEPÓSITO")
                        valor = float(input("Digite o valor que deseja depositar: "))
                        banco.depósito(valor)

                    else:
                        print("A opção não existe")
                        os.system("cls")

                case 2:
                    print("Esse é o Menu destinado ao Administrador")
                    print("1. Criar conta\n2. Excluir conta\n3. Atualizar dados")
                    função = input("O que você deseja fazer? ")
                    os.system("cls")

                    if função == "1":
                        print("Essa é a área de CRIAR CONTA")
                        nome = input("Nome do usuário: ")
                        rg = int(input("RG: "))
                        cep = int(input("CEP: "))
                        saldo = 0
                        banco.adicionar_clientes(nome, rg, cep, saldo)
                    
                    elif função == "2":
                        print("Essa é a área de EXCLUIR CONTA")
                        conta = int(input("Qual conta você deseja excluir? "))
                        banco.excluir_clientes(conta)
                    
                    elif função == "3":
                        print("Essa é a área de ATUALIZAR DADOS")
                        conta = input("Qual conta você deseja atualizar? ")
                        banco.atualizar(conta)

                    else:
                        print("A opção não existe")
                        os.system("cls")
                case 3:

                    print("Essa é a área de ATUALIZAR DADOS\nO que você deseja atualizar?\n 1 - nome\n2 - RG\n3 - cep")
                    função = input("Digite o que será realizado: ")

                    if função == "1":
                        input("Digite o nome do cliente")
                        banco.atualizar(conta)

                    elif função == "2":
                        input("Digite o RG")
                        banco.atualizar(conta)

                    elif função == "3":
                        input("Digite o cep")
                        banco.atualizar(conta)


                    else:
                        print("A opção não existe")
                        os.system("cls")

                case _:
                    print("Opção Invalida")

        except Exception as erro:
            print("Valor invalido")
            print(erro.__class__.__name__)
            