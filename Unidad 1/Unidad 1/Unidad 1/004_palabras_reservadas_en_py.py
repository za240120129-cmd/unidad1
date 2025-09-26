import keyword

#def True():
#    pass
# SyntaxError: invalid syntax
#is = 4
# SyntaxError: invalid syntax
a = list("letras")
print(a)
# ['l', 'e', 't', 'r', 'a', 's']
def list():
    print("Funcion list")

a = list("letras")
# TypeError: list() takes 0 positional arguments but 1 was given
print(keyword.kwlist)

# ['False', 'None', 'True', 'and', 'as', 'assert',
# 'async', 'await', 'break', 'class', 'continue',
# 'def', 'del', 'elif', 'else', 'except', 'finally',
# 'for', 'from', 'global', 'if', 'import', 'in', 'is',
# 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
# 'return', 'try', 'while', 'with', 'yield']

lenguaje = "Python"

if lenguaje == "Python":
    print("Estoy de acuerdo, Python es el mejor")
elif lenguaje == "Java":
    print("No me gusta, Java no mola")
else:
    print("Ningún otro lenguaje supera a Python")

# Salida: Estoy de acuerdo, Python es el mejor

x = 0
while x < 3:
    print(x)
    x += 1

# Salida: 0, 1, 2
for i in range(3):
    print(i)

# Salida: 0, 1, 2
for i in range(3):
    if i == 1:
        continue
    print(i)

# Salida: 0, 2
x = 0
while True:
    print(x)
    if x == 2:
        break
    x += 1

# Salida: 0, 1, 2

x = (5 == 1)
print(x)
# Salida: False

x = True
if x:
    print("Python!")
    
# Salida: Python!

def mi_funcion():
    pass

print(mi_funcion())
# Salida: None

print(True and False) # False
print(True or False)  # True
print(not True)       # False

def funcion_suma(a, b):
    print("La suma es", a + b)

funcion_suma(3, 5)

# Salida: La suma es 8

def funcion_suma(a, b):
    return a + b

suma = funcion_suma(3, 5)
print("La suma es", suma)

# Salida: La suma es 8
print("La suma es", (lambda a, b: a + b)(3, 5))

# Salida: La suma es 8

def funcion_suma(a, b):
    pass
