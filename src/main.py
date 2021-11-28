import hashlib
import time
import pandas as pd

# de https://restcountries.com/ hago la consulta para que me traiga todo el json
from api import obtener_regiones

# hago la importación de la conexión a la base de datos
from db import ConexionDB

# Almacenar la respuesta json de la api en un dataframe
df = pd.DataFrame(obtener_regiones())

# hago el recorrido del json para poder extraer la información pertinente
arregloOrdenado = ["region", "name", "languages"]
info = df[arregloOrdenado]
# print(info)
filas = []
for i in info.index:
    try:
        # En tal caso que no se haya limpiado la lista de regiones y se detecte una region nula o sin nombre, para evitar errores se evalua dentro
        # de un try-catch usando la funcion assert() que evalua valores y devuelve una excepcion AssertionError la cual evita que enviemos a la api
        # valores vacios o nulos y se nos generen problemas
        assert (i)
        # Comienzo el reloj para calcular el tiempo que tarda cada tupla en generarse
        start_time = time.time()
        pais = info['name'][i]
        # De https://restcountries.com/ obtenga el nombre del idioma que habla el pais y encriptelo con SHA1
        for lenguaje in info['languages'][i]:
            lengua = lenguaje['name']
            # Encripto el lenguage con SHA1
            lengua = hashlib.sha1(lengua.encode('UTF-8')).hexdigest()
            # En la columna Time ponga el tiempo que tardo en armar la fila (debe ser automatico)
            # Al tiempo que se hace esto se almacena la fila en el la lista de las filas
            filas.append([info['region'][i], pais, lengua, time.time() - start_time])
    except AssertionError:
        pass

# Se crea el dataframe a mostrar como resultado, se le agregan las columnas y se rellena con las filas
dataframe = pd.DataFrame(filas, columns=["Region", "Country", "Language", "Time"])
print(dataframe)

# Con funciones de la libreria pandas muestre el tiempo total, el tiempo promedio, el tiempo minimo y el maximo que tardo en procesar toda las filas de la tabla.
print(
    "----------- tiempo total, tiempo promedio, el tiempo minimo y el maximo que tardo en procesar toda las filas de la tabla ----------------")
print(f"Tiempo total: {dataframe['Time'].sum()} s")
print(f"Tiempo promedio: {dataframe['Time'].mean()} s")
print(f"Tiempo minimo: {dataframe['Time'].min()} s")
print(f"Tiempo maximo: {dataframe['Time'].max()} s")

# Insertar todas las filas en una base de datos sqlite
db = ConexionDB()

# Crear tabla
db.crearTabla()

# Por cada fila que hay en el array de filas se envia para ser almacenada en la bd
for i in filas:
    db.insertarFila(i)

# Se muestra la tabla

print("----------- Tabla de sqlite ----------------")
for i in db.mostrarFilas():
    print(i)

# Genere un Json de la tabla creada y guardelo como data.json

# Se usa el metodo de pandas.DataFrame.to_json que nos permite exportar el dataframe creado en formato json y como argumento se pasa destino y nombre de archivo
dataframe.to_json(r'../json/data.json', orient='records')

# Se evalua el archivo json generado
print('--------- Dataframe from data.json ----------')
print(pd.read_json('../json/data.json'))
