numero = input("Digite um número inteiro positivo: ")

somaDigitos = 0

for digito in numero:
    somaDigitos += int(digito)

print(f"A soma dos dígitos é: {somaDigitos}")