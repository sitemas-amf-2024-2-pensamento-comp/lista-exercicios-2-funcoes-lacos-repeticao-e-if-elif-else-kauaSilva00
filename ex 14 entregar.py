soma_notas = 0
quantidade_notas = 0

print("Digite as notas (digite -1 para encerrar):")

while True:
    nota = float(input("Digite uma nota: "))
    
    if nota == -1:
        break
    
    soma_notas += nota
    quantidade_notas += 1

if quantidade_notas > 0:
    media = soma_notas / quantidade_notas
    print(f"A média das notas é: {media:.2f}")
else:
    print("Nenhuma nota foi inserida.")
