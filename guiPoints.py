from tkinter import *
from rootCreation import root

import sympy as sym
import numpy as np
import matplotlib.pyplot as plt

import sys

from newton import newton
from lagrange import lagrange
from taylor import taylor

points = []
values = []

pointsFrame = Frame(root, width=500, height=500)
errorLabel = Label(pointsFrame, text="Error! Revise los campos", bg="yellow", font=(
    "Comic Sans MS", 15))

funcBox = Entry(pointsFrame, font=("Comic Sans MS", 15))
valueBox = Entry(pointsFrame, font=("Comic Sans MS", 15))
grado = Entry(pointsFrame, font=("Comic Sans MS", 15))


def calculate(e=None):
    try:
        for point in points:
            values.append((float(point[0].get()), float(point[1].get())))
        errorLabel.destroy()
        g = sym.sympify(funcBox.get())
        approxValue = float(valueBox.get())
        gradoTaylor = int(grado.get())

        xi = np.array([])
        fi = np.array([])
        for point in values:
            xi = np.append(xi, point[0])
        for point in values:
            fi = np.append(fi, point[1])

        sys.stdout = open("resultados.txt", "w")

        print("*****************")
        print(f'* g(x) = {g} *')
        print("*****************")

        print("")
        print("Punto a evaluar: x =", approxValue)
        print("")

        newton(g, approxValue, xi, fi)
        lagrange(g, approxValue, xi, fi)
        taylor(g, approxValue, gradoTaylor)

        sys.stdout.close()

        plt.show()

    except:
        errorLabel.grid(row=1, column=0, columnspan=2, padx=5, pady=5)


def createPointsFrame(numberOfPoints):
    pointsFrame.grid(row=0, column=0, padx=15, pady=15)
    pointsFrame.config(width=500, height=500)

    Label(pointsFrame, text="Metodos númericos", font=("Comic Sans MS", 25)).grid(
        row=0, column=0, columnspan=2, padx=0, pady=5)

    Label(pointsFrame, text="Función a aproximar: f(x)=", font=(
        "Comic Sans MS", 15)).grid(row=2, column=1, padx=5, pady=5)
    funcBox.grid(
        row=2, column=2, columnspan=2, padx=5, pady=5)
    funcBox.focus_set()

    Label(pointsFrame, text="Punto a aproximar: x=", font=(
        "Comic Sans MS", 15)).grid(row=3, column=1, padx=5, pady=5)
    valueBox.grid(
        row=3, column=2, columnspan=2, padx=5, pady=5)
        
    Label(pointsFrame, text="Grado maximo para taylor:", font=(
            "Comic Sans MS", 15)).grid(row=4, column=1, padx=5, pady=5)
    grado.grid(row=4, column=2, columnspan=2, padx=5, pady=5)

    Label(pointsFrame, text="", font=(
            "Comic Sans MS", 15)).grid(row=5, column=0, padx=5, pady=5)

    for i in range(numberOfPoints):
        Label(pointsFrame, text="x:", font=(
            "Comic Sans MS", 15)).grid(row=i+6, column=0, padx=5, pady=5)
        x = Entry(pointsFrame, font=("Comic Sans MS", 15))
        x.grid(row=i+6, column=1, padx=5, pady=5)

        Label(pointsFrame, text="y:", font=(
            "Comic Sans MS", 15)).grid(row=i+6, column=2, padx=5, pady=5)
        y = Entry(pointsFrame, font=("Comic Sans MS", 15))
        y.grid(row=i+6, column=3, padx=5, pady=5)

        points.append((x, y))

    root.bind("<Return>", calculate)

    Button(pointsFrame, text="Calcular", font=(
        "Comic Sans MS", 15), bg="LightSkyBlue1", command=calculate).grid(row=numberOfPoints + 8, column=2, columnspan=2, padx=5, pady=5)
