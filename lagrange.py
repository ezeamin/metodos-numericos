import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# Introduccion de datos: xi y f(xi)
xi = np.array([1, 2, 4])
fxi = np.array([0, 0.693, 1.386])

xDatoDeseado = 5
x = sym.Symbol('x')
g = sym.ln(x)

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
if (xDatoDeseado < a):
    a = xDatoDeseado
elif (xDatoDeseado > b):
    b = xDatoDeseado
pxi = np.linspace(a, b, muestras)
pfi = px(pxi)

# para evaluar numericamente la funcion real
gx = sym.lambdify(x, g)
pgi = gx(pxi)

fxDatoDesReal = gx(xDatoDeseado)
fxDatoDesAprox = px(xDatoDeseado)

error = abs(fxDatoDesReal - fxDatoDesAprox) * 100

# imprimir datos
print("Valores de xi: ", xi)
print("Valores de f(xi): ", fxi)
print(" ")
print("Polinomio de LaGrange")
print(polisimple)
print(" ")
print(f'Valor X deseado: {xDatoDeseado:}')
print(f'Valor f(x) real: {fxDatoDesReal:.4}')
print(f'Valor f(x) aprox: {fxDatoDesAprox:.4}')
print(" ")
print(f'Error: {error:.4}%')

# imprimir gráfica
plt.figure(num='LaGrange')
plt.plot(xi, fxi, 'o', label='Puntos')
plt.plot(pxi, pfi, label="Polinomio")
plt.plot(pxi, pgi, "--", label="Funcion real")
plt.plot(xDatoDeseado, fxDatoDesReal, 'o', label="Valor real")
plt.plot(xDatoDeseado, fxDatoDesAprox, 'o', label="Valor aproximado")
plt.legend()
plt.xlabel('xi')
plt.ylabel('fi')
plt.title('Interpolacion de LaGrange')
plt.show()
