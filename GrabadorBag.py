import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import pyrealsense2 as rs
import datetime
import os
import time
class GrabadorBag:
    def __init__(self, duracion=15):
        self.config = rs.config()
        self.duracion = duracion
        self.configurar_streams()
        self.grabando = False
        self.pipeline_activa = False
        self.pipeline = None

    def configurar_streams(self):
        self.config.enable_stream(rs.stream.depth, 848, 480, rs.format.z16, 30)
        self.config.enable_stream(rs.stream.color, 848, 480, rs.format.bgr8, 30)

    def generar_nombre_archivo_en_carpeta_seleccionada(self, carpeta_destino):
        nombre_archivo = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".bag"
        return os.path.join(carpeta_destino, nombre_archivo)

    def grabar_segmento(self, carpeta_destino):
        nombre_archivo = self.generar_nombre_archivo_en_carpeta_seleccionada(carpeta_destino)
        self.config.enable_record_to_file(nombre_archivo)
        self.pipeline = rs.pipeline()
        self.pipeline.start(self.config)
        self.pipeline_activa = True
        print(f"Grabación iniciada, guardando en {nombre_archivo}.")

        inicio = time.time()
        while time.time() - inicio < self.duracion and self.grabando:
            time.sleep(0.01)

        self.detener_pipeline()

    def detener_pipeline(self):
        if self.pipeline_activa and self.pipeline:
            self.pipeline.stop()
            self.pipeline_activa = False
            print("Pipeline detenido correctamente.")

    def ejecutar_grabacion(self, carpeta_destino):
        self.grabando = True
        while self.grabando:
            self.grabar_segmento(carpeta_destino)

    def detener_grabacion(self):
        self.grabando = False
        self.detener_pipeline()