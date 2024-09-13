numeros = []

# Solicita ao usuário 5 números inteiros
for i in range(5):
    numero = int(input(f"Digite o número {i + 1}: "))
    numeros.append(numero)

# Encontra o maior e o menor número na lista
maior_numero = max(numeros)
menor_numero = min(numeros)

# Exibe o maior e o menor número
print(f"O maior número é: {maior_numero}")
print(f"O menor número é: {menor_numero}")
