#importações
import cv2

webcam = cv2.VideoCapture(0) #conecta com a webcam
if webcam.isOpened():#verifica se existe conexão
   validacao, frame = webcam.read() # Leitura da webcam

   while validacao: #verifica se existe conexao
     validacao, frame = webcam.read() # Leitura da webcam
     cv2.imshow("Webcam", frame) #Adiciona imagem
     key = cv2.waitKey(1) #Tempo em que os frames aparecem

     if key == 27 : #seleciona tecla ESC
         break

webcam.release() #finaliza conexão
cv2.destroyAllWindows() #garante que fechou a janela de exibição