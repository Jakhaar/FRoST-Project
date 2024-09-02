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
