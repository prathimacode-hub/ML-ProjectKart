import winsound
frequency=2500
duration=1000
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
import tensorflow as tf
import tkinter as tk
from PIL import ImageTk,Image  
from flask import Flask,redirect, url_for,render_template,request

def func():
    root = tk.Tk() 
    canvas = tk.Canvas(root, width = 400, height = 200)  
    canvas.pack()  
    img = ImageTk.PhotoImage(Image.open("E:\github\ML-ProjectKart\Driver Drowsiness Detection System\Images\driver1.jpg"))  
    canvas.create_image(15, 20, anchor="nw", image=img)
    l = tk.Label(root, text = "Click Run to take the test!")
    l.config(font =("Georgia", "18"))
    l.pack(side=tk.TOP, pady= 10)

    def run_program():
        new_model = tf.keras.models.load_model('E:\github\ML-ProjectKart\Driver Drowsiness Detection System\models\my_model2.h5')

        path= "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        cap = cv2.VideoCapture(1)

        if not cap.isOpened():
            cap= cv2.VideoCapture(0)
        if not cap.isOpened():
            raise IOError("Cannot open webcam")
        counter=0
        eyes_roi=0

        while True:
            ret,frame =cap.read()
            eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')
            gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            #print(faceCascade.empty())
            eyes = eye_cascade.detectMultiScale(gray, 1.1,4)
            for x,y,w,h in eyes:
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
                cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
                eyess = eye_cascade.detectMultiScale(roi_gray)
                if len(eyess) ==0:
                    print("eyes are not detected")
                    continue
                else:
                    for(ex,ey,ew,eh) in eyess:
                        eyes_roi = roi_color[ey: ey+eh, ex:ex+ew]
            gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            print(faceCascade.empty())
            faces = faceCascade.detectMultiScale(gray,1.1,4)
    
            for (x,y,w,h) in faces:
                cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
            font =cv2.FONT_HERSHEY_SIMPLEX
            final_image =cv2.resize(eyes_roi, (224, 224))
            final_image = np.expand_dims(final_image, axis=0)
            final_image=final_image/255.0
  
            print(final_image.shape)
            if len(final_image.shape)!=4:
                continue
            #final_image = final_image.reshape(1, 224, 224, 3)
    
            Predictions = new_model.predict(final_image)
            if (Predictions>=0.8 and Predictions<=1.0):
                status = "Open eyes"
                cv2.putText(frame,
                        status,
                        (150,150),
                        font,3,
                        (0,255,0),
                        2, cv2.LINE_4)
                x1, y1, w1, h1 = 0, 0, 175, 75
                #draw black bg rectangle
                cv2.rectangle(frame,(x1, x1), (x1+w1, y1 + h1), (0,0,0), -1)
                #add text
                cv2.putText(frame, 'Active', (x1 + int(w1/10),y1 + int(h1/2)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

            else:
                counter= counter+1
                status= "closed eyes"
                cv2.putText(frame,
                            status,
                            (150,150),
                            font,3,
                            (0,0,255),
                            2, cv2.LINE_4)

                cv2.rectangle(frame,(x , y), (x +w , y + h), (0,0,255), 2)
                if counter>7:
                    x1,y1,w1,h1 = 0,0,175,75
                    cv2.rectangle(frame,(x1, x1), (x1+w1, y1 + h1), (0,0,0), -1)
                    #add text
                    cv2.putText(frame, 'Sleep Alert!!', (x1 + int(w1/10),y1 + int(h1/2)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)
                    winsound.Beep(frequency, duration)
                    counter = 0
    
            cv2.imshow('Drowsiness Detection' , frame)
            if cv2.waitKey(2) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()


    frame = tk.Frame(root)
    frame.pack()
    root.title("Driver's drowsiness test")
    root.geometry('400x300')

    """
    b1 = tk.Button(frame, 
                    text="QUIT", 
                    fg="red",
                    width=10,
                    height=10,
                    command=quit)
    b1.pack(side=tk.RIGHT, padx=5, pady=5)
    """
    b2 = tk.Button(frame,
                    text="RUN",
                    width=10,
                    height=10,
                    command=run_program)
    b2.pack(side=tk.RIGHT, padx=5, pady=5)

    root.mainloop()