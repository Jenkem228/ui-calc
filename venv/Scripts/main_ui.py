import tkinter as tk
import math
from tkinter import messagebox

def calculate():
    try:
        result = eval(entry.get())
        output.config(state="normal")
        output.delete(1.0, tk.END)
        output.insert(tk.END, str(result))
        output.config(state="disabled")
    except Exception as e:
        output.config(state="normal")
        output.delete(1.0, tk.END)
        output.insert(tk.END, "Ошибка: " + str(e))
        output.config(state="disabled")

def clear():
    entry.delete(0, tk.END)

def sin():
    entry.insert(tk.END, "math.sin(")

def negate():
    entry.insert(tk.END, "-")

def on_closing():
    if messagebox.askokcancel("Выход", "Вы уверены, что хотите выйти?"):
        window.destroy()

window = tk.Tk()
window.title("Калькулятор")
window.protocol("WM_DELETE_WINDOW", on_closing)

entry = tk.Entry(window, width=30)
entry.grid(row=0, column=0,sticky="ew", columnspan=2)

output = tk.Text(window, state="disabled", width=30, height=1)
output.grid(row=1, column=0, sticky="ew")

clear_button = tk.Button(window, text="Стереть", command=clear, bg="blue", fg="white", width=10)
clear_button.grid(row=2, column=1)

sin_button = tk.Button(window, text="sin", command=sin, bg="blue", fg="white", width=10)
sin_button.grid(row=3, column=1)

negate_button = tk.Button(window, text="-", command=negate, bg="blue", fg="white", width=10)
negate_button.grid(row=4, column=1)

calculate_button = tk.Button(window, text="Вычислить", command=calculate, bg="blue", fg="white", width=10)
calculate_button.grid(row=5, column=1)

window.mainloop()
