# mongo_gui.py

import tkinter as tk
from pymongo import MongoClient

# Conexión a MongoDB local
client = MongoClient("mongodb://localhost:27017/")
db = client["catalogo"]
coleccion = db["productos"]

def cargar_productos():
    lista.delete(0, tk.END)  # Limpiar lista
    productos = coleccion.find()
    for p in productos:
        linea = f"{p['nombre']} - {p['descripcion']} - {p['precio']}€ - Stock: {p['stock']}"
        lista.insert(tk.END, linea)

# Configurar ventana principal
ventana = tk.Tk()
ventana.title("Catálogo MongoDB")
ventana.geometry("600x400")

# Título
titulo = tk.Label(ventana, text="Productos en MongoDB", font=("Arial", 16))
titulo.pack(pady=10)

# Lista de productos
lista = tk.Listbox(ventana, width=80, height=15)
lista.pack()

# Botón para recargar productos
boton = tk.Button(ventana, text="Cargar productos", command=cargar_productos)
boton.pack(pady=10)

ventana.mainloop()
