# Proyecto-1-Sistemas-Operativos   
#  COMPONENTES DE VISUALIZACIÓN 
# """Módulo de visualización de estado del sistema.
#Contiene los widgets para mostrar:
#- Procesos en ejecución
#- Procesos en cola de espera


# Lista de procesos en ejecución
ctk.CTkLabel(
    ventana,
    text="🟢 Procesos en ejecución",
    font=ctk.CTkFont(weight="bold")
).place(x=50, y=200)
"""Widget que muestra el título de la sección de procesos activos.
- Uso del emoji 🟢 para indicar estado activo
- Fuente en negrita para mejor jerarquía visual
- Posicionamiento absoluto en coordenadas (50, 200)
"""

lista_procesos = ctk.CTkTextbox(
    ventana,
    width=300,
    height=150,
    font=("Courier New", 12)
)
lista_procesos.place(x=50, y=230)
lista_procesos.configure(state="disabled")  # Solo lectura


# Cola de espera
ctk.CTkLabel(
    ventana,
    text="🕓 Cola de espera",
    font=ctk.CTkFont(weight="bold")
).place(x=420, y=200)
