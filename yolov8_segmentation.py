import cv2
import pyrealsense2 as rs
import numpy as np
from ultralytics import YOLO

# 1. YOLOv8-Modell für Segmentierung laden
model = YOLO('yolov8n-seg.pt')

# 2. RealSense Pipeline initialisieren
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)

# Starten der RealSense-Kamera
pipeline.start(config)

# Tiefenskala für RealSense-Tiefe (Meter-Konvertierung)
depth_sensor = pipeline.get_active_profile().get_device().first_depth_sensor()
depth_scale = depth_sensor.get_depth_scale()  # z.B. 0.001 (1mm)

# 3. Verarbeitungsschleife
try:
    while True:
        # Frames von der Kamera abrufen
        frames = pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()
        depth_frame = frames.get_depth_frame()

        if not color_frame or not depth_frame:
            continue

        # Farb- und Tiefenbilder abrufen
        color_image = np.asanyarray(color_frame.get_data())
        depth_image = np.asanyarray(depth_frame.get_data())

        # YOLOv8 auf das Farbbild anwenden
        results = model(color_image, task="segment")
        annotated_frame = results[0].plot()

        # Tiefe der erkannten Objekte berechnen
        for segment in results[0].masks.data:  # Segmentierte Bereiche
            # Segment-Maske in Pixel umwandeln
            mask = segment.cpu().numpy().astype(np.uint8) * 255

            # Tiefenwerte innerhalb des Maskenbereichs extrahieren
            masked_depth = cv2.bitwise_and(depth_image, depth_image, mask=mask)
            valid_depth = masked_depth[masked_depth > 0]  # Nicht-Null-Werte

            if len(valid_depth) > 0:
                # Medianwert der Tiefe für das erkannte Objekt berechnen
                median_depth = np.median(valid_depth) * depth_scale  # In Meter
                print(f"Tiefe des Objekts: {median_depth:.2f} Meter")

        # Annotierten Frame anzeigen
        cv2.imshow("YOLOv8 + RealSense", annotated_frame)

        # Beenden bei 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    # Kamera und Fenster schließen
    pipeline.stop()
    cv2.destroyAllWindows()
