valor_emprestimo = float(input("Digite o valor do empréstimo: "))
taxa_juros_mensal = float(input("Digite a taxa de juros mensal (em %): "))
num_meses = int(input("Digite o número de meses para pagar: "))
salario = float(input("Digite o salário mensal: "))

taxa_juros_mensal_decimal = taxa_juros_mensal / 100

if taxa_juros_mensal_decimal == 0:
    prestacao_mensal = valor_emprestimo / num_meses
else:
    prestacao_mensal = valor_emprestimo * (taxa_juros_mensal_decimal * (1 + taxa_juros_mensal_decimal) ** num_meses) / ((1 + taxa_juros_mensal_decimal) ** num_meses - 1)

limite_prestacao = 0.30 * salario

print(f"\nValor da prestação mensal: R${prestacao_mensal:.2f}")

if prestacao_mensal > limite_prestacao:
    print("Empréstimo não aprovado. O valor da prestação é maior que 30% do seu salário.")
else:
    print("Empréstimo aprovado. O valor da prestação está dentro do limite de 30% do seu salário.")