# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 00:08:23 2020

@author: Suryansh Singh Rawat
"""

import cv2
camera = cv2.VideoCapture(0)
classifier = cv2.CascadeClassifier("F:\\haarcascade_frontalface_default.xml")

while True:
    ret, frame = camera.read()
    if ret == True:
        faces = classifier.detectMultiScale(frame)
        for face in faces:
            x,y,w,z = face
            frame = cv2.rectangle(frame, (x,y), (x+w,y+z), (255,0,0), 2)
                
            cv2.imshow("output",frame)
            
        key = cv2.waitKey(50)
    
    if key == ord("q"):
        break
    
camera.release()
cv2.destroyAllWindows
            