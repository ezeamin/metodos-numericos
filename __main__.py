from tkinter import *

from guiPoints import createPointsFrame
from rootCreation import root

# -----------------------------

mainFrame = Frame(root, width=500, height=500)

mainFrame.grid(row=0, column=0, padx=15, pady=15)

mainFrame.config(width=500, height=500)

# -----------------------------

Label(mainFrame, text="Metodos númericos", font=("Comic Sans MS", 25)).grid(
    row=2, column=0, padx=0, pady=5)

# -----------------------------


numberOfPointsEntry = Entry(mainFrame, font=("Comic Sans MS", 15))
numberOfPointsEntry.grid(row=5, column=1, padx=5, pady=5)
numberOfPointsEntry.focus_set()

Label(mainFrame, text="Cantidad de puntos:", font=(
    "Comic Sans MS", 15)).grid(row=5, column=0, padx=0, pady=5)

# -----------------------------

errorLabel = Label(mainFrame, text="Error! Revise los campos", bg="yellow", font=(
    "Comic Sans MS", 15))


def getPoints(e=None):
    try:
        numberOfPoints = int(numberOfPointsEntry.get())
        if (numberOfPoints > 30 or numberOfPoints < 2):
            raise Exception
        errorLabel.destroy()
        mainFrame.destroy()
        
        createPointsFrame(numberOfPoints)
    except:
        errorLabel.grid(row=4, column=0, columnspan=2, padx=5, pady=5)


Label(mainFrame, text="*Los grados de los polinomios de LaGrange y Newton", font=(
    "Comic Sans MS", 10)).grid(row=6, column=0, padx=0, pady=0)
Label(mainFrame, text="dependeran de la cantidad de puntos ingresados", font=(
    "Comic Sans MS", 10)).grid(row=7, column=0, padx=0, pady=0)

Button(mainFrame, text="Calcular", font=(
    "Comic Sans MS", 15), bg="LightSkyBlue1", command=getPoints).grid(row=8, column=0, columnspan=2, padx=5, pady=5)

root.bind("<Return>", getPoints)

# -----------------------------

root.mainloop()
