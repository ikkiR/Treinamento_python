print("###################################### Calculo fatorial ##########################\n")


try:
    numero = int(input("Insira um número inteiro: "))

    if numero <= 0:
        print("Não é possivel calcular o fatorial de um número negativo")

    else:
        fatorial = 1
        lista_num = []

        for i in range(numero,0,-1):
            fatorial*= i
            lista_num.append(i)

        resultado = " x ".join(map(str,lista_num))

        print(f"{fatorial} ({numero}! = {resultado})")

except ValueError:
    print("Por favor insira um número inteiro")
    










