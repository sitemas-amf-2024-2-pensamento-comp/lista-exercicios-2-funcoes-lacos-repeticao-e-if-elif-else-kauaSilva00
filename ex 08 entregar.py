n = int(input("Digite um número inteiro positivo: "))

if n <= 0:
    print("Por favor, digite um número inteiro positivo.")
else:
    print(f"Divisores de {n}:")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)
    