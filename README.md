# ZED Mini Object Detection with Python

Dieses Repository enthält alle nötigen Skripte zur Objekterkennung und für das Spatial Mapping mithilfe der ZED Kamera und der Python API von Stereolabs. Die Dokumentation beschreibt detailliert die Schritte zur Initialisierung der Kamera, Aktivierung der Objekterkennung und Darstellung der Ergebnisse.

## Voraussetzungen

Bevor Sie mit der Implementierung beginnen, stellen Sie sicher, dass die folgenden Komponenten auf Ihrem System installiert sind:

- [ZED SDK](https://www.stereolabs.com/developers/release/): Zur Nutzung der Tiefenkamera-Funktionen.
- [Python ZED API](https://www.stereolabs.com/docs/app-development/python/install/): Für die Entwicklung von Python-Skripten mit der ZED Kamera.
- [CUDA](https://developer.nvidia.com/cuda-downloads): Erforderlich für die Nutzung der NVIDIA GPUs, um rechenintensive Aufgaben wie Tiefenwahrnehmung und Objekterkennung zu bewältigen.

## Installation

**Hinweis:** Zunächst empfehlen wir, das offizielle Tutorial zur Einrichtung einer Python-Entwicklungsumgebung mit virtueller Umgebung zu befolgen: [Stereolabs Python Virtual Environment Tutorial](https://www.stereolabs.com/docs/app-development/python/virtual_env).

Falls die Installation über das Tutorial nicht erfolgreich ist, folgen Sie den untenstehenden Anweisungen in dieser README:

1. **Installation des ZED SDKs**:
   Laden Sie das ZED SDK von der [offiziellen Stereolabs Website](https://www.stereolabs.com/developers/release/) herunter und folgen Sie den Installationsanweisungen für Ihr Betriebssystem.

2. **Installation der Python ZED API**:
   Installieren Sie die Python API über pip:

   ```bash
   pip install pyzed
   ```

3. **Installation zusätzlicher Abhängigkeiten**:
   Installieren Sie notwendige Python-Module wie `requests`:

   ```bash
   pip install requests
   ```

4. **Konfiguration der Python API**:
   Führen Sie das Skript `get_python_api.py` aus, um die Python API korrekt zu konfigurieren:
   ```bash
   python .\get_python_api.py
   ```

## Nutzung

1. Klonen Sie das Repository:

   ```bash
   git clone https://github.com/Jakhaar/FRoST-Project
   cd FRoST-Project
   ```

2. Starten Sie das Skript zur Objekterkennung:

   ```bash
   python object_detection.py
   ```

3. Das Skript führt die Objekterkennung durch und gibt die erkannten Objekte in der Konsole aus.

## Beispielskript zur Kamerainitialisierung und Bildaufnahme

Das folgende Python-Skript demonstriert die grundlegende Einrichtung der ZED Mini Kamera und das Speichern eines aufgenommenen Bildes:

```python
# Test File
import pyzed.sl as sl

# Erstellen eines Kameraobjekts
zed = sl.Camera()

# Konfiguration der Kameraparameter
init_params = sl.InitParameters()
init_params.camera_resolution = sl.RESOLUTION.HD720  # Wählen der Auflösung
init_params.camera_fps = 30  # Bildrate

# Öffnen der Kamera
status = zed.open(init_params)
if status != sl.ERROR_CODE.SUCCESS:
    print(f"Fehler beim Öffnen der Kamera: {status}")
    exit(1)

# Erstellen eines Bildobjekts
image = sl.Mat()

# Erfassen eines Bildes
if zed.grab() == sl.ERROR_CODE.SUCCESS:
    # Holen des linken Bildes (RGB)
    zed.retrieve_image(image, sl.VIEW.LEFT)

    # Speichern des Bildes als PNG
    image.write(".data/pictures/camera_test.png")
    print("Bild gespeichert als 'camera_test.png'")

# Schließen der Kamera
zed.close()
```

## Anpassungsmöglichkeiten

- **Erkennungsschwelle anpassen**: Passen Sie die Empfindlichkeit der Objekterkennung an, indem Sie den Wert von `runtime_params.detection_confidence_threshold` ändern.
- **Modellauswahl**: Passen Sie das verwendete Erkennungsmodell durch Modifikation von `obj_param.detection_model` an (z.B. Nutzung von `MULTI_CLASS_BOX` für die Erkennung mehrerer Objektklassen).

## Fehlerbehebung

- Vergewissern Sie sich, dass die ZED Kamera korrekt angeschlossen und eingeschaltet ist.
- Stellen Sie sicher, dass die erforderlichen Treiber und das ZED SDK korrekt installiert sind.
- Überprüfen Sie, ob CUDA ordnungsgemäß auf Ihrem System eingerichtet ist.

## Unterstützung

Bei Fragen oder Problemen können Sie ein Issue im Repository erstellen.
