# prueba-zinobe

## Trabajo a resolver
|Region | City Name |  Languaje | Time  |
|---|---|---|---|
|  Africa | Angola  |  AF4F4762F9BD3F0F4A10CAF5B6E63DC4CE543724 | 0.23 ms  |
|   |   |   |   |
|   |   |   |   |

Desarrolle una aplicacion en python que genere la tabla anterior teniendo las siguientes consideraciones:

- De https://restcountries.com/ obtenga el nombre del idioma que habla el pais y encriptelo con SHA1
- En la columna Time ponga el tiempo que tardo en armar la fila (debe ser automatico)
- La tabla debe ser creada en un DataFrame con la libreria PANDAS
- Con funciones de la libreria pandas muestre el tiempo total, el tiempo promedio, el tiempo minimo y el maximo que tardo en procesar toda las filas de la tabla.
- Guarde el resultado en sqlite.
- Genere un Json de la tabla creada y guardelo como data.json
- La prueba debe ser entregada en un repositorio git.



**Es un plus si:**
* No usa framework
* Entrega Test Unitarios
* Presenta un diseño de su solucion.

## Descargar:

```
https://github.com/mdmd0497/prueba_zinobe.git
```

```
cd prueba_zinobe
```


## Correr el proyecto

```
python -m venv venv 
```
si esta en windows ejecutar esta linea
```
.\venv\Scripts\activate
```
*-----------------------------------------------------------------------------------------------------------------------------------------*
```
pip install -r requirements.txt
```
```
cd src
```

```
python main.py
```




