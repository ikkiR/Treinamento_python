print("Descubra se o número é impar ou par!!")

numero = input("Inclua um número: ")
numero = int(numero)

if numero % 2 == 0:
    print(f"{numero} é um número par")
else:
    print(f"{numero} é um número impar")

