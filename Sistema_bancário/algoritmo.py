from classes import *

def main ():
    while True:
        try:
            print("Você está no banco tal, para entrar na sua conta, digite sue nome: ")
            nome = input("Digite seu nome aqui:")
            


        except Exception as erro: # Vai captar qualquer erro ou qualquer anormalidade
		print("Um erro foi detectado. Modifique para que seu software funcione corretamente")
		print(erro.__class.__name)
