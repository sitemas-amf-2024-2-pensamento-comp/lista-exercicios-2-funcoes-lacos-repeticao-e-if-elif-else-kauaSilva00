def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print("Temperatura em Celsius | Temperatura em Fahrenheit")
print("-" * 40)

for celsius in range(0, 101, 10):
    fahrenheit = celsius_para_fahrenheit(celsius)
    print(f"{celsius:>22} | {fahrenheit:>24.1f}")