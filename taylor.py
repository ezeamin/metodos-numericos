import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
from scipy.interpolate import approximate_taylor_polynomial

# value of x to approximate the function at
approxValue = 3
max = approxValue+5
min = approxValue-5

# Creating a vector of 100 equally spaced points between -10 and 10.
x = sym.Symbol('x')
xValues = np.linspace(min, max, num=100)

# Function to approximate
g = sym.sin(x)

# X values for approximation
gx = sym.lambdify(x, g)
evaluatedValues = gx(xValues)  # Array of values
valorReal = gx(approxValue)

# Draw function to approximate.
plt.plot(xValues, evaluatedValues, "--", label="Funcion a aproximar")
plt.plot(approxValue, gx(approxValue), 'o', label="Valor real")

minDegree = 1
maxDegree = 15
stepDegree = 2

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

    # Draw approximation at that degree
    plt.plot(xValues, func_taylor(xValues), label=f"grado={degree}")

# Drawing details
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left',
           borderaxespad=0.0, shadow=True)
plt.tight_layout()
plt.axis([min, max, -10, 10])
plt.show()
