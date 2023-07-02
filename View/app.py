import customtkinter as ctk  # Importa el módulo customtkinter con el alias ctk
import tkinter as tk  # Importa el módulo tkinter con el alias tk
from tkinter import ttk
from PIL import ImageTk, Image  # Importa las clases ImageTk y Image del módulo PIL
from controller import Controller  # Importa la clase Controller del módulo controller


ctk.set_appearance_mode("System")  # Establece el modo de apariencia de ctk como "System"
ctk.set_default_color_theme("blue")  # Establece el tema de color predeterminado de ctk como "blue"

class AppWindow(ctk.CTk, tk.Frame, tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Agentes Inteligentes")  # Establece el título de la ventana como "App"
        self.geometry("1200x740")  # Establece las dimensiones de la ventana como 1200x800
        self.resizable(False, False)  # Deshabilita el redimensionamiento de la ventana
        self.update_idletasks()

        self.main_frame = ctk.CTkFrame(self, width=1000, height=200,fg_color="#5D6D7E")  # Crea un marco principal con las dimensiones 1200x650
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=1)
        self.main_frame.rowconfigure(1, weight=1)

        self.options_frame = ctk.CTkFrame(self.main_frame, width=1000, height=800,fg_color="#283747")  # Crea un marco de opciones con las dimensiones 1000x100
        self.options_frame.grid(row=0, column=0, sticky=tk.NSEW, padx=10, pady=10)  # Ubica el marco de opciones en la primera fila y columna del marco principal
        self.options_frame.columnconfigure(0, weight=1)

        self.label = ctk.CTkLabel(self.options_frame, text="AGENTES INTELIGENTES")  # Crea una etiqueta con el texto "AGENTES IA"
        self.label.grid(row=0, column=0, sticky=tk.NSEW, pady=5, padx=10)  # Ubica la etiqueta en la primera fila y columna del marco de opciones

        self.label_start = ctk.CTkLabel(self.options_frame, text="INICIO")  # Crea una etiqueta con el texto "Inicio"
        self.label_start.grid(row=0, column=1, sticky=tk.NSEW, pady=5, padx=15)  # Ubica la etiqueta en la segunda fila y columna del marco de opciones

        self.entry_start = ctk.CTkEntry(self.options_frame, placeholder_text="Ingrese el inicio",fg_color="#283747")  # Crea una entrada de texto con un texto de marcador "Ingrese el inicio"
        self.entry_start.grid(row=0, column=2, sticky=tk.NSEW, pady=5, padx=10)  # Ubica la entrada de texto en la tercera fila y columna del marco de opciones

        self.label_destination = ctk.CTkLabel(self.options_frame, text="DESTINO")  # Crea una etiqueta con el texto "Destino"
        self.label_destination.grid(row=0, column=3, sticky=tk.NSEW, pady=5, padx=10)  # Ubica la etiqueta en la cuarta fila y columna del marco de opciones

        self.entry_destination = ctk.CTkEntry(self.options_frame, placeholder_text="Ingrese el destino",fg_color="#283747")  # Crea una entrada de texto con un texto de marcador "Ingrese el destino"
        self.entry_destination.grid(row=0, column=4, sticky=tk.NSEW, pady=5, padx=10)  # Ubica la entrada de texto en la quinta fila y columna del marco de opciones

        self.send_agent_button = ctk.CTkButton(self.options_frame, text="BUSCAR", command=lambda: self.buscar_ruta())  # Crea un botón con el texto "Enviar" y un comando asociado para cuando se presione
        self.send_agent_button.grid(row=0, column=5, sticky=tk.NSEW, pady=5, padx=10)  # Ubica el botón en la sexta fila y columna del marco de opciones

        self.img_frame = ctk.CTkCanvas(self.main_frame, width=1000, height=630, bg="white")  # Crea un lienzo con las dimensiones 1200x550 y un color de fondo "#0E6063"
        self.img_frame.grid(row=1, column=0, columnspan=7, sticky=tk.NSEW, padx=10, pady=10)  # Ubica el lienzo en la segunda fila y columna del marco principal

        self.ima = Image.open("mapa.png")  # Abre la imagen "mapa.png"
        self.nuevaima = self.ima.resize(( 1200 , 645))  # Redimensiona la imagen a 1200x550
        self.gf = ImageTk.PhotoImage(self.nuevaima)  # Crea una instancia de ImageTk.PhotoImage a partir de la imagen redimensionada
        self.img_frame.create_image(0, 0, image=self.gf, anchor=tk.NW)  # Crea una imagen en el lienzo a partir de la imagen redimensionada

        self.main_frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)  # Empaqueta el marco principal dentro de la ventana

        self.clear_button = ctk.CTkButton(self.options_frame, text="LIMPIAR")
        self.clear_button.grid(row=0, column=7, sticky=tk.NSEW, pady=5, padx=5)

    def buscar_ruta(self):
        pass  # Función de marcador, no realiza ninguna operación

app = AppWindow() #Crea una instancia de la clase AppWindow
ctr = Controller(app)  # Crea una instancia del controlador, pasando la instancia de AppWindow como argumento
app.mainloop()  # Inicia el bucle principal de la aplicación
