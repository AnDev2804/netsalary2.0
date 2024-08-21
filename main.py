import tkinter as tk
from tkinter import ttk
from conexion import conexion
from datetime import date

# Variables que irán a la clase Conexion
host = "localhost"
user = "root"
password = ""
database = "pyexamen"

# Crear nueva conexion
con = conexion(host, user, password, database)
db = con.conectar()
cursor = db.cursor()

# Cargar las tablas de Cargo, Grado academico, Pais y parentezco
cargos = con.cargar_datos_cargo()  # Supongo que esta es una lista
gradAcad = con.cargar_datos_gradAcad()  # Supongo que esta es una lista
pais = con.cargar_datos_pais()
parentezco = con.cargar_datos_parentezco()

# Función que maneja el comando del botón submit_button
def consult_sueldo():
    # Limpiar todos los widgets existentes para evitar apilar los datos
    for widget in window.winfo_children():
        if isinstance(widget, tk.Label) and widget != label1 and widget != id_label and widget != id_entry and widget != submit_button:
            widget.destroy()

    id = id_entry.get()
    data_pers = con.consult_personal_data(id)
    data_lab = con.consult_laboral_data(id)
    data_fam = con.consult_familiar_data(id)
    data_acad = con.consult_acad_data(id)

    # Cargar datos personales
    sexo = data_pers[1]
    fnac = data_pers[2]
    names = data_pers[3]
    surnames = data_pers[4]
    pnac = data_pers[5]

    # Cargar datos laborales
    codCargo = data_lab[1]
    fcontrato = data_lab[2]
    paisRes = data_lab[3]
    sBase = data_lab[4]
    sTotal = sBase

    # Cargar datos academicos
    gradoAcad = data_acad[1]

    label_info = tk.Label(window, text="El empleado: " + names + " " + surnames + "\n" + "Tiene un sueldo base de: " + str(sBase))
    label_info.pack(padx=5, pady=5)

    # Comenzar a calcular
    factual = date.today()
    
    # Calcular edad
    edad = factual.year - fnac.year
    if factual < fnac:
        edad -= 1
    
    # Calcular antigüedad
    ant = factual.year - fcontrato.year
    if factual < fcontrato:
        ant -= 1
    
    # Incentivo especial de 15% para empleados mayores de 50 años
    if edad >= 50:
        sTotal += (sBase * 0.15)
        label_1 = tk.Label(window, text="Como es mayor a 50 años se le suma un 15%.\n Sueldo total actual: " + str(sTotal))
        label_1.pack(padx=5, pady=5)

    # Incentivo por antigüedad de 5% por cada 4 años de servicio
    if ant >= 4:
        sTotal += (sBase * 0.05 * (ant // 4))
        label_2 = tk.Label(window, text="Por cada 4 años de antigüedad se le sumará un 5%\n Sueldo total actual: " + str(sTotal))
        label_2.pack(padx=5, pady=5)

    # Incentivos por cargo
    cargo_incentivos = {1: 0.1, 2: 0.15, 3: 0.2, 4: 0.25, 5: 0.35}
    if codCargo in cargo_incentivos:
        # Accedemos a la lista `cargos` por índice, restando 1 si los índices son 0-basados.
        descripcion_cargo = cargos[codCargo - 1] if 0 <= codCargo - 1 < len(cargos) else 'Desconocido'
        sTotal += (sBase * cargo_incentivos[codCargo])
        label_cargo = tk.Label(window, text=f"Por tener el cargo: {descripcion_cargo} se le sumará un {cargo_incentivos[codCargo] * 100}%\n Sueldo total actual: {sTotal}")
        label_cargo.pack(padx=5, pady=5)
    
    # Incentivos por grado académico
    acad_incentivos = {3: 2000, 4: 2000, 5: 3500, 6: 7500, 7: 9000}
    if gradoAcad in acad_incentivos:
        descripcion_grado = gradAcad[gradoAcad - 1] if 0 <= gradoAcad - 1 < len(gradAcad) else f"Código {gradoAcad}"
        sTotal += acad_incentivos[gradoAcad]
        label_acad = tk.Label(window, text=f"Por tener el título: {descripcion_grado} se le sumarán +{acad_incentivos[gradoAcad]}\n Sueldo total actual: {sTotal}")
        label_acad.pack(padx=5, pady=5)

# Formulario

window = tk.Tk()
window.geometry("800x600")
window.resizable(False, False)

label1 = tk.Label(window, text="Sistema de Consulta de Sueldos Totales")
id_label = tk.Label(window, text="Ingrese el ID del empleado")
id_entry = tk.Entry(window)
submit_button = tk.Button(window, padx="5", pady="5", text="Consultar", command=consult_sueldo)

label1.pack(pady=20)
id_label.pack(pady=10)
id_entry.pack(pady=10)
submit_button.pack(pady=20)

window.mainloop()
