numero = int(input("Digite um número inteiro: "))

print("Tabuada do:", numero)
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
