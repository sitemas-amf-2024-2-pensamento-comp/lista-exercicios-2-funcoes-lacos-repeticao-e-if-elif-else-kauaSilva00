n = int(input("Digite um número:"))

if n <= 0:
    print("Digite um número inteiro positivo:")
else:
    print("Contagem regressiva")
    for i in range (n, -1, -1 ):
        print(i)
