def converter_para_fahrenheit(celsius):
    
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

while True:
    try:
        celsius = float(input("Digite a temperatura em Celsius (ou digite -999 para sair): "))
        
        if celsius == -999:
            break
        
        fahrenheit = converter_para_fahrenheit(celsius)
        
        print("A temperatura em Fahrenheit é:" ,fahrenheit)
    except ValueError:
        print("Por favor, insira um número válido.")
        
print("Obrigado por usar o conversor de temperaturas.")
