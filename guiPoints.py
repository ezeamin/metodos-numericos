from tkinter import *
from rootCreation import root

points = []
values = []

pointsFrame = Frame(root, width=500, height=500)
errorLabel = Label(pointsFrame, text="Error! Revise los campos", bg="yellow", font=(
    "Comic Sans MS", 15))

def calculate(e=None):
    try:
        for point in points:
            values.append((float(point[0].get()), float(point[1].get())))
        errorLabel.destroy()
    except:
        errorLabel.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    print(values)


def createPointsFrame(numberOfPoints):
    pointsFrame.grid(row=0, column=0, padx=15, pady=15)
    pointsFrame.config(width=500, height=500)

    root.bind("<Return>", calculate)

    Label(pointsFrame, text="Metodos númericos", font=("Comic Sans MS", 25)).grid(
        row=0, column=0, columnspan=2, padx=0, pady=5)

    for i in range(numberOfPoints):
        Label(pointsFrame, text="x:", font=(
            "Comic Sans MS", 15)).grid(row=i+3, column=0, padx=5, pady=5)
        x = Entry(pointsFrame, font=("Comic Sans MS", 15))
        x.grid(row=i+3, column=1, padx=5, pady=5)

        Label(pointsFrame, text="y:", font=(
            "Comic Sans MS", 15)).grid(row=i+3, column=2, padx=5, pady=5)
        y = Entry(pointsFrame, font=("Comic Sans MS", 15))
        y.grid(row=i+3, column=3, padx=5, pady=5)

        points.append((x, y))

    

    points[0][0].focus_set()
    Button(pointsFrame, text="Calcular", font=(
        "Comic Sans MS", 15), bg="LightSkyBlue1", command=calculate).grid(row=numberOfPoints + 3, column=2, columnspan=2, padx=5, pady=5)


