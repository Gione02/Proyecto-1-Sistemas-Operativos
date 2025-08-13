# main.py
"""
SIMULADOR DE GESTIÓN DE MEMORIA
--------------------------------
Este programa simula la administración de memoria RAM en un sistema operativo,
mostrando cómo se asignan procesos y se maneja la cola de espera cuando la memoria es insuficiente.

Desarrollado usando:
- CustomTkinter para la interfaz gráfica
- Threading para ejecución paralela de procesos
- PIL para manejo de imágenes (opcional)

#  MÓDULOS IMPORTADOS 
import customtkinter as ctk  # Para la interfaz gráfica moderna
import threading             # Para ejecutar procesos en segundo plano
import time                  # Para simular el tiempo de ejecución de procesos
from PIL import Image        # Para manejar imágenes de fondo (opcional)

# CONFIGURACIÓN INICIAL 
# Configuración de la interfaz gráfica
ctk.set_appearance_mode("dark")          # Tema oscuro
ctk.set_default_color_theme("blue")      # Color principal azul

# VARIABLES GLOBALES 
RAM_TOTAL = 1024           # Memoria RAM total disponible en MB (valor simulado)
ram_disponible = RAM_TOTAL # Memoria RAM actualmente disponible
procesos_activos = []      # Lista de procesos actualmente en ejecución
cola_espera = []           # Procesos en espera por falta de memoria
pid_counter = 1            # Contador para asignar IDs únicos a los procesos

#CLASE PROCESO 
class Proceso:
    
    Representa un proceso en el sistema operativo.
    
    Atributos:
        pid (int): Identificador único del proceso
        nombre (str): Nombre descriptivo del proceso
        memoria (int): Cantidad de memoria RAM requerida (en MB)
        duracion (int): Tiempo de ejecución del proceso (en segundos)
   
    def __init__(self, pid, nombre, memoria, duracion):
        
        Inicializa un nuevo proceso.
        
        Args:
            pid: Identificador único (entero)
            nombre: Nombre del proceso (str)
            memoria: Memoria requerida en MB (entero positivo)
            duracion: Tiempo de ejecución en segundos (entero positivo)
       
        self.pid = pid          # ID del proceso (Process ID)
        self.nombre = nombre    # Nombre descriptivo (ej: "Navegador")
        self.memoria = memoria  # Memoria necesaria para ejecución
        self.duracion = duracion # Duración estimada de ejecución

# FUNCIONES DE PROCESOS #(PARTE 2 ERICK RONALDIÑO APEN PEREZ)
def crear_proceso(nombre, memoria, duracion):
    # Crea y retorna una nueva instancia de Proceso.
    
    # Args:
     #   nombre (str): Nombre descriptivo del proceso. Si está vacío, se autogenera.
     #   memoria (int): Memoria requerida en MB (debe ser positivo).
     #   duracion (int): Tiempo de ejecución en segundos (debe ser positivo).
        
    #Returns:
    #    Proceso: Nueva instancia configurada.

   # """Crea un nuevo proceso con nombre, memoria y duración."""
    global pid_counter
    if not nombre:
        nombre = f"Proceso{pid_counter}"  # Nombre por defecto si está vacío
    p = Proceso(pid_counter, nombre, memoria, duracion)
    pid_counter += 1
    return p

def ejecutar_proceso(proceso):
   #  Intenta ejecutar un proceso si hay suficiente memoria disponible.
   # Si no hay memoria, lo coloca en la cola de espera.
    
   # Args:
    #    proceso (Proceso): Proceso a ejecutar.
        
    # Side Effects:
    #    - Modifica ram_disponible
    #    - Actualiza procesos_activos o cola_espera
    #   - Inicia un hilo para finalización automática
    #   - Actualiza la interfaz gráfica

    #"""Intenta ejecutar un proceso si hay memoria disponible."""
    global ram_disponible
    if proceso.memoria <= ram_disponible:
        # Asignar memoria y agregar a procesos activos
        ram_disponible -= proceso.memoria
        procesos_activos.append(proceso)
        actualizar_estado()
        # Ejecutar en un hilo para no bloquear la interfaz
        threading.Thread(target=finalizar_proceso, args=(proceso,)).start()
    else:
        # Insuficiente memoria -> enviar a cola de espera
        cola_espera.append(proceso)
        actualizar_estado()

def finalizar_proceso(proceso):
   #Finaliza un proceso después de su tiempo de ejecución y libera recursos.
   #
   #Args:
   #    proceso (Proceso): Proceso a finalizar.
        
   #Workflow:
   #    1. Espera el tiempo de duración del proceso (simulado con sleep)
   #    2. Libera la memoria ocupada
   #    3. Remueve el proceso de la lista de activos
   #   4. Revisa si procesos en espera pueden ejecutarse
   #    5. Actualiza la interfaz
   
   #"""Finaliza un proceso después de su tiempo de ejecución."""

    time.sleep(proceso.duracion) # Simular tiempo de ejecución
    global ram_disponible
    procesos_activos.remove(proceso)
    ram_disponible += proceso.memoria # Liberar memoria
    revisar_cola()      # Verificar si procesos en espera pueden ejecutarse
    actualizar_estado() # Reflejar cambios en la GUI

#333333333333333333333333333333333333

def revisar_cola():
   # """Revisa la cola de espera y ejecuta procesos si hay memoria."""
   #Flujo de operación:
     #  1. Itera sobre una copia de la cola de espera (para evitar modificaciones durante la iteración)
     #  2. Para cada proceso verifica si hay suficiente RAM disponible
     #  3. Si hay memoria:
     #       - Remueve el proceso de la cola de espera
     #      - Lo envía a ejecución mediante ejecutar_proceso()
    
    for proceso in cola_espera[:]:  # Iterar sobre una copia de la lista
        if proceso.memoria <= ram_disponible:
            cola_espera.remove(proceso)
            ejecutar_proceso(proceso)

def actualizar_estado():

   # Actualiza todos los elementos de la interfaz gráfica con el estado actual del sistema.
    
   # Componentes actualizados:
   #     1. Label de RAM disponible
   #     2. Lista de procesos en ejecución
   #     3. Lista de procesos en cola de espera
        
   # Efectos secundarios:
   #     - Modifica el estado de los widgets CTkTextbox (normal/disabled)
   #     - Actualiza el contenido de los textos
   # """Actualiza la interfaz con el estado actual."""

    estado_label.configure(text=f"RAM disponible: {ram_disponible} MB")
    
    # Actualizar lista de procesos en ejecución
    lista_procesos.configure(state="normal")
    lista_procesos.delete("1.0", "end")
    for p in procesos_activos:
        lista_procesos.insert("end", f"{p.nombre} | PID: {p.pid} | {p.memoria}MB | {p.duracion}s\n")
    lista_procesos.configure(state="disabled")
    
    # Actualizar cola de espera
    lista_espera.configure(state="normal")
    lista_espera.delete("1.0", "end")
    for p in cola_espera:
        lista_espera.insert("end", f"{p.nombre} | PID: {p.pid} | {p.memoria}MB\n")
    lista_espera.configure(state="disabled")

def agregar_proceso():
    #"""Agrega un nuevo proceso desde la interfaz."""
   # Flujo:
   #     1. Obtiene valores de los campos de entrada
   #     2. Valida que los valores sean positivos
   #     3. Crea un nuevo proceso
   #     4. Intenta ejecutarlo
   #     5. Limpia los campos de entrada
        
   # Manejo de errores:
   #     - ValueError: Si memoria o duración no son números positivos
   #     - Muestra mensaje de error en CTkMessagebox
        
   # Campos afectados:
   #     - entry_nombre (str)
   #     - entry_memoria (int)
   #     - entry_duracion (int)
    try: # Obtener valores de la interfaz
        nombre = entry_nombre.get()
        memoria = int(entry_memoria.get())
        duracion = int(entry_duracion.get())

        if memoria <= 0 or duracion <= 0: # Validación de entradas
            raise ValueError("Valores deben ser positivos")

        nuevo = crear_proceso(nombre, memoria, duracion)  # Creación y ejecución del proceso
        ejecutar_proceso(nuevo)

        # Limpiar campos después de agregar
        entry_nombre.delete(0, "end")
        entry_memoria.delete(0, "end")
        entry_duracion.delete(0, "end")

    except ValueError:  # Mostrar error en cuadro de diálogo
        ctk.CTkMessagebox(title="Error", message="Memoria y duración deben ser números positivos")

#termina parte 33333333333333333333333333333333333333333333333333333333


# 444444444

   #  INTERFAZ GRÁFICA 

#   Módulo de interfaz gráfica usando CustomTkinter.
#Contiene la configuración de ventana principal y todos los widgets.

# Configuración de ventana principal
ventana = ctk.CTk() # Crear instancia de ventana principal
ventana.title("Simulador de Gestión de Memoria") # Título de la ventana
ventana.geometry("800x500")  # Dimensiones (ancho x alto)

# Fondo opcional (manejo de errores si no hay imagen)
try: # Cargar imagen de fondo si existe
    imagen_fondo = ctk.CTkImage(light_image=Image.open("GEm.png"), size=(800, 500)) # Ruta de la imagen y tamaño
    fondo = ctk.CTkLabel(ventana, image=imagen_fondo, text="")  # Crear label con la imagen
    fondo.place(x=0, y=0, relwidth=1, relheight=1)
except:
    pass  # Continuar sin fondo si no se encuentra la imagen

# Campos de entrada

# Campo para nombre del proceso
entry_nombre = ctk.CTkEntry(ventana, placeholder_text="Nombre del Proceso", width=200)
entry_nombre.place(x=50, y=30)
# Campo para memoria requerida
entry_memoria = ctk.CTkEntry(ventana, placeholder_text="Memoria (MB)", width=200)
entry_memoria.place(x=50, y=70)
# Campo para duración del proceso
entry_duracion = ctk.CTkEntry(ventana, placeholder_text="Duración (s)", width=200)
entry_duracion.place(x=50, y=110)

# Botón para agregar procesos
agregar_btn = ctk.CTkButton(
    ventana,
    text="Agregar Proceso",
    command=agregar_proceso,
    width=150,
    fg_color="#4CAF50",  # Verde
    hover_color="#45A049"
)
agregar_btn.place(x=600, y=60)

# Etiqueta de estado de RAM
estado_label = ctk.CTkLabel(
    ventana,
    text=f"RAM disponible: {RAM_TOTAL} MB",
    font=ctk.CTkFont(size=14, weight="bold")
)
estado_label.place(x=50, y=160)

# FIN 444444444
        
