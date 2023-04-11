Quantidade = int(input("Digite a quantidade de fitas da locadora: "))
valordoaluguel = float(input("Digite o valor cobrado por aluguel: "))

#Faturamento anual
faturamento = Quantidade * valordoaluguel * 12 / 3
print("Faturamento anual: R${:.2f}".format(faturamento))

#valor das multas por mês
multas = Quantidade / 10 * valordoaluguel * 0.1
print("Valor das multas por mês: R${:.2f}".format(multas))

#total de fitas ao final do ano
totalfitas = Quantidade + Quantidade / 10 - Quantidade * 0.02
print("Total de fitas ao final do ano: {:.2f}".format(totalfitas))
