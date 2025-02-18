   
import random


for __ in range(10):
    nove_digitos = ""
    
    equacao1 = 0 
    equacao2 = 0
    multiplicador1 = 10
    multiplicador2 = 11

    for i in range(9):
        nove_digitos += str(random.randint(0,9))


    for digito in nove_digitos:
        digito_int = int(digito)
        equacao1 += digito_int * multiplicador1 
        multiplicador1-=1



    equacao1 = (equacao1 * 10) % 11


    if equacao1 > 9:
        primeiro_digito = 0


    else:
        primeiro_digito = equacao1


    nove_digitos = nove_digitos + str(primeiro_digito)

    dez_digitos = nove_digitos[:10]


    for digito in dez_digitos:
        digito_int = int(digito) 
        equacao2 += digito_int * multiplicador2
        multiplicador2 -= 1


    equacao2 = (equacao2 * 10) % 11


    if equacao2 > 9:
        segundo_digito = 0

    else:

        segundo_digito = equacao2


    cpf = nove_digitos + str(segundo_digito)
                    

    print(f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}")


    







