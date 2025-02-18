def soma(x,y):
    
    return x + y


def entrada(mensagem):
    while True:
        
        try:
            return int(input(mensagem))
        except ValueError:
            print("por favor insira um número inteiro!")



valor1 = entrada("Insira um valor para soma: ")
valor2 = entrada("Insira outro valor para soma: ")

print(soma(valor1,valor2))





