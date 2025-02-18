
try:
    continuar = True

    while continuar: 
        tabuada = int(input("insira um número e veja a tabuada dele: "))
        cont = 0

        if tabuada <0 :
            print("Insira um número positivo.")

        else:
            print(f"\ntabuada do {tabuada}\n")
            while cont <=10 :
                resultado = tabuada * cont
                print(f"{tabuada} X {cont} = {resultado}")
                cont+= 1 
            
            saida = ""


            while saida != "S" and saida != "N":

                saida = input("\ndeseja encerrar o programa? [S]sim [N]não: ")

                if saida.upper() == "N":
                    break 

                elif saida.upper() == "S":
                    continuar = False
                    break

                else: 
                    print("Insira uma opção valida")

except:
    print("insira um número válido")




    