import math

catetoA = float(input("Digite o valor do cateto A: "))
catetoB = float(input("Digite o valor do cateto B: "))

hipotenusa = math.sqrt(catetoA**2 + catetoB**2)

print("Hipotenusa:", round(hipotenusa, 1))
