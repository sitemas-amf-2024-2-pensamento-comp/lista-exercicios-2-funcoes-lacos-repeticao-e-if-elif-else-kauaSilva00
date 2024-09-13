def calcular_area_retangulo(largura, altura):
    return largura * altura

largura = float(input("Digite a largura do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))
area = calcular_area_retangulo(largura, altura)

print("A área do retângulo é:", area)
