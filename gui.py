from tkinter import *

root = Tk()

root.title("Metodos númericos")

root.resizable(False, False)

# -----------------------------

myFrame = Frame(root, width=500, height=500)

myFrame.grid(row=0, column=0, padx=15, pady=15)

myFrame.config(width=500, height=500)

# -----------------------------

Label(myFrame, text="Metodos númericos", font=("Comic Sans MS", 25)).grid(
    row=2, column=0, padx=0, pady=5)

# -----------------------------


numberOfPointsEntry = Entry(myFrame, font=("Comic Sans MS", 15))
numberOfPointsEntry.grid(row=5, column=1, padx=5, pady=5)
numberOfPointsEntry.focus_set()

Label(myFrame, text="Cantidad de puntos:", font=(
    "Comic Sans MS", 15)).grid(row=5, column=0, padx=5, pady=5)


# -----------------------------

def calculate(e=None):
    try:
        numberOfPoints = int(numberOfPointsEntry.get())
        print("Cantidad de puntos:",numberOfPoints)
    except:
        print("Error de campos")


buttonSubmit = Button(myFrame, text="Calcular", font=(
    "Comic Sans MS", 15), bg="LightSkyBlue1", command=calculate)
buttonSubmit.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

root.bind("<Return>", calculate)

root.mainloop()
