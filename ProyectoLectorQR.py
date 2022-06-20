#Isaac Alejandro Gutiérrez Huerta 19110198 7E1
#Sistemas de Visión Artificial

import cv2

print("La cámara se cerrará automáticamente al detectar un código QR")

cap = cv2.VideoCapture(0)

detector = cv2.QRCodeDetector()
while True:
  _, img = cap.read()
  data, vertices_array, _ = detector.detectAndDecode(img)
 
  if vertices_array is not None:
    if data:
        print("El link detectado del código QR es el siguiente:\n", data)
        break
    
  cv2.imshow("img", img)

  if cv2.waitKey(1) == ord("0"):
    break

cap.release()
cv2.destroyAllWindows()
