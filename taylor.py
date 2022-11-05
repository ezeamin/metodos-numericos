import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
from scipy.interpolate import approximate_taylor_polynomial

# g = funcion a aproximar
# approxValue = valor a aproximar
# gradoTaylor = grado del polinomio de Taylor

def taylor(g, approxValue, gradoTaylor):
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
    maxDegree = gradoTaylor
    stepDegree = 1

    if (gradoTaylor > 6):
        stepDegree = 2

    if (gradoTaylor > 30):
        stepDegree = 3

    if (gradoTaylor > 50):
        stepDegree = 4

    if (gradoTaylor > 60):
        maxDegree = 60

    print("")
    print('--------------------------------------')
    print('-------------- TAYLOR ----------------')
    print('--------------------------------------')
    print("")

    print("")
    print("----------------------------------")

    for degree in np.arange(minDegree, maxDegree, step=stepDegree):
        # function, point, degree, scale (width of interval), order (order of the polynomial)
        func_taylor = approximate_taylor_polynomial(gx, approxValue, degree, 1,
                                                    order=degree + 2)

        print("GRADO: ", degree)
        print("")
        print("f(x)=")
        print(func_taylor)
        print("")
        print(f'Valor x: {approxValue}')
        if (isinstance(valorReal, float)):
            print(f'Valor f(x) real: {valorReal:.5}')
            print(f'Valor f(x) aprox: {func_taylor(approxValue):.5}')
        else:
            print(f'Valor f(x) real: {valorReal:}')
            print(f'Valor f(x) aprox: {func_taylor(approxValue):}')
        print("")
        print(f'Error: {(abs(valorReal - func_taylor(approxValue))*100):.5}%')
        print("----------------------------------")

        # Dibujar aproximacion de grado n
        plt.plot(xValues, func_taylor(xValues), label=f"grado={degree}")

    # Dibujando detalles
    plt.legend()
    plt.axis([min, max, -10, 10])
    plt.title('Series de Taylor')
    plt.savefig("results/taylor.png")

# x = sym.Symbol('x')
# taylor(sym.log(x), 7, 15)
# plt.show()
