def saludo():
    mensaje = "¡Hola, mundo!"  # Variable local
    print(mensaje)

saludo()
#print(mensaje)  # Esto generará un error porque 'mensaje' es local a la función.

def funcion_exterior():
    mensaje = "Hola desde la función exterior"  # Variable en el alcance 'enclosing'

    def funcion_interior():
        print(mensaje)  # La función interior accede a la variable de la exterior

    funcion_interior()

funcion_exterior()

def funcion_exterior():
    mensaje = "Hola desde la función exterior"  # Variable en el alcance 'enclosing'

    def funcion_interior():
        print(mensaje)  # La función interior accede a la variable de la exterior

    funcion_interior()

funcion_exterior()

from math import sqrt  # 'sqrt' es una función built-in del módulo 'math'

numero = 16
raiz_cuadrada = sqrt(numero)  # Usamos la función built-in para calcular la raíz cuadrada
print(f"La raíz cuadrada de {numero} es {raiz_cuadrada}")
