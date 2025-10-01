altura = int(input("Informe sua altura em cm:"))
peso = int(input("Informe seu peso em kg:"))
imc = peso / (altura/100) ** 2
print("Seu IMC é: ", imc)

