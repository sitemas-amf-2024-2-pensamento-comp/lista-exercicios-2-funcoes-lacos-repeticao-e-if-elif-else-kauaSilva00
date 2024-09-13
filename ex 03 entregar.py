a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

if a <= 0 or b <= 0:
    print("Os números devem ser inteiros positivos.")
elif a > b:
    print("O valor de a deve ser menor ou igual ao valor de b.")
else:
   
    soma = 0
    
    for numero in range(a, b + 1):
        if numero % 3 == 0:
            soma += numero
    
    print(f"A soma dos números entre {a} e {b} que são divisíveis por 3 é: {soma}")