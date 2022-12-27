#created by AhmadRezaAnaami
import cv2
import math
from deepface import DeepFace
import time
import playsound
import os
import sys



cap = cv2.VideoCapture(0) #or address of your webcam

face_detect = cv2.CascadeClassifier("RES\haarcascade_frontalface_default.xml")

_counter = 2 ;

font = cv2.FONT_HERSHEY_SIMPLEX

org = (50, 50)

fontScale = 1

color = (255, 0, 0)

thickness = 2


prev_frame_time = 0
new_frame_time = 0


while True:

    _counter += 1 
    ret , frame = cap.read()
    
    
    frame = cv2.resize(frame , (int(frame.shape[1] / 2 ),int(frame.shape[0] / 2)))
    
    faces_rect1 = face_detect.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=4)
    if len(faces_rect1) != 0  :
        for (x, y, w, h) in faces_rect1:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
        try:
            result = DeepFace.find(frame, db_path = "Pic")
            if (result["identity"].count()) > 0:
                

                
                frame = cv2.putText(frame,"matched with " +  result["identity"][0], org, font, fontScale, color, thickness, cv2.LINE_AA)
                myText = "face perfectly matched with " + result["identity"][0]
                img = cv2.imread(result["identity"][0])
                for (x, y, w, h) in faces_rect1:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
                faces_rect2 = face_detect.detectMultiScale(img, scaleFactor=1.1, minNeighbors=4)
                for (x, y, w, h) in faces_rect2:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
                cv2.imshow("img" , frame)
                cv2.imshow("Database" , img)
                playsound.playsound("RES/FM.mp3")
                ret , frame = cap.read()
                if cv2.waitKey(0) & 0XFF == ord("q"):
                    cap.release()
                    cv2.destroyAllWindows()
                    sys.exit()
                cv2.destroyAllWindows()
                cap.release()
                cap = cv2.VideoCapture("http://192.168.42.129:8080/video")
                _counter= 0 ; 
        except:
            pass  



    for (x, y, w, h) in faces_rect1:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
    

    
    if _counter > 200:
        frame = cv2.putText(frame,"Not Matched", org, font, fontScale, color, thickness, cv2.LINE_AA)
        cv2.imshow("img" , frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        _counter= 0 ; 
        
    new_frame_time = time.time()

    fps = 1/(new_frame_time-prev_frame_time)
    prev_frame_time = new_frame_time

    fps = str(int(fps))

    frame = cv2.putText(frame,"fps : " + fps, org, font, fontScale, color, thickness, cv2.LINE_AA)

    if _counter % 3 == 0:
        cv2.imshow("img" , frame)
    
    if cv2.waitKey(1) & 0XFF == ord("q"):
        cap.release()
        cv2.destroyAllWindows()
        sys.exit()
    if cv2.waitKey(1) & 0XFF == ord("p"):
        while True:
            if cv2.waitKey(1) & 0XFF == ord("p"):
                cap.release()
                cap = cv2.VideoCapture("http://192.168.42.129:8080/video")
                break
 
 
   
