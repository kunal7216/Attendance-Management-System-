from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime
import schedule
import time

class Face_Recongnition:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition Pannel")

        # This part is image labels setting start
        # first header image
        img=Image.open(r"C:\Users\91895\OneDrive\Desktop\PBL\college_images\banner.jpg")
        img=img.resize((1366,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

        # backgorund image
        bg1=Image.open(r"C:\Users\91895\OneDrive\Desktop\PBL\college_images\bg2.jpg")
        bg1=bg1.resize((1366,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Welcome to Face Recognition Pannel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        # Create buttons below the section
        # -------------------------------------------------------------------------------------------------------------------
        # Training button 1
        std_img_btn=Image.open(r"C:\Users\91895\OneDrive\Desktop\PBL\college_images\f_det.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.face_recog,image=self.std_img1,cursor="hand2")
        std_b1.place(x=600,y=170,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.face_recog,text="Face Detector",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=600,y=350,width=180,height=45)

        # =============attendace===========

    def mark_attendance(self,i,r,n,d,e,p):
        with open("attendance_report/Student_daily_record.csv","r+",newline="") as f:
         myDataList=f.readlines()
         name_list=[]
         for line in myDataList:
             entry=line.split((","))
             name_list.append(entry[0])
         if((i not in name_list)and(r not in name_list)and( n not in name_list)and(d not in name_list)and(e not in name_list)and(p not in name_list)):
             now=datetime.now()
             d1=now.strftime("%d/%m/%Y")
             dtString=now.strftime("%H:%M:%S")
             f.writelines(f"{n},{e},{p},{i},{r},{d},{dtString},{d1},Present\n")



        # <============recognition===========>

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y: y + h, x: x + w])
                confidence = int((100 * (1 - predict / 300)))


                conn = mysql.connector.connect(host="localhost", user="root", password="hpndjain", database="face_recognizer_2")
                my_cursor = conn.cursor()

                my_cursor.execute("Select Name from student where Student_id=" + str(id))
                n = my_cursor.fetchone()
                n = n[0] if n else "Unknown"

                my_cursor.execute("Select Roll from student where Student_id=" + str(id))
                r = my_cursor.fetchone()
                r = r[0] if r else "Unknown"

                my_cursor.execute("Select Dep from student where Student_id=" + str(id))
                d = my_cursor.fetchone()
                d = d[0] if d else "Unknown"

                my_cursor.execute("Select Student_id from student where Student_id=" + str(id))
                i = my_cursor.fetchone()
                i = i[0] if i else "Unknown"

                my_cursor.execute("Select email from student where Student_id=" + str(id))
                e = my_cursor.fetchone()
                e = e[0] if e else "Unknown"

                my_cursor.execute("Select phone from student where Student_id=" + str(id))
                p = my_cursor.fetchone()
                p = p[0] if p else "Unknown"

                if confidence > 74:
                    cv2.putText(img,f"Id:{i}",(x, y - 75),cv2.FONT_HERSHEY_COMPLEX,0.8,	(0,0,0),3,)
                    cv2.putText(img,f"Roll:{r}",(x, y - 55),cv2.FONT_HERSHEY_COMPLEX,0.8,	(0,0,0),3,)
                    cv2.putText(img,f"Name:{n}",(x, y - 30),cv2.FONT_HERSHEY_COMPLEX,0.8,	(0,0,0),3,)
                    cv2.putText(img,f"Deartment:{d}",(x, y - 5),cv2.FONT_HERSHEY_COMPLEX,0.8,	(0,0,0),3,)
                    self.mark_attendance(i,r,n,d,e,p)
                else:
                    cv2.rectangle(img, (x, y), (x + w,y + h), (0, 0, 255), 3)
                    cv2.putText(img,"Unknown face",(x, y - 5),cv2.FONT_HERSHEY_COMPLEX,0.8,	(0,0,0),3,)
                coord = [x, y, w, h]
            return coord

        def recognize(img,clf,faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        # url = 'http://192.168.0.243:8080/video'
        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to face recognition",img)

            if cv2.waitKey(1) == 13:  # Press Enter key to exit the loop
                break
        video_cap.release()
        cv2.destroyAllWindows()

    def destroy_window(self):
        self.root.destroy()  # Destroy the root window

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recongnition(root)
    root.mainloop()
