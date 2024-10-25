# Color Trending:
# https://coolors.co/palettes/trending

import tkinter as tk
import tkinter.messagebox

window = tk.Tk()

window.title("My first GUI")
window.geometry("300x300")

def msgboxpopup():
    tkinter.messagebox.showinfo(title="Success", message="Name saved successfully.")

label = tk.Label(window, text="Name", bg="#ffb703")
label.pack()

entry = tk.Entry(window, width=20)
entry.pack()

button = tk.Button(window, text="Submit", command=msgboxpopup, bg="#00b4d8")
button.pack()

window.mainloop()