import tkinter as tk
from tkinter import filedialog, messagebox
import threading



class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Grabador de Datos RealSense")
        self.setup_gui()

    def setup_gui(self):
        self.label_carpeta = tk.Label(self.root, text="Carpeta de destino no seleccionada")
        self.label_carpeta.pack(pady=5)

        boton_seleccionar_carpeta = tk.Button(self.root, text="Seleccionar Carpeta", command=self.seleccionar_carpeta)
        boton_seleccionar_carpeta.pack(pady=5)

        boton_grabar = tk.Button(self.root, text="Iniciar Grabación", command=self.iniciar_grabacion)
        boton_grabar.pack(pady=5)

        boton_detener_grabacion = tk.Button(self.root, text="Detener Grabación y Salir", command=self.detener_grabacion_y_salir)
        boton_detener_grabacion.pack(pady=5)

    def seleccionar_carpeta(self):
        carpeta_destino = filedialog.askdirectory()
        if carpeta_destino:
            self.carpeta_destino = carpeta_destino
            self.label_carpeta.config(text="Carpeta de destino seleccionada: " + self.carpeta_destino)

    def iniciar_grabacion(self):
        if not hasattr(self, 'carpeta_destino'):
            messagebox.showerror("Error", "Por favor selecciona una carpeta de destino.")
            return
        if not hasattr(self, 'grabador'):
            from GrabadorBag import GrabadorBag
            self.grabador = GrabadorBag(15)
        threading.Thread(target=self.grabador.ejecutar_grabacion, args=(self.carpeta_destino,), daemon=True).start()

    def detener_grabacion_y_salir(self):
        if hasattr(self, 'grabador'):
            self.grabador.detener_grabacion()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()