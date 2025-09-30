dias = int(input("Informe o número de dias:"))
horas = int(input("Informe o número de horas:"))
minutos = int(input("Informe o número de minutos:"))
segundos = int(input("Informe o número de segundos:"))
total_segundos = (dias * 24 * 3600) + (horas * 3600) + (minutos * 60) + segundos
print("O total em segundos é: ", total_segundos)