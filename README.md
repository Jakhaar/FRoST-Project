Hier ist das angepasste README mit den zusätzlichen Schritten zur Installation des `requests` Moduls und dem Ausführen des `get_python_api.py` Skripts:

```markdown
# ZED Mini Object Detection with Python

Dieses Repository enthält ein Beispielskript zur Objekterkennung mit der ZED Mini Kamera und der Python API von Stereolabs. Die Anleitung beschreibt, wie die Kamera initialisiert wird, wie die Objekterkennung aktiviert und wie erkannte Objekte angezeigt werden.

## Voraussetzungen

Bevor Sie beginnen, stellen Sie sicher, dass die folgenden Komponenten auf Ihrem System installiert sind:

- [ZED SDK](https://www.stereolabs.com/developers/release/)
- [Python ZED API](https://www.stereolabs.com/docs/app-development/python/install/)
- [CUDA](https://developer.nvidia.com/cuda-downloads) (NVIDIA GPUs erforderlich)

## Installation

1. **ZED SDK Installieren**:
   Laden Sie das ZED SDK von der [offiziellen Stereolabs Website](https://www.stereolabs.com/developers/release/) herunter und installieren Sie es gemäß den Anweisungen für Ihr Betriebssystem.

2. **Python ZED API Installieren**:
   Installieren Sie die Python API mit pip:
   ```bash
   pip install pyzed
   ```

3. **Zusätzliche Abhängigkeiten Installieren**:
   Installieren Sie das `requests` Modul, das für das Skript benötigt wird:
   ```bash
   pip install requests
   ```

4. **Python API Skript ausführen**:
   Führen Sie das `get_python_api.py` Skript aus, um die Python API zu konfigurieren:
   ```bash
   python .\get_python_api.py
   ```

## Nutzung

1. Klonen Sie dieses Repository:
   ```bash
   git clone https://github.com/IhrBenutzername/zed-mini-object-detection.git
   cd zed-mini-object-detection
   ```

2. Führen Sie das Skript zur Objekterkennung aus:
   ```bash
   python object_detection.py
   ```

3. Das Skript startet die Objekterkennung und zeigt die erkannte Objekte in der Konsole an.

## Beispielskript

Das folgende Python-Skript zeigt, wie die ZED Mini Kamera für die Objekterkennung eingerichtet wird:

```python
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
```

## Anpassungen

- **Erkennungsschwelle:** Die Erkennungsschwelle kann über `runtime_params.detection_confidence_threshold` angepasst werden, um die Empfindlichkeit der Objekterkennung zu steuern.
- **Modellauswahl:** Ändern Sie das Erkennungsmodell durch Anpassen von `obj_param.detection_model` (z.B., `MULTI_CLASS_BOX`).

## Fehlerbehebung

- Stellen Sie sicher, dass die Kamera korrekt angeschlossen und eingeschaltet ist.
- Vergewissern Sie sich, dass die erforderlichen Treiber und das ZED SDK korrekt installiert sind.
- Überprüfen Sie, ob CUDA ordnungsgemäß auf Ihrem System eingerichtet ist.

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert – siehe die [LICENSE](LICENSE) Datei für Details.

## Unterstützung

Bei Problemen oder Fragen können Sie ein Issue im Repository erstellen oder die [Stereolabs Dokumentation](https://www.stereolabs.com/docs/) konsultieren.
```

Dieses README enthält nun die Schritte zur Installation von `requests` und zur Ausführung des `get_python_api.py` Skripts. Falls Sie weitere Änderungen benötigen, lassen Sie es mich wissen!
