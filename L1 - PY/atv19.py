#Ler o número da conta
numconta = int(input("Digite o número da conta corrente (3 dígitos): "))

#Inverso do número
inverso = int(str(numconta)[::-1])

#Somar o número com o inverso
soma = numconta + inverso

#Calcular o dígito verificador
digitoverificador = str(soma)[::-1][0]

#Resultado
print("Dígito verificador da conta:", digitoverificador)
