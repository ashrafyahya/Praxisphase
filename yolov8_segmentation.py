import cv2
from ultralytics import YOLO

# 1. Lade das YOLOv8-Segmentierungsmodell
model = YOLO('yolov8n-seg.pt')  # Verwende das YOLOv8-Segmentierungsmodell

# 2. Kamera-Stream initialisieren
cap = cv2.VideoCapture(4)  # 0 für die Standardkamera

# Überprüfen, ob die Kamera geöffnet ist
if not cap.isOpened():
    print("Fehler: Kamera konnte nicht geöffnet werden.")
    exit()

# 3. Echtzeit-Videostream mit YOLOv8-Segmentierung
while True:
    ret, frame = cap.read()  # Frame von der Kamera lesen
    if not ret:
        print("Fehler: Frame konnte nicht gelesen werden.")
        break

    # YOLOv8-Segmentierung auf den aktuellen Frame anwenden
    results = model(frame, task="segment")

    # Ergebnisse als annotiertes Bild erhalten
    annotated_frame = results[0].plot()

    # Annotierten Frame anzeigen
    cv2.imshow("YOLOv8 Segmentation", annotated_frame)

    # Beenden, wenn die 'q'-Taste gedrückt wird
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 4. Kamera und Fenster schließen
cap.release()
cv2.destroyAllWindows()

