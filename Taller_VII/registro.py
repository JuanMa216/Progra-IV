# ejemplo2_formulario.py
import tkinter as tk
from tkinter import messagebox, ttk

def registrar():
    nombre   = entry_nombre.get().strip()
    correo   = entry_correo.get().strip()
    edad     = entry_edad.get().strip()
    genero   = genero_var.get()
    terminos = terminos_var.get()

    #Validaciones
    if not nombre or not correo or not edad:
        messagebox.showwarning("Campos vacíos", "Por favor completa todos los campos")
        return
    if "@" not in correo:
        messagebox.showerror("Correo inválido", "Ingresa un correo válido")
        return
    if not edad.isdigit() or not (1 <= int(edad) <= 120):
        messagebox.showerror("Edad inválida", "Ingresa una edad entre 1 y 120")
        return
    if not terminos:
        messagebox.showwarning("Términos", "Debes aceptar los términos y condiciones")
        return

    #Mostrar resumen
    resumen = (
        f"✔ Registro exitoso\n\n"
        f"Nombre: {nombre}\n"
        f"Correo: {correo}\n"
        f"Edad:   {edad}\n"
        f"Género: {genero}"
    )
    messagebox.showinfo("Registro completado", resumen)
    limpiar()

def limpiar():
    entry_nombre.delete(0, tk.END)
    entry_correo.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    genero_var.set("Prefiero no decir")
    terminos_var.set(False)

#Ventana principal
ventana = tk.Tk()
ventana.title("Formulario de Registro")
ventana.geometry("360x400")
ventana.resizable(False, False)

tk.Label(ventana, text="Formulario de Registro", font=("Arial", 15, "bold")).pack(pady=12)

#Función auxiliar para filas de campo
def campo(etiqueta):
    tk.Label(ventana, text=etiqueta, anchor="w").pack(fill="x", padx=30)
    entry = tk.Entry(ventana, width=35)
    entry.pack(pady=3)
    return entry

entry_nombre = campo("Nombre completo:")
entry_correo = campo("Correo electrónico:")
entry_edad   = campo("Edad:")

tk.Label(ventana, text="Género:", anchor="w").pack(fill="x", padx=30)
genero_var = tk.StringVar(value="Prefiero no decir")
combo_genero = ttk.Combobox(ventana, textvariable=genero_var, state="readonly", width=32,
                             values=["Masculino", "Femenino", "Otro", "Prefiero no decir"])
combo_genero.pack(pady=3)

terminos_var = tk.BooleanVar()
tk.Checkbutton(ventana, text="Acepto los términos y condiciones", variable=terminos_var).pack(pady=8)

#Botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=6)
tk.Button(frame_botones, text="Registrar", command=registrar, bg="#2196F3", fg="white", width=12).pack(side=tk.LEFT, padx=6)
tk.Button(frame_botones, text="Limpiar",   command=limpiar,   bg="#9E9E9E", fg="white", width=12).pack(side=tk.LEFT, padx=6)

ventana.mainloop()