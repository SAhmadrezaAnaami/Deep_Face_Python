#created by AhmadRezaAnaami
import cv2
from deepface import DeepFace
import sys
webcampath = "http://192.168.42.129:8080/video" 
cap = cv2.VideoCapture(0) # or any address

face_detect = cv2.CascadeClassifier("RES\haarcascade_frontalface_default.xml")
scale =1
_counter =0


font = cv2.FONT_HERSHEY_SIMPLEX

org = (30, 30)

fontScale = 0.8

color = (255, 0, 0)

thickness = 2


while True:

    ret , frame = cap.read()
    
    frame = cv2.resize(frame , (int(frame.shape[1] / scale ),int(frame.shape[0] / scale)))

    if _counter % 3 == 0 :
        gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
        faces_rect = face_detect.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
        for (x, y, w, h) in faces_rect:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
    
        if len(faces_rect) != 0 and _counter % 5 == 0:    
            try :
                result = DeepFace.find(frame, db_path = "Pic")
                if (result["identity"].count()) > 0:


                    
                    img = cv2.imread(result["identity"][0])

                    for (x, y, w, h) in faces_rect:
                        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
                    faces_rect2 = face_detect.detectMultiScale(img, scaleFactor=1.1, minNeighbors=4)
                    for (x, y, w, h) in faces_rect2:
                        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

                    frame = cv2.putText(frame,"matched with " +  result["identity"][0], org, font, fontScale, color, thickness, cv2.LINE_AA)

                    cv2.imshow("Cam" , frame)
                    cv2.imshow("Database" , img)

                    if cv2.waitKey(0) == ord("q"):
                        sys.exit()
                        break
                    else:
                        cv2.destroyAllWindows()
                        ret , frame = cap.read()
                else:
                    frame = cv2.putText(frame,"Not matched", org, font, fontScale, color, thickness, cv2.LINE_AA)
                    cv2.imshow("Cam" , frame)

            except:
                pass 

    cv2.imshow("Cam" , frame)
    _counter += 1 
    if cv2.waitKey(1) == ord("q"):
        break


