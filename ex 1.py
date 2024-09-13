def MostrarMenu():
    print("Escolha uma opereção:")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair do programa")


def calcular(operador, num1, num2):
    if operador == 1:
        return num1 + num2
    elif operador == 2:
        return num1 - num2
    elif operador == 3:
        return num1 * num2
    elif operador == 4:
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro! Divisão por zero"
    else:
        return "Saindo/encerrando o programa..."


def main():
    while True:
        MostrarMenu()
        opcaoDigitada = int(input("Digite uma opção:"))

        if opcaoDigitada == 5:
            print("Saindo do programa...")
            break

        num1 = float(input("Digite o primeiro número:"))
        num2 = float(input("Digite o segundo número:"))


        resultado = calcular(opcaoDigitada, num1, num2)

        print("O resultado é:", resultado)

        continuaOuNao = input("Deseja continuar? (s/n):")

        if continuaOuNao . lower() != 's':
            print("Obrigado por usar a calculador. Encerrando...")
            break
MostrarMenu()


