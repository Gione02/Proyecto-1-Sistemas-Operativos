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
