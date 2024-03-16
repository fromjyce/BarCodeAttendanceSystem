import cv2
import time
from pyzbar import pyzbar

def scan_barcodes(timeout):         #scanningbarcode
    cap = cv2.VideoCapture(0)
    barcodes = []
    start_time = time.time()
    while True:
        ret, frame = cap.read()
        decoded_objects = pyzbar.decode(frame)
        for obj in decoded_objects:
            barcodes == obj.data
            (x, y, w, h) = obj.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            if obj.data.decode("utf-8") not in barcodes:
                barcodes.append(obj.data.decode("utf-8"))
        cv2.imshow('Barcode Scanner [Click Space Bar to Exit the Camera]', frame)
        if time.time() - start_time > timeout:
            break
        if cv2.waitKey(1) & 0xFF == ord(" "):
            break
    cap.release()
    cv2.destroyAllWindows()
    return barcodes
