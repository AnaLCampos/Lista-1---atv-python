Salariominimo = float(input("Digite o valor do salário mínimo: "))
Quilowatts = int(input("Digite a quantidade de quilowatts gasta pela residência: "))

Valorquilowatt = salariominimo / 700
Valortotal = valorquilowatt * quilowatts
Valorcomdesconto = valortotal * 0.9

print(f"Valor do quilowatt: R${valorquilowatt:.2f}")
print(f"Valor a ser pago: R${valortotal:.2f}")
print(f"Valor com desconto: R${valorcomdesconto:.2f}")
