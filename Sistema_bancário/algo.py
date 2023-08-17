from classes import *
import os

def Main():
    while True:
        try:
            print("Você está no banco do Brasil")
            print("Vocé é")
            print("1. Cliente\n 2. Administrador")
            opção = int(input("Qual valor deseja? > "))

            match opção:
                case 1:
                    print("Esse é o Menu destinado aos Clientes'")
                    print("1. Transferência\n 2. Saque\n 3. Depósito")
                    função = input("O que você deseja fazer? ")

                    if função == 1:
                        print("Essa é a área de TRANSFERÊNCIA")
                        branco = Banco_Brasil()
                        destinatário = input("Digite o nome do destinário que você deseja enviar o valor: ")
                        branco.

                case 2:
                    menu_adm = Circulo(int(input("Informe o raio > ")))
                    print(cir.calc_circo())
                case 3:
                    para = Paralelepipedo(int(input("Informe o Comprimento > ")), int(input("Informe a Largura > ")), int(input("Informe a Altura > ")))
                    print(para.calc_volume())
                case 0:
                    print("Saindo do software")
                    break
                case _:
                    print("Opção Invalida")  
        except Exception as erro:
            print("Valor invalido")
            print(erro.__class__.__name__)