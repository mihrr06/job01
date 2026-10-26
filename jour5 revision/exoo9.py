import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Ma calculatrice")
fenetre.resizable(False, False)

ecran = tk.Entry(fenetre, font=("Arial", 24), justify="right", width=15)
ecran.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def cliquer(touche):
    if touche == "=":
        try:
            resultat = eval(ecran.get())
            ecran.delete(0, tk.END)
            ecran.insert(tk.END, str(resultat))
        except Exception:
            ecran.delete(0, tk.END)
            ecran.insert(tk.END, "Erreur")
    elif touche == "C":
        ecran.delete(0, tk.END)
    else:
        ecran.insert(tk.END, touche)

touches = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", ".", "+"],
    ["="],
]

for ligne, rangee in enumerate(touches, start=1):
    for colonne, touche in enumerate(rangee):
        bouton = tk.Button(
            fenetre,
            text=touche,
            font=("Arial", 18),
            width=5,
            height=2,
            command=lambda t=touche: cliquer(t),
        )
        bouton.grid(row=ligne, column=colonne, padx=3, pady=3)

fenetre.mainloop()