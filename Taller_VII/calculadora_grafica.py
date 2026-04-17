# ejemplo1_calculadora.py
import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operacion = operacion_var.get()

        if operacion == "+":
            resultado = num1 + num2
        elif operacion == "-":
            resultado = num1 - num2
        elif operacion == "*":
            resultado = num1 * num2
        elif operacion == "/":
            if num2 == 0:
                messagebox.showerror("Error", "No se puede dividir entre cero")
                return
            resultado = num1 / num2

        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Ingresa números válidos")

def limpiar():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    label_resultado.config(text="Resultado: ")

# ── Ventana principal ──────────────────────────────────────────
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("320x280")
ventana.resizable(False, False)

# ── Widgets ────────────────────────────────────────────────────
tk.Label(ventana, text="Calculadora", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(ventana, text="Número 1:").pack()
entry_num1 = tk.Entry(ventana, width=20)
entry_num1.pack(pady=4)

tk.Label(ventana, text="Número 2:").pack()
entry_num2 = tk.Entry(ventana, width=20)
entry_num2.pack(pady=4)

tk.Label(ventana, text="Operación:").pack()
operacion_var = tk.StringVar(value="+")
frame_ops = tk.Frame(ventana)
frame_ops.pack(pady=4)
for op in ["+", "-", "*", "/"]:
    tk.Radiobutton(frame_ops, text=op, variable=operacion_var, value=op).pack(side=tk.LEFT, padx=8)

frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)
tk.Button(frame_botones, text="Calcular", command=calcular, bg="#4CAF50", fg="white", width=10).pack(side=tk.LEFT, padx=5)
tk.Button(frame_botones, text="Limpiar",  command=limpiar,  bg="#f44336", fg="white", width=10).pack(side=tk.LEFT, padx=5)

label_resultado = tk.Label(ventana, text="Resultado: ", font=("Arial", 12))
label_resultado.pack(pady=6)

ventana.mainloop()