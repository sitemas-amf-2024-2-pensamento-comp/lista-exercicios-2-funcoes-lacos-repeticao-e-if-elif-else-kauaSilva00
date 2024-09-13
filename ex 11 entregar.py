import random

numero_sorteado = random.randint(1, 100)

while True:
   
    tentativa = int(input("Tente adivinhar o número (entre 1 e 100): "))

    if tentativa < numero_sorteado:
        print("O número sorteado é maior. Tente novamente.")
    elif tentativa > numero_sorteado:
        print("O número sorteado é menor. Tente novamente.")
    else:
        print("Parabéns! Você acertou o número.")
        break 