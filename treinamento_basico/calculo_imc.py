print("#################################################### CALCULO DE IMC #####################################################")

try:

    altura = float(input("Digite a sua altura (em metros): "))
    peso = float(input("Digite o seu peso (em kg): "))

    if peso<= 0 or altura <= 0:
        print("Insira um valor maior que zero")

    else:
        imc = peso / (altura ** 2)

        if imc <= 18.5:
            print(f"Seu imc é: {imc:.2f}. você está abaixo do peso")

        elif imc >= 18.6 and imc <= 24.9:
            print(f"Seu imc é {imc:.2f}. você está com o peso normtal")
        
        elif imc >= 25 and imc <= 29.9:
            print(f"seu imc é {imc:.2f}. você está acima do peso")
        
        elif imc >= 30 and imc <= 34.9:
            print(f"seu imc é {imc:.2f}. obesidade de grau 1")

        elif imc >= 35 and imc <= 39.9:
            print(f"seu imc é {imc:.2f}. obesidade de grau 2")
        
        else:
            print(f"seu imc é {imc:.2f}. obesidade de grau 3")

except ValueError:
    print("Por favor insira um valor valido")
    
