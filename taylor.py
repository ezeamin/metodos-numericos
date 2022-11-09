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
    
    if (gradoTaylor > 60):
        maxDegree = 60

    print("")
    print('--------------------------------------')
    print('-------------- TAYLOR ----------------')
    print('--------------------------------------')
    print("")

    print("")
    print("----------------------------------")

    for degree in np.arange(minDegree, maxDegree+1, step=stepDegree):
        func_taylor = 0
        error = 0

        # Aca se elevan dos casos de calculo. En el try estará la mayoria, usando la libreria,
        # y en el except se hará el calculo manualmente en casos mas extremos con el valor x=0.

        try:
        # function, point, degree, scale (width of interval), order (order of the polynomial)
            func_taylor = approximate_taylor_polynomial(gx, 0, degree, 1,
                                                        order=degree + 2)

            # si incluye algun nan, salir del try
            if (np.isnan(func_taylor(approxValue))):
                raise Exception
            else:
                error = abs(valorReal - func_taylor(approxValue))*100

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
                print(f'Error: {error:.5}%')
                print("----------------------------------")

                # Dibujar aproximacion de grado n
                plt.plot(xValues, func_taylor(xValues),
                         label=f"grado={degree}")

        except:
            # 2do caso, en caso que la libreria no pueda aproximar la funcion
            # porque se tenga un valor que genere error matematico en x=0
            func_taylor = gx(approxValue)
            for internalDegree in np.arange(1, degree+1, step=1):

                derivativeExp = sym.diff(g, x, internalDegree)
                derivative = sym.lambdify(x, derivativeExp)

                func_taylor += (derivative(approxValue) * (x - approxValue)
                                ** internalDegree) / sym.factorial(internalDegree)

            func_taylor = func_taylor.expand()
            func_taylorTest = sym.lambdify(x, func_taylor)

            error = abs(valorReal - func_taylorTest(approxValue))*100

            print("GRADO: ", degree)
            print("")
            print("f(x)=")
            print(func_taylor)
            print("")
            print(f'Valor x: {approxValue}')
            if (isinstance(valorReal, float)):
                print(f'Valor f(x) real: {valorReal:.5}')
                print(f'Valor f(x) aprox: {func_taylorTest(approxValue):.5}')
            else:
                print(f'Valor f(x) real: {valorReal:}')
                print(f'Valor f(x) aprox: {func_taylorTest(approxValue):}')
            print("")
            print(f'Error: {error:.5}%')
            print("----------------------------------")

            # Dibujar aproximacion de grado n
            plt.plot(xValues, func_taylorTest(
                xValues), label=f"grado={degree}")

    # Dibujando detalles
    plt.legend()
    plt.axis([min, max, -10, 10])
    plt.title('Series de Taylor')
    plt.savefig("taylor.png")
