
# Problema 1: Control de Temperatura
print("Problema 1")

valores = [60, 68, 72, 75, 64, 70, 66]  # como si fueran lecturas
fan = False  # el ventilador al inicio

x = 0
while x < len(valores):  # simulamos el monitoreo continuo con lista
    t = valores[x]
    print("Temp:", t)
    if t > 70:
        fan = True
        print("Ventilador ON")
    else:
        if t < 65:
            fan = False
            print("Ventilador OFF")
        else:
            print("sin cambios")
    x = x + 1

print("---")

# Problema 2: Revision de Voltaje
print("Problema 2")
volt = [3.2, 3.3, 3.7, 4.1, 2.9]

for v in volt:
    if v < 3.3:
        print(v, "= Baja")
    elif v >= 4.0:
        print(v, "= Optima")
    else:
        print(v, "= Advertencia")

print("---")

# Problema 3: Contador de Señales Digitales
print("Problema 3")

senal = [1,0,1,1,0,0,1,0,1,0,1,1,1,0,0,1,1,0,0,1]

altas = 0
bajas = 0

c1 = 0
while True:  # como si fuera do while
    if senal[c1] == 1:
        altas = altas + 1
    else:
        bajas = bajas + 1
    c1 = c1 + 1
    if c1 >= 20:
        break

print("Altas:", altas, "Bajas:", bajas)
if altas > bajas:
    print("Alto flujo de datos")
else:
    print("Indicador apagado")
