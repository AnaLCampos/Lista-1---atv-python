Valorproduto = float(input("Digite o valor do produto: "))

Desconto = valorproduto * 0.09
novovalor = valorproduto - desconto

print("Valor com desconto de 9%: R${:.2f}".format(novovalor))
