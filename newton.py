# Polinomio interpolación
# Diferencias Divididas de Newton
# Tarea: Verificar tamaño de vectores,
#        verificar puntos equidistantes en x
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# INGRESO , Datos de prueba
xi = np.array([1, 0, -3])  # entradas de x
fi = np.array([2,4,-2])  # entradas de y en esos puntos

xDatoDeseado = -1;
x = sym.symbols("x");
g = -(x**2)+5.5 

# PROCEDIMIENTO

# Tabla de Diferencias Divididas Avanzadas
titulo = ['i ', 'xi', 'fi']
n = len(xi)  # longitud del arreglo
numbers = np.arange(0, n, 1)  # rango numerico entre: inicio, fin, step
tabla = np.concatenate(([numbers], [xi], [fi]), axis=0)
tabla = np.transpose(tabla)  # da vuelta la tabla


# diferencias divididas vacia
dfinita = np.zeros((n, n-1), dtype=float)
tabla = np.concatenate((tabla, dfinita), axis=1)
# genera posiciones llenas de 0 a la derecha de los
# datos ya ingresados en la tabla, donde estarán
# los valores calculados

# Calcula tabla, inicia en columna 3
[n, m] = np.shape(tabla)
diagonal = n-1
j = 3  # empieza en 3 porque ahi estan los 0 en la tabla
while (j < m):
    # Añade título para cada columna
    numeroCol = str(j-2)
    titulo.append('F['+numeroCol+']')

    # cada fila de columna
    i = 0
    paso = j-2  # inicia en 1
    while (i < diagonal):
        denominador = (xi[i+paso]-xi[i])
        numerador = tabla[i+1, j-1]-tabla[i, j-1]
        tabla[i, j] = numerador/denominador
        i = i+1
    diagonal = diagonal - 1
    j = j+1

# POLINOMIO con diferencias Divididas
# caso: puntos equidistantes en eje x
dDividida = tabla[0, 3:]  # trae los valores de la 1era fila
n = len(dfinita)

# expresión del polinomio con Sympy
x = sym.Symbol('x')
polinomio = fi[0]
for j in range(1, n, 1):
    factor = dDividida[j-1]
    termino = 1
    for k in range(0, j, 1):
        termino = termino*(x-xi[k])
    polinomio = polinomio + termino*factor

# simplifica multiplicando entre (x-xi)
polisimple = polinomio.expand()

# polinomio para evaluacion numérica
px = sym.lambdify(x, polisimple)

# Puntos para la gráfica
muestras = 101  # constante
a = np.min(xi)  # minimo de las entradas
b = np.max(xi)  # máximo de las entradas
# similar a np.arange, pero usa num de elementos en vez de step
pxi = np.linspace(a, b, muestras)  # start,stop,#elements
pfi = px(pxi)

# print(px(-1)) #EVALUACION DE UN PUNTO

# SALIDA
np.set_printoptions(precision=2)  # elegimos como mostrar decimales
print('Tabla Diferencia Dividida')
print('', titulo)  # espacio para que se alinee correctamente
print(tabla)
print('dDividida: ')
print(dDividida)
print('polinomio: ')
print(polinomio)
print('polinomio simplificado: ')
print(polisimple)

# MATPLOTLIB - GRAFICA
plt.plot(xi, fi, 'o', label='Puntos')
plt.plot(pxi, pfi, label='Polinomio')
plt.plot(xDatoDeseado,g.subs(x,xDatoDeseado),'o',label="Valor real")
plt.plot(xDatoDeseado,px(xDatoDeseado),'o',label="Valor aproximado")
plt.legend()
plt.xlabel('xi')
plt.ylabel('fi')
plt.title('Diferencias Divididas - Newton')
plt.show()
