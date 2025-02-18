print("##################################### Descubra se uma palavra é um palindromo ############################\n")

palavra = input("Digite uma palavra: ").strip().lower()


if palavra == palavra[::-1]:
    print(f"{palavra} é um palindromo!")

else:
    print(f"{palavra} não é um palindromo!")
    