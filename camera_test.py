#Test File
import pyzed.sl as sl

# Erstellen Sie ein Kameraobjekt
zed = sl.Camera()

# Konfigurieren Sie die Kameraparameter
init_params = sl.InitParameters()
init_params.camera_resolution = sl.RESOLUTION.HD720  # Wählen Sie die Auflösung
init_params.camera_fps = 30  # Bildrate

# Öffnen Sie die Kamera
status = zed.open(init_params)
if status != sl.ERROR_CODE.SUCCESS:
    print(f"Fehler beim Öffnen der Kamera: {status}")
    exit(1)

# Erstellen Sie ein Bildobjekt
image = sl.Mat()

# Erfassen Sie ein Bild
if zed.grab() == sl.ERROR_CODE.SUCCESS:
    # Holen Sie sich das linke Bild (RGB)
    zed.retrieve_image(image, sl.VIEW.LEFT)
    
    # Speichern Sie das Bild als PNG
    image.write("zed_image.png")
    print("Bild gespeichert als 'zed_image.png'")

# Schließen Sie die Kamera
zed.close()
