import cv2
import mediapipe as mp

webcam = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

while True:
    verificador, frame = webcam.read()
    if not verificador:
        break

    results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))  # Processa a imagem com o MediaPipe Hands

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Faça o que desejar com os pontos-chave das mãos (hand_landmarks)
            # Por exemplo, você pode desenhar os pontos na imagem
            for landmark in hand_landmarks.landmark:
                x, y = int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0])
                cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

    cv2.imshow("Hands Detection", frame)
    key = cv2.waitKey(1)  # Tempo em que os frames aparecem

    if key == 27:  # seleciona tecla ESC
        break

webcam.release()
cv2.destroyAllWindows()