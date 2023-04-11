import math

pi = math.pi

Raio = float(input("Digite o raio do círculo: "))

Circunferencia = 2 * pi * Raio
Area = pi * Raio**2

print("Circunferência:", round(Circunferencia, 2))
print("Área:", round(Area, 2))
