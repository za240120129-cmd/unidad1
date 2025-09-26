# Ejercicios de Arreglos en Python
# los comentarios no son muy explicativos, solo lo basico

# 1. Monitoreo de sensores de temperatura
print("Ejercicio 1")
sensores = [55,62,48,70,61,59,80,45]
cont = 0
for i in range(0,8):  # puse 8 porque son 8 sensores
    if sensores[i] > 60:
        print("El sensor", i, "tiene", sensores[i], "grados")
        cont = cont + 1
print("cuantos superan 60:", cont)

print("---")

# 2. Validacion de clave de acceso
print("Ejercicio 2")
clave_ok = [1,2,3,4]
fallos = 0
entradas = [[1,2,3,4],[9,9,9,9],[0,0,0,0],[1,2,5,4],[1,2,3,4]]
for clave in entradas:
    if clave==clave_ok:
        print("bien, clave correcta")
        fallos=0
    else:
        print("mal intento", clave)
        fallos=fallos+1
        if fallos>=3:
            print("Alarma activada!!!")
            break

print("---")

# 3. Adquisicion de señales
print("Ejercicio 3")
voltajes = [3.0,3.1,3.4,3.2,3.5,3.6,3.1,3.0,3.3,3.7,3.8,3.2]
suma=0
for x in voltajes:
    suma=suma+x
promedio = suma/12  # puse 12 fijo en lugar de len
print("prom:",promedio)
if promedio>3.3:
    print("ALARMA")
else:
    print("voltaje normal")

print("---")

# 4. Estados digitales
print("Ejercicio 4")
botones=[True,False,False,True,False,True,False,False,True,False]
def cuales(arr):
    res=[]
    for j in range(0,len(arr)):
        if arr[j]==True:
            res.append(j)
    return res

print("presionados:",cuales(botones))

print("---")

# 5. Mapeo sensores
print("Ejercicio 5")
matriz=[[1,2,3],[2,3,1],[3,1,2],[1,1,3]]
fila=2
columna=1
num = matriz[fila][columna]
if num==1:
    print("es termico")
if num==2:
    print("es luminoso")
if num==3:
    print("es digital")
