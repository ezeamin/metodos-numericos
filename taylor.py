import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
from scipy.interpolate import approximate_taylor_polynomial

# g = funcion a aproximar
# approxValue = valor a aproximar
def taylor(g, approxValue):
    # value of x to approximate the function at
    max = approxValue+5
    min = approxValue-5

    # Creando un vector de 100 puntos espaciados uniformemente entre -10 y 10.
    x = sym.Symbol('x')
    xValues = np.linspace(min, max, num=100)

    # Valores de x para aproximación
    gx = sym.lambdify(x, g)
    evaluatedValues = gx(xValues)  # Array of values
    valorReal = gx(approxValue)

    # Dibujar funcion de aproximacion
    plt.figure(num='Taylor')
    plt.plot(xValues, evaluatedValues, "--", label="Funcion a aproximar")
    plt.plot(approxValue, gx(approxValue), 'o', label="Valor real")

    minDegree = 1
    maxDegree = 15
    stepDegree = 2

    print("")
    print('--------------------------------------')
    print('-------------- TAYLOR ----------------')
    print('--------------------------------------')
    print("")

    print("*****************")
    print(f'* g(x) = {g} *')
    print("*****************")
    print("")
    print("----------------------------------")

    for degree in np.arange(minDegree, maxDegree, step=stepDegree):
        # function, point, degree, scale (width of interval), order (order of the polynomial)
        func_taylor = approximate_taylor_polynomial(gx, 0, degree, 1,
                                                    order=degree + 2)

        print("GRADO: ", degree)
        print("")
        print("f(x)=")
        print(func_taylor)
        print("")
        print(f'Valor x: {approxValue}')
        print(f'Valor real g: {valorReal}')
        print(f'Valor aproximado f: {func_taylor(approxValue):.5}')
        print("")
        print(f'Error: {(abs(valorReal - func_taylor(approxValue))*100):.5}%')
        print("----------------------------------")

        # Dibujar aproximacion de grado n
        plt.plot(xValues, func_taylor(xValues), label=f"grado={degree}")

    # Dibujando detalles
    plt.legend()
    plt.tight_layout()
    plt.axis([min, max, -10, 10])
    plt.title('Series de Taylor')
    # plt.show()
