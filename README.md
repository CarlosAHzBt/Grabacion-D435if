# Aplicación de Grabación RealSense D435i

## Descripción
Este proyecto proporciona una aplicación para grabar videos usando la cámara Intel RealSense D435i. La aplicación permite al usuario seleccionar una carpeta de destino, iniciar y detener la grabación, y cerrar la aplicación mediante una interfaz gráfica de usuario (GUI).
Cada video tiene una duracion de 15 Segundos y se generaran mientras se inicie la grabacion
## Características
- **Selección de Carpeta**: Permite al usuario elegir la carpeta donde se guardarán los archivos `.bag`.
- **Control de Grabación**: Iniciar y detener la grabación con un clic.
- **Interfaz de Usuario Amigable**: Interfaz simple que no requiere conocimientos previos de programación o del hardware.
## EL EJECUTABLE DE LA APLICACION SE ENCUENTRA EN LA RAMA EXE, 
En la rama se encuentra el ejecutable junto a la carpeta necesaria para correr el programa

## IMPORTANTE TENER ESTA APLICACION FUNCIONA SI TIENES EL MODULO D435IF CONECTADO A TU COMPUTADORA.

## Diagrama de Secuencia

El siguiente diagrama de secuencia ilustra el flujo de interacciones para una sesión de grabación continua que repite grabaciones de 15 segundos hasta que se detiene:

```mermaid
sequenceDiagram
    participant Usuario as User
    participant GUI as App (GUI)
    participant Grabador as GrabadorBag
    participant RealSense as RealSense Device

    Usuario->>+GUI: Click "Seleccionar Carpeta"
    GUI->>+Usuario: Abre diálogo de selección de carpeta
    Usuario->>-GUI: Selecciona carpeta y confirma
    GUI->>+Grabador: Establece carpeta_destino
    Note right of Grabador: Carpeta de destino configurada

    Usuario->>+GUI: Click "Iniciar Grabación"
    GUI->>+Grabador: iniciar_grabacion()
    loop Cada 15 segundos
        Grabador->>+RealSense: Configura y empieza la grabación
        RealSense-->>-Grabador: Grabando (15 segundos)
    end
    Note over RealSense: Grabación en curso

    Usuario->>+GUI: Click "Detener Grabación y Salir"
    GUI->>+Grabador: detener_grabacion()
    Grabador->>+RealSense: Detiene la grabación
    RealSense-->>-Grabador: Confirma detención
    Grabador->>-GUI: Grabación detenida
    GUI->>-Usuario: Cierra la aplicación
