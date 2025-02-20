# Sistema de perguntas e respostas



perguntas = [
    {
        'pergunta': 'Qual é a capital da França?',
        'opcoes': ['Berlim', 'Madri', 'Paris', 'Roma'],
        'resposta': 'Paris',
    },

    {
        'pergunta': 'Se João tem 3 maçãs e compra mais 5, quantas maçãs ele terá no total?',
        'opcoes': ['7', '8', '9', '10'],
        'resposta': '8',
    },

    {
        'pergunta': 'Se todos os cães são mamíferos e alguns mamíferos são felinos, então podemos concluir que:',
        'opcoes': ['Todos os cães são felinos', 'Nenhum mamífero é um cão', 'Alguns mamíferos não são cães', 'Todos os mamíferos são cães'],
        'resposta': 'Alguns mamíferos não são cães',
    },
]



def imprimir_questao(i):
    pergunta = perguntas[i]['pergunta']
    print(f"Questão {i+1} de {numero_questoes}: {pergunta}")
    print()


def imprimir_opcoes(i):
    print("Opções: ")
    
    for indice,alternativa in enumerate(perguntas[i]['opcoes']):
         print(f'{indice}) {alternativa}')


def comparar_respostas(i):
    try:
        resposta_usuario = int(input("Escolha uma opção: "))
        resposta_Correta = perguntas[i]['opcoes'].index(perguntas[i]['resposta']) #Aqui eu posso utilizar o index, onde ele já verifica se a resposta correta é igual
        if resposta_usuario == resposta_Correta:                                  # a resposta nas opções e pega seu indice. Assim não precisamos fazer um For.
            print("Acertou \U0001F44D")
            print()
            return 1
            
            
        else:
            print("Errado \U0000274C")
            print()
            return 0
        
    except (ValueError, IndexError):
        print("Errado \U0000274C")
        print()
        return 0
    

    
    
numero_questoes = len(perguntas)
cont = 0
total_acertos = 0



print("RESPONDA O QUIZ!!!")
print()


while cont < numero_questoes:
    imprimir_questao(cont)
    imprimir_opcoes(cont)
    total_acertos += comparar_respostas(cont) # Aqui Aprendemos que podemos fazer multiplas funções dentro de uma variavel, como além de somar o acumulador,
    cont+=1                                   # já podemos chamar a função.
    
    
print(f"Você acertou {total_acertos} de {len(perguntas)} questões")



if total_acertos == numero_questoes:
    print("Parabéns, você acertou todas as perguntas!!!")
elif total_acertos > 0 and total_acertos <=2:
    print("Bom trabalho, continue praticanto!!!")
else:
    print("Tente novamente, não desista!!")



        




