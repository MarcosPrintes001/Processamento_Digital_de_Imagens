import cv2
import sys
from random import randint

cap = cv2.VideoCapture("assets/futebol.mp4") #pega o video

ok, frame = cap.read()
if not ok:
    print("Não foi possível ler o arquivo")
    sys.exit(1)

caixas = []
imagens = []

while True:
    caixa = cv2.selectROI('Tracker', frame)
    caixas.append(caixa)
    imagens.append((randint(0,255),randint(0,255),randint(0,255)))
    print("Pressione Q para sair ou qualquer outra para continuar proximmo objeto")
    if cv2.waitKey(0) == ord('q'):
        break

tracker = cv2.legacy.TrackerCSRT_create()
multitracker = cv2.legacy.MultiTracker_create()

for caixa in caixas:
    multitracker.add(tracker, frame, caixa)


while cap.isOpened():
    ok, frame = cap.read()
    if not ok:
        break

    ok , boxes = multitracker.update(frame)

    for i, newbox in enumerate(boxes):
        (x,y,w,h) = [int(v) for v in newbox]
        cv2.rectangle(frame, (x,y), (x+w, y+h), imagens[i], 1,1)

    cv2.imshow('MultiTracker', frame)

    if cv2.waitKey(1) & 0XFF == 27:
        break



# cap = cv.VideoCapture("assets/futebol.mp4")
# if not cap.isOpened():
#     print("Cannot open camera")
#     exit()
# while True:
#     # Capture frame-by-frame
#     ret, frame = cap.read()
#     # if frame is read correctly ret is True
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break
#     # Our operations on the frame come here
#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     # Display the resulting frame
#     cv.imshow('frame', gray)
#     if cv.waitKey(1) == ord('q'):
#         break
# # When everything done, release the capture
# cap.release()
# cv.destroyAllWindows()