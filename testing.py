import pyzed.sl as sl

# Erstellen Sie ein Kameraobjekt
zed = sl.Camera()

# Konfigurieren Sie die Initialisierungsparameter
init_params = sl.InitParameters()
init_params.camera_resolution = sl.RESOLUTION.HD720  # Setzen Sie die Auflösung
init_params.camera_fps = 30  # Setzen Sie die Bildrate

# Öffnen Sie die Kamera
status = zed.open(init_params)
if status != sl.ERROR_CODE.SUCCESS:
    print(f"Fehler beim Öffnen der Kamera: {status}")
    exit(1)

# Konfigurieren Sie die Objekterkennungsparameter
obj_param = sl.ObjectDetectionParameters()
obj_param.enable_tracking = True  # Aktivieren Sie die Objektverfolgung
obj_param.detection_model = sl.DETECTION_MODEL.MULTI_CLASS_BOX  # Multi-Klassen-Modell

# Initialisieren Sie die Objekterkennung
if zed.enable_object_detection(obj_param) != sl.ERROR_CODE.SUCCESS:
    print("Fehler beim Aktivieren der Objekterkennung")
    zed.close()
    exit(1)

# Erstellen Sie die Laufzeitparameter
runtime_params = sl.ObjectDetectionRuntimeParameters()
runtime_params.detection_confidence_threshold = 50  # Setzen Sie die Erkennungsschwelle

# Erstellen Sie ein Objekt für die Detektionsergebnisse
objects = sl.Objects()

# Hauptschleife zur Bilderfassung und Objekterkennung
try:
    while True:
        # Erfassen Sie ein Bild
        if zed.grab() == sl.ERROR_CODE.SUCCESS:
            # Führen Sie die Objekterkennung aus
            zed.retrieve_objects(objects, runtime_params)
            
            # Holen Sie sich die erkannten Objekte
            obj_list = objects.object_list
            print(f"Anzahl erkannter Objekte: {len(obj_list)}")
            
            # Iterieren Sie über die erkannten Objekte
            for obj in obj_list:
                # Zeigen Sie die Objekt-ID, Position und Erkennungsklasse an
                print(f"Objekt ID: {obj.id}, Klasse: {obj.label}, Position: {obj.position}, Konfidenz: {obj.confidence}")
            
except KeyboardInterrupt:
    # Beenden Sie das Programm mit STRG+C
    print("Beenden des Programms")

# Schließen Sie die Kamera
zed.disable_object_detection()
zed.close()