import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# g = funcion a aproximar
# approxValue = valor a aproximar
# xi = vector de puntos x
# fi = vector de puntos f(x)


def newton(g, approxValue, xi, fi):
    x = sym.Symbol("x")

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
    if (approxValue < a):
        a = approxValue
    elif (approxValue > b):
        b = approxValue
    # similar a np.arange, pero usa num de elementos en vez de step
    pxi = np.linspace(a, b, muestras)  # start,stop,#elements
    pfi = px(pxi)

    gx = sym.lambdify(x, g)
    pgi = gx(pxi)

    real = gx(approxValue)
    aprox = px(approxValue)

    error = abs(real - aprox) * 100

    # SALIDA
    np.set_printoptions(precision=2)  # elegimos como mostrar decimales
    print('--------------------------------------')
    print('-------------- NEWTON ----------------')
    print('--------------------------------------')
    print("")
    print('Tabla Diferencias Divididas')
    print('', titulo)  # espacio para que se alinee correctamente
    print(tabla)
    print('dDividida: ')
    print(dDividida)
    print('polinomio: ')
    print(polinomio)
    print('polinomio simplificado: ')
    print(polisimple)
    print("")
    print("")
    print(f'Valor X deseado: {approxValue:}')
    if (isinstance(real, float)):
        print(f'Valor f(x) real: {real:.4}')
        print(f'Valor f(x) aprox: {aprox:.4}')
    else:
        print(f'Valor f(x) real: {real:}')
        print(f'Valor f(x) aprox: {aprox:}')

    print(" ")
    if (isinstance(error, float)):
        print(f'Error: {error:.4}%')
    else:
        print(f'Error: {error:}%')

    # MATPLOTLIB - GRAFICA
    plt.figure(num='Newton')
    plt.plot(xi, fi, 'o', label='Puntos')
    plt.plot(pxi, pfi, label='Polinomio')
    plt.plot(pxi, pgi, "--", label="Funcion real")
    plt.plot(approxValue, g.subs(x, approxValue), 'o', label="Valor real")
    plt.plot(approxValue, px(approxValue), 'o', label="Valor aproximado")
    plt.legend()
    plt.xlabel('xi')
    plt.ylabel('fi')
    plt.title('Diferencias Divididas - Newton')
    plt.savefig("newton.png")