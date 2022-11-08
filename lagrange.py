import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# g = funcion a aproximar
# approxValue = valor a aproximar
# xi = valores de x
# fxi = valores de f(x)


def lagrange(g, approxValue, xi, fxi):
    x = sym.Symbol('x')

    # ---------- PROCEDIMIENTO -----------
    n = len(xi)
    polinomio = 0

    # términos
    for i in range(0, n, 1):
        num = 1
        den = 1
        for j in range(0, n, 1):
            if (j != i):
                num = num * (x-xi[j])
                den = den * (xi[i]-xi[j])
                termino = num / den
        polinomio = polinomio + termino * fxi[i]

    # simplificar polinomio
    polisimple = polinomio.expand()

    # para evaluar numericamente
    px = sym.lambdify(x, polisimple)

    # ---------- RESULTADOS -----------
    muestras = 101
    a = np.min(xi)
    b = np.max(xi)
    if (approxValue < a):
        a = approxValue
    elif (approxValue > b):
        b = approxValue
    pxi = np.linspace(a, b, muestras)
    pfi = px(pxi)

    # para evaluar numericamente la funcion real
    gx = sym.lambdify(x, g)
    pgi = gx(pxi)

    fxDatoDesReal = gx(approxValue)
    fxDatoDesAprox = px(approxValue)

    error = abs(fxDatoDesReal - fxDatoDesAprox) * 100

    # imprimir datos
    print("")
    print('--------------------------------------')
    print('-------------- LAGRANGE --------------')
    print('--------------------------------------')
    print("")
    print("Valores de xi: ", xi)
    print("Valores de f(xi): ", fxi)
    print(" ")
    print("Polinomio de LaGrange")
    print(polisimple)
    print(" ")
    print(f'Valor X deseado: {approxValue:}')
    # format only when its a float
    if (isinstance(fxDatoDesReal, float)):
        print(f'Valor f(x) real: {fxDatoDesReal:.4}')
        print(f'Valor f(x) aprox: {fxDatoDesAprox:.4}')
    else:
        print(f'Valor f(x) real: {fxDatoDesReal:}')
        print(f'Valor f(x) aprox: {fxDatoDesAprox:}')
    print(" ")

    if (isinstance(error, float)):
        print(f'Error: {error:.4}%')
    else:
        print(f'Error: {error:}%')

    # imprimir gráfica
    plt.figure(num='LaGrange')
    plt.plot(xi, fxi, 'o', label='Puntos')
    plt.plot(pxi, pfi, label="Polinomio")
    plt.plot(pxi, pgi, "--", label="Funcion real")
    plt.plot(approxValue, fxDatoDesReal, 'o', label="Valor real")
    plt.plot(approxValue, fxDatoDesAprox, 'o', label="Valor aproximado")
    plt.legend()
    plt.xlabel('xi')
    plt.ylabel('fi')
    plt.title('Interpolacion de LaGrange')
    plt.savefig("lagrange.png")