refrigerante = int(input("Ingrese el refrigerante: "))

temperatura = int(input("Ingrese la temperatura: "))

pressure = int(input("Ingrese la presion: "))

#CONDICIONALES

if (refrigerante >= 50) and (temperatura >= 800) and (pressure >= 500):
    print("Estado: CRITICO")
elif (refrigerante >= 50) and (600 <= temperatura <= 800) or (300 <= pressure <= 500):
    print("Estado: ALERTA")
elif (refrigerante >= 50) and (temperatura < 600) and (pressure < 300):
    print("Estado: NORMAL")
elif (refrigerante <= 50) and (temperatura > 800) and (pressure > 500):
    print("Estado: CRITICO")
elif (refrigerante <= 50) and (600 < temperatura < 800) or (300 < pressure < 500):
    print("Estado: CRITICO")
else:
    print("Error")