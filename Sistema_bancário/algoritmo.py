from classes import *
import os 

def main ():
    while True:
            try:
               print("Você está no banco tal, você é: \n1 - cliente\n2 - admiistrador ")
               
               def menu_p():
                    input("Digite uma das opções acima: ")

                    if menu_p == 1:
                         print("Você entrou em clientes, entre na sua conta: ")
                         os.system("pause")
                         os.system("cls")

                    elif menu_p == 2:
                         print("você entrou em administrador, oq que deseja fazer?")
                         os.system("pause")
                         os.system("cls")

               print ("Você entrou na opção cliente, o que deseja realizar? \n1 - Transferência entre clientes\n2 - Saque\n3 - Depósito ")
               
               def menu_c():
                    input ("Digite o que precisa ser realizado: ")

                    if menu_c == 1:
                         print ("Você entrou em Tranferência entre clientes, digite qual valor será transferido: ")
                         os.system("pause")

                    elif menu_c == 2:
                         print ("Você está em Saque, digite o valor que deseja retirar: ")
                         os.system("pause")

                    elif menu_c == 3:
                         print("Você entrou em Depósitos, digite a quantia que deseja depositar: ")
                    
                    elif menu_c == 4:
                         print("Saindo do programa.")
                         break
     


          
                 
          



        # except Exception as erro: # Vai captar qualquer erro ou qualquer anormalidade
		# print("Um erro foi detectado. Modifique para que seu software funcione corretamente")
		# print(erro.__class.__name)
