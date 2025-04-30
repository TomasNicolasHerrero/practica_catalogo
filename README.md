# practica_catalogo 

# Introducción
Este proyecto contiene códigos de ejemplo del uso de SQLAlchemy sobre una bbdd
sqlite.
Existen dos formas de usar SQLAlchemy: mediante ENGINE (lanzando consultas sql
directamente) u ORM (generando los objetos a partir de la bbdd)
## Instalación de dependencias
El archivo requirements.txt contiene las dependencias del proyecto. Ha sido
generado del siguiente modo:
pip freeze >> requirements.txt
De cara a la práctica deberéis generar un nuevo proyecto y utilizar un entorno
virtual env o venv, según os lo especifique PyCharm en la misma pantalla donde
estáis introduciendo la ruta y el nombre del proyecto.
Una vez esté creado, copiaréis el archivo requirements.txt dentro del proyecto y,
desde la terminal ABIERTA DESDE PYCHARM, ejecutaréis esta instrucción:
pip install -r requirements.txt
**NOTA** En mi ordenador el comando ha sido el siguiente
(.venv) rauldelaguila@MacBook-Pro-de-Raul-2 acceso_bbdd % pip install -r
requirements.txt
FIJAOS QUE APARECE UN (.venv) delante de mi nombre de usuario.
Como podéis ver, existen dos dependencias que son muy relevantes: sqlalchemy y
sqlacodegen. Estas dependencias deben estar instaladas en vuestro proyecto.
## sqlacodegen
1. sqlacodegen permite generar de forma automática las clases a partir de una base
de datos sqlalchemy. Para hacer esto sobre recetas, podéis hacer lo siguiente:
sqlacodegen sqlite:///./recetas.db
**NOTA** En mi línea de comandos ha sido así: (.venv) rauldelaguila@MacBook-Pro-
de-Raul-2 acceso_bbdd % sqlacodegen sqlite:///./recetas.db >> recetas.py
Posteriormente, el código recetas.py lo he metido dentro de un paquete nuevo (en mi
caso ddbb)
2. En vuestro caso, de cara al proyecto, tendréis que generar una base de datos de
catálogo y seguir los mismos pasos.
## Ejemplos de uso de sqlalchemy
En este proyecto tenéis 6 códigos con ejemplos de uso de sqlalchemy. De cara a la
práctica, fijaos en los códigos denominados ejemplo_{operacion}.py, donde
{operacion} es actualización, borrado, query e insert.
