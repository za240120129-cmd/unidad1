import sqlite3

def conecta_db():
    return sqlite3.connect('gastos.db')

def crea_tabla():
    with conecta_db() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS gastos (
                categoria TEXT NOT NULL,
                cantidad REAL NOT NULL
            )''')
def add_gasto(categoria, cantidad):
    with conecta_db() as conn:
        conn.execute('''
            INSERT INTO gastos (categoria, cantidad)
            VALUES (?, ?)''', (categoria, cantidad))
def get_gastos(categoria=None):
    with conecta_db() as conn:
        cursor = conn.cursor()
        query = 'SELECT * FROM gastos WHERE '
        condiciones, parametros = [], []

        if categoria:
            condiciones.append("categoria = ?")
            parametros.append(categoria)

        query += " AND ".join(condiciones) if condiciones else "1=1"

        cursor.execute(query, parametros)
        return cursor.fetchall()
crea_tabla()
add_gasto("Transporte", 5)
add_gasto("Comida", 5)
add_gasto("Comida", 7)
add_gasto("Alquiler", 300)

gastos = get_gastos()
for gasto in gastos:
    print(gasto)

gastos = get_gastos(categoria="Comida")
for gasto in gastos:
    print(gasto)
