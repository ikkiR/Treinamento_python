vogais = ["a","e","i","o","u","A","E","I","O","U"]

frase = input("Escreva uma frase para verificar as vogais: ")



letras_encontradas = 0

for letra in frase:
    if letra in vogais:
        letras_encontradas+=1
    
    
print(letras_encontradas)