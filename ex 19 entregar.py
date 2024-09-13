def contar_vogais(texto):
   
    vogais = 'aeiouAEIOU'
    
    contador = 0
    
    for caractere in texto:
        if caractere in vogais:
            contador += 1
    
    return contador

frase = input("Digite uma frase para contar o número de vogais: ")

numeroVogais = contar_vogais(frase)

print("O número de vogais na frase é:",numeroVogais)

