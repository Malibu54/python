import tkinter as tk
from tkinter import messagebox
from openpyxl import Workbook
import re


# Crear libro de Excel
wb = Workbook()
ws = wb.active
ws.append(["Nombre","Edad","Email","Telefono","Direccion"])
#wb.save('datos.xlsx')

def guardar_datos():
   Nombre = entry_Nombre.get()
   Edad = entry_Edad.get()
   Email = entry_Email.get()
   Telefono = entry_Telefono.get()
   Direccion = entry_Direccion.get()

   if not Nombre or not Edad or not Email or not Telefono or not Direccion:
    messagebox.showwarning(title="Advertencia", message="Todos los campos son obligatorios")
    return
   try:
    Edad = int(Edad)
    Telefono = int (Telefono)
   except ValueError:
    messagebox.showwarning(title="Advertencia", message="Edad y Telefono deben ser numericos")
    return
   
   #Validar formado de Email
   if not re.match(pattern=r"[^@]+@[^@]+\.[^@]", Email):
    messagebox.showwarning(title="Advertencia", message="El correo electrónico no es válido")
    return

    ''' 1) Obtener los datos ingresados
    2) Validar que no existan campos vacios estableciendo todos los campos como obligatorios
    3) Validar que edad y telefono sean datos de tipo numerico
    4)Guardar en col 0 [Nombre]
        Guardar en col 1 [Edad]
        Guardar en col 2 [Email]
        Guardar en col 3 [Teléfono]
        Guardar en col 4 [Direccion]
        En la fila siguiente a la última registrada.'''


#Estilos
root = tk.Tk()
root.title("Formulario de Entrada de datos")
root.configure(bg='#4b6587')
label_style = {"bg": '#4B6578', 'fg': "white"}
entry_style = {"bg": '#D3D3D3', 'fg': "black"}

#Columna {Nombre}
label_Nombre = tk.Label(root, text="Nombre", **label_style)
label_Nombre.grid (row=0, column=0, padx=10, pady=5)
entry_Nombre= tk.Entry(root, **entry_style)
entry_Nombre.grid(row=0, column=1, padx=10, pady=5)

#Columna {Edad}
label_Edad = tk.Label(root, text="Edad", **label_style)
label_Edad.grid (row=1, column=0, padx=10, pady=5)
entry_Edad= tk.Entry(root, **entry_style)
entry_Edad.grid(row=1, column=1, padx=10, pady=5)

#Columna {Email}
label_Email = tk.Label(root, text="Email", **label_style)
label_Email.grid (row=2, column=0, padx=10, pady=5)
entry_Email= tk.Entry(root, **entry_style)
entry_Email.grid(row=2, column=1, padx=10, pady=5)

#Columna {Telefono}
label_Telefono = tk.Label(root, text="Telefono", **label_style)
label_Telefono.grid (row=3, column=0, padx=10, pady=5)
entry_Telefono= tk.Entry(root, **entry_style)
entry_Telefono.grid(row=3, column=1, padx=10, pady=5)

#Columna {Dirección}
label_Direccion = tk.Label(root, text="Direccion", **label_style)
label_Direccion.grid (row=4, column=0, padx=10, pady=5)
entry_Direccion= tk.Entry(root, **entry_style)
entry_Direccion.grid(row=4, column=1, padx=10, pady=5)

boton_guardar = tk.Button(root, text="Guardar", command=guardar_datos, bg='#6d8299', fg='white', width=30)
boton_guardar.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
root.mainloop()


