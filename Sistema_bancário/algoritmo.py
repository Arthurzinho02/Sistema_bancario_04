from classes import *
import os 

def main ():
    while True:
        try:
            print("Você está no banco tal, você é: \n1 - cliente\n2 - admiistrador ")
            menu = input("Digite uma das opções acima: ")

            if menu == 1:
                 print("Você entrou em clientes, entre na sua conta: ")
                 os.system("pause")
                 os.system("cls")

            elif menu == 2:
                 print("você entrou em administrador, oq que deseja fazer?")
                 os.system("pause")
                 os.system("cls")
            



        except Exception as erro: # Vai captar qualquer erro ou qualquer anormalidade
		print("Um erro foi detectado. Modifique para que seu software funcione corretamente")
		print(erro.__class.__name)
