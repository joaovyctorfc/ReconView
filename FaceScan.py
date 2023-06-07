import cv2
import mediapipe as mp

webcam = cv2.VideoCapture(0)
solucao_reconhecimento_rosto = mp.solutions.face_detection
reconhecedor_rosto = solucao_reconhecimento_rosto.FaceDetection()
desenho = mp.solutions.drawing_utils

while True:
    verificador, frame = webcam.read()
    if not verificador:
        break

    lista_faces = reconhecedor_rosto.process(frame)
    if lista_faces.detections:
        for face in lista_faces.detections:
            desenho.draw_detection(frame, face)
    cv2.imshow("FaceScan", frame)
    key = cv2.waitKey(1)  # Tempo em que os frames aparecem

    if key == 27:  # seleciona tecla ESC
        break

webcam.release()
cv2.destroyAllWindows()
