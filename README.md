# Interpolacion

Este programa permite interpolar una funcion en un punto dado.

Se analizan las interpolaciones de Lagrange y Newton, añadiendo una comparacion con las Series de Taylor.

## Ejecucion

Para ejecutar el programa, se debe ejecutar el archivo `__main__.py` con Python 3.6 o superior.

Se deberá instalar las librerias mencionadas en el apartado más abajo, con el comando

```bash
$ pip install (libreria)
```

Tambien, se puede instalar el programa, generando un ejecutable, de la siguiente manera:

```bash
$ pip install pyinstaller
```

Aqui se deberá reiniciar la consola, y ejecutar el siguiente comando:

```bash
$ pyinstaller --onefile --windowed __main__.py
```

Se generará una carpeta `dist`, en la cual se encontrará el ejecutable.

Si no detectara "pyinstaller", se deberá agregar a las variables de entorno manualmente, o bien intentar reiniciar la PC.

## Uso

Se ingresa la cantidad de puntos deseados, y luego la funcion en terminos de x, el punto x a interpolar, y el grado de la interpolacion para las series de Newton.

Se observarán los resultados de las interpolaciones, y las series de Taylor, tanto por pantalla como en archivos guardados dentro de la carpeta "results".

Allí mismo se guardan los detalles de los calculos, para poder ser consultados, incluido el error de cada metodo.

## Librerias

- numpy
- matplotlib
- sympy
- scipy
