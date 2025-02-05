import os
from calculator import Calculadora

#função que define as opções disponíveis

def titulo():
    print("\t\t\t\tPYTHONLATOR 5000\n\n")
def options():
    titulo()
    print("1-Soma\n2-subtracao\n3-Multiplicação\n4-Divisão\n5-Sair")
    option_choice()
#função que recebe a escolha de ação do usuário
def option_choice():
   while True:
        choice = input("Escolha a opção desejada: ")
    
        #se a opção escolhida for 1
        if (choice == "1"):
                os.system("cls")
                soma()
                break
        #se a opção escolhida for 2
        elif (choice == "2"):
                os.system("cls")
                subtracao()
                break
        #se a opção escolhida for 3
        elif (choice == "3"):
                os.system("cls")
                multiplicacao()
                break
        #se a opção escolhida for 4
        elif (choice == "4"):
                os.system("cls")
                divisao()
                break
        #se a opção escolhida for 5
        elif (choice == "5"):
            os.system("cls")
            exit()
        #se nenhuma das opções forem escolhidas
        else:
            input("Opção escolhida inválida!\nCertifique-se de digitar apenas um dos valores numéricos disponíveis.\nPressione qualquer tecla para tentar novamente.")
            os.system("cls")
            return options()
       
#retornando
def final_choice():
    escolha = input("\nDeseja retornar ao menu de opções?\n1-Sim\n2-Não\n")
    if escolha == "1":
        return main()
    elif escolha == "2":
        exit()
    else:
        input("Opção inválida! Tente novamente.")
        return final_choice()
    
#escolhendo os valores
def value():
    os.system("cls")
    titulo()
    
    while True:
        
        try:
            num1 = float(input("Digite o primeiro valor: "))
            num2 = float(input("Digite o segundo valor: "))
            break
        
        except ValueError:
            input("Valores inválidos! Por favor, insire apenas números.\nAperte qualquer tecla para tentar novamente")
            os.system("cls")
            
    
    global sm 
    sm = Calculadora(num1,num2)
#soma
def soma():
    value()
    resultado = sm.soma()
    print(f"O resultado é: {resultado}")
    final_choice()
    
#subtração
def subtracao():
    value()
    resultado = sm.subtracao()
    print(f"O resultado é: {resultado}")
    final_choice()
#multiplicação
def multiplicacao():
    value()
    resultado = sm.multiplicacao()
    print(f"O resultado é: {resultado}")
    final_choice()
#divisão
def divisao():
    value()
    resultado = sm.divisao()
    print(f"O resultado é: {resultado}")
    final_choice()
#função principal
def main():
    os.system("cls")
    options()

if __name__ == "__main__":
    main()