import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('catalogo.db')
cursor = conn.cursor()

# Ejecutar la consulta para obtener los nombres de las tablas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print(tables)

# Ejecutar una consulta para obtener todos los datos de la tabla "productos"
cursor.execute("SELECT * FROM productos;")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Cerrar la conexión después de las consultas
conn.close()

