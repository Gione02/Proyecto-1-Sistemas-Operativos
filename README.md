     SIMULADOR DE GESTIÓN DE MEMORIA

Descripción del Proyecto
Sistema que **simula la administración de memoria RAM** en un sistema operativo, mostrando:  
- Asignación de memoria a procesos  
- Manejo de colas de espera  
- Visualización en tiempo real del estado de la memoria  
- Interfaz gráfica intuitiva  

Objetivos
- Demostrar cómo los SO gestionan memoria limitada
- Visualizar el concepto de colas de espera
- Servir como herramienta educativa

       Tecnologías Implementadas

Lenguaje de Programación
- Python 3.10+: Lenguaje base del proyecto, elegido por su sintaxis clara y amplia disponibilidad de librerías para desarrollo de sistemas.

Interfaz Gráfica
- CustomTkinter: Versión moderna de Tkinter que permite crear interfaces visuales atractivas con widgets personalizables y temas oscuros/claros.

Manejo de Procesos
- Threading: Módulo nativo de Python utilizado para ejecutar múltiples procesos en paralelo sin bloquear la interfaz gráfica principal.

Procesamiento de Imágenes
- Pillow (PIL): Usado para cargar y manipular imágenes de fondo en la interfaz gráfica.

        Requerimientos técnicos 
customtkinter == 5.2.1   # Interfaz gráfica moderna
pillow == 10.0.0         # Manejo de imágenes

     Instrucciones de Instalación

1. Requisitos Previos
- Python 3.10 o superior  
- Gestor de paquetes PIP  

2. Instalación
Ejecutar
 Clonar repositorio
git clone https://github.com/tu-usuario/simulador-memoria.git

Entrar al directorio
cd simulador-memoria

Instalar dependencias
pip install -r requirements.txt

3. Ejecución
Ejecutar python main.py

          Instrucciones de Uso
1. Ingresar datos del proceso:  
   - Nombre (opcional)  
   - Memoria requerida (MB)  
   - Tiempo de ejecución (segundos)  

2. Botones:  
   - `Agregar Proceso`: Envía el proceso a memoria o cola de espera  

3. Áreas de visualización:  
   - Procesos activos: Muestra PID, memoria usada y tiempo restante  
   - Cola de espera: Procesos pendientes por memoria

           Estructura del Código
```markdown
simulador-memoria/
├── main.py                # Lógica principal e interfaz
├── requirements.txt       # Dependencias
├── README.md              # Este archivo
└── img/                   # Assets visuales
    ├── screenshot.png     # Captura de pantalla
    └── GEm.png            # Imagen de fondo (opcional)
