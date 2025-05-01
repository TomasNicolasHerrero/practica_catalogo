# 🗃️ Gestor de Catálogos

## ✅ Funcionalidades del programa

Este gestor de catálogos permite administrar un listado de productos desde una interfaz de texto. Las funcionalidades implementadas son:

### 1. Crear producto
Permite añadir un nuevo producto al catálogo introduciendo los siguientes datos:
- **Nombre** (texto)
- **Descripción** (texto)
- **Precio** (número, puede ser entero, por ejemplo: `20`, o decimal, por ejemplo: `9.99`)
- **Stock** (número entero, por ejemplo: `15`)

El producto queda registrado en la base de datos.

### 2. Listar productos
Muestra en pantalla todos los productos existentes, con sus respectivos campos: ID, nombre, descripción, precio y stock.

### 3. Buscar producto por ID
Solicita el ID del producto y muestra sus detalles si existe. En caso contrario, informa que no se ha encontrado.

### 4. Modificar producto
Permite actualizar uno o varios campos de un producto existente:
- Se puede dejar cualquier campo en blanco si no se desea cambiar.
- Si se introducen nuevos valores, se actualizan en la base de datos.

### 5. Eliminar producto
Elimina un producto de la base de datos introduciendo su ID.

### 6. Salir
Cierra el programa.

---

## 📊 Visualización con MongoDB y `pymongo` (opcional)

Existe una versión alternativa del programa que utiliza **MongoDB** en lugar de una base de datos relacional. En este caso:

- Se emplea `pymongo` como interfaz para conectarse a la base de datos Mongo.
- Los productos se almacenan como documentos JSON.
- Las funcionalidades CRUD se mantienen iguales.
- La estructura del producto en MongoDB es:


## 🧩 Introducción de datos: consejos y errores comunes

Para evitar errores al introducir los datos en el programa, ten en cuenta lo siguiente:

### ✅ Buenas prácticas

- **Precio** debe ser un número, ya sea decimal (`19.99`) o entero (`20`)
- **Stock** debe ser un número entero sin comas ni puntos
- Los campos **nombre** y **descripción** no deben estar vacíos
- Al modificar un producto, puedes dejar campos en blanco si no quieres cambiarlos

### ⚠️ Errores comunes y soluciones

| Error                                           | Causa                                            | Solución                                         |
|------------------------------------------------|--------------------------------------------------|--------------------------------------------------|
| `ValueError: could not convert string to float` | Introdujiste texto en el campo **precio**        | Asegúrate de escribir un número como `9.99`      |
| `ValueError: invalid literal for int()`         | Pusiste texto o número decimal en el **stock**   | Escribe un número entero como `20`               |
| `"Producto no encontrado."`                     | El ID introducido no existe                      | Verifica con la opción de **listar productos**   |
| El programa se cierra inesperadamente           | Entrada vacía o tipo de dato incorrecto          | Introduce siempre el tipo de dato correcto       |
