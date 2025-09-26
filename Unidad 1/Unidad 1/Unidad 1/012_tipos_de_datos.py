# Ejercicios electricos en Python
# comentarios sencillos, sin mucha explicacion

# 1. Registro de consumo electrico
print("Problema 1")
consumo = {"tv":120, "refri":200, "pc":90, "lampara":40}
total=0
for aparato in consumo:
    total=total+consumo[aparato]
print("Total:", total)
for aparato in consumo:
    porc=(consumo[aparato]/total)*100
    print(aparato, porc,"%")
    if porc>30:
        print("-- este supera 30%")

print("---")

# 2. Seguimiento de averias
print("Problema 2")
averias=[("01-01","corto"),("02-01","falla"),("03-01","corto"),("04-01","corto")]
conts={}
for f,tipo in averias:
    if tipo in conts:
        conts[tipo]=conts[tipo]+1
    else:
        conts[tipo]=1
print(conts)
mas=0
mas_tipo=""
for k in conts:
    if conts[k]>mas:
        mas=conts[k]
        mas_tipo=k
print("Mas frecuente:",mas_tipo)

print("---")

# 3. Contador señales digitales
print("Problema 3")
senales=[1,0,1,1,0,0,1,0,1,0,1,0,1,1,1,0,0,1,0,1]
a=0
b=0
c=0
while True:
    if senales[c]==1:
        a=a+1
    else:
        b=b+1
    c=c+1
    if c>=20:
        break
print("Altas:",a,"Bajas:",b)
if a>b:
    print("indicador ON")
else:
    print("indicador OFF")

print("---")

# 4. Revision instalaciones
print("Problema 4")
estados=["apto","reparar","correcto","reparar","apto"]
reps=0
for e in estados:
    if e=="reparar":
        reps=reps+1
print("Necesitan reparar:",reps)
if reps>2:
    print("ALERTA muchas reparaciones")

print("---")

# 5. Listado unico suministros
print("Problema 5")
lista1=["cable","foco","cable","fusible"]
unicos=set(lista1)
print("Unicos:",unicos)

print("---")

# 6. Historial interrupciones
print("Problema 6")
cortes=[(1,3),(5,8),(10,12)]
acum=0
for ini,fin in cortes:
    acum=acum+(fin-ini)
print("Total sin servicio:",acum)
if acum>5:
    print("mucho tiempo sin servicio")

print("---")

# 7. Agenda mantenimientos
print("Problema 7")
fechas={"2023-10-01","2023-10-05"}
fechas.add("2023-10-03")
fechas.add("2023-10-01") # repetida
orden=sorted(fechas)
for f in orden:
    print(f)

print("---")

# 8. Potencia por habitacion
print("Problema 8")
habs={"sala":[60,100],"cocina":[200,150],"cuarto":[80,90]}
total_g=0
for h in habs:
    suma=0
    for p in habs[h]:
        suma=suma+p
    print("Potencia",h,":",suma)
    if suma>250:
        print("-- sobre limite")
    total_g=total_g+suma
print("Total general:",total_g)

print("---")

# 9. Fugas
print("Problema 9")
fugas={"01-01":1,"02-01":2,"03-01":1}
for d in fugas:
    if fugas[d]>1:
        print("dia",d,"tiene",fugas[d],"fugas")

print("---")

# 10. Distribucion carga fases
print("Problema 10")
cargas=[10,20,15,25,30,12]
fases=[[],[],[]]
i=0
for c in cargas:
    fases[i%3].append(c)
    i=i+1
for j in range(0,3):
    s=0
    for x in fases[j]:
        s=s+x
    print("fase",j,":",s)
    if s>40:
        print("!! sobrecarga en fase",j)
