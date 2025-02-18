import sys


try:

    cpf_usuario = input("Insira o seu cpf: ")
    cpf_usuario = cpf_usuario.replace(".", "").replace("-", "")

    cpf_e_sequencial = cpf_usuario == cpf_usuario[0] * len(cpf_usuario)


    if cpf_e_sequencial:
        sys.exit()

    else:
         
        if len(cpf_usuario) == 11:
        
            Nove_Digitos_Formatados =  cpf_usuario[:9]

            multiplicador1 = 10

            equacao1 = 0
        

            for digito in Nove_Digitos_Formatados:
                digito_int = int(digito)
                equacao1 += digito_int * multiplicador1 
                multiplicador1-=1



            equacao1 = (equacao1 * 10) % 11


            if equacao1 > 9:
                primeiro_digito = 0


            else:
                primeiro_digito = equacao1


            Verificador_cpf = Nove_Digitos_Formatados + str(primeiro_digito)

            dez_digitos_formatados = Verificador_cpf[:10]

            multiplicador2 = 11

            equacao2 = 0


            for digito in dez_digitos_formatados:
                digito_int = int(digito) 
                equacao2 += digito_int * multiplicador2
                multiplicador2 -= 1


            equacao2 = (equacao2 * 10) % 11


            if equacao2 > 9:
                segundo_digito = 0

            else:

                segundo_digito = equacao2


            Verificador_cpf = dez_digitos_formatados + str(segundo_digito)
                

            # print(f"Seu CPF é {Verificador_cpf[:3]}.{Verificador_cpf[3:6]}.{Verificador_cpf[6:9]}-{Verificador_cpf[9:11]}")


            if Verificador_cpf == cpf_usuario:
                print("O seu CPF é valido")

            else:
                print("CPF inválido")


        else:
            print("Por favor insira todos os número do seu CPF")



except:

    print("Insira um CPF valido")






