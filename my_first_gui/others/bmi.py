import tkinter as tk
import tkinter.messagebox

def calculate():
    if weight.get() != "" and height.get() != "":
        result = int(weight.get()) / (int(height.get()) / 100) ** 2
        if 18.5 <= result < 24:
            feedback = "You are healthy."
        elif 24 <= result < 27:
            feedback = "You are overweight."
        elif 27 <= result < 30:
            feedback = "You are a little bit fat."
        elif 30 <= result < 35:
            feedback = "You are fat."
        elif result >= 35:
            feedback = "You are too fat."
        else:
            feedback = "You are too thin."
        tkinter.messagebox.showinfo(
            title="Success", 
            message="BMI calculated.\nYour BMI is " + str(result) + ".\n" + feedback
        )
    else:
        tkinter.messagebox.showerror(title="Error", message="Weight or height not given.")

root = tk.Tk()

root.title("BMI Calculator")
root.geometry("400x400")

title = tk.Label(root, text="BMI Calculator", font=("Arial", 35))
height_hint = tk.Label(root, text="Height(cm)")
height = tk.Entry(root, width=40)
weight_hint = tk.Label(root, text="Weight(kg)")
weight = tk.Entry(root, width=40)
submit = tk.Button(root, text="Submit", command=calculate)

title.pack()
height_hint.pack()
height.pack()
weight_hint.pack()
weight.pack()

submit.pack()

root.mainloop()
