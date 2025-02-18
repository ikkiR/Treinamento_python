
import os

os.system('cls')



def multiplicacao (*args):
    valor = 1
    for num in args:
        if num == 0:
            ...
        else:
            valor *= num
    
    return valor
        

def entrada(mensagem):

    while True:
        try:
            msg = int(input(mensagem))
            return msg
        except ValueError:
            print("Por favor insira um número inteiro.")
            

saida = "S"
list_conta = []

while True:
    if saida == "S":   
        numeros = entrada("Insira um número inteiro para a multiplicação: ")
        list_conta.append(numeros)
        saida = input("Deseja inserir mais algum número? [S]sim [N]não: ").upper()
    elif saida == "N":
        break
    else:
        saida = input("Deseja inserir mais algum número? [S]sim [N]não: ").upper()



print(multiplicacao(*list_conta))

print(3*8*65*62)

    


