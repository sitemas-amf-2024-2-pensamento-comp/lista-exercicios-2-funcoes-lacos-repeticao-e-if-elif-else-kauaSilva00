a = int(input("Digite o primeiro número inteiro positivo (a): "))
b = int(input("Digite o segundo número inteiro positivo (b): "))

resultado = 0

if a < 0 or b < 0:
    print("Por favor, digite apenas números inteiros positivos.")
else:
    for _ in range(b):
        resultado += a

    print(f"O resultado de {a} multiplicado por {b} é: {resultado}")