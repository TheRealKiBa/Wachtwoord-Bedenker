import random as rand
import tkinter as ttk
window = ttk.Tk()
window.title("Lekker gamblen")

def gamble():
    lot = rand.randint(0,100)
    print(lot)

button = ttk.Button(text="GAMBLE!", width=10, height=5, command=gamble)
button.pack(padx=200, pady=100)

label = ttk.Label(textvariable=lot, width=10, height=5, bg="green")
label.pack(padx=25, pady=25, anchor="center")

#run die window
window.mainloop()