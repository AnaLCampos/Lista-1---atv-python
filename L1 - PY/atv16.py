Valor = float(input("Digite o valor da prestação em atraso: "))
Taxa = float(input("Digite a taxa de juros em percentual: "))
Tempo = int(input("Digite o tempo em atraso em dias: "))

Prestacao = Valor + (Valor * (Taxa/100) * (Tempo/30))

print(f"O valor da prestação em atraso é: R${Prestacao:.2f}")
