from os import close
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector.fabric import connect
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION SYSTEM")
        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("Arial Black",35,"bold"),bg="WHITE",fg="GREEN")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #img1
        img_bottom=Image.open(r"C:\Users\hp\Desktop\face_recognition_system\college_images\face_detector1.jpg")
        img_bottom=img_bottom.resize((650,700),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=55,width=650,height=700)

        #img2
        img_top=Image.open(r"C:\Users\hp\Desktop\face_recognition_system\college_images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img_top=img_top.resize((950,700),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=650,y=55,width=950,height=700)
        
        #Button
        b1_1=Button(f_lbl,text="Face Recognition",command=self.face_recog,font=("Arial Black",15,"bold"),bg="DARKGREEN",fg="white",cursor="hand2")
        b1_1.place(x=365,y=620,width=200,height=40)

    #Attendance
    def mark_attendance(self,i,i1,i2,i3):
        with open("At.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if ((i not in name_list) and (i1 not in name_list) and (i2 not in name_list) and (i3 not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i3},{i1},{i},{i2},{dtString},{d1},present")

    
    #FACE RECOGNITION

    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbour,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbour)

            coord=[]
            
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",user="root",passwd="Krunal@2002",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("Select Name from student where Student_ID="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                my_cursor.execute("Select Roll from student where Student_ID="+str(id))
                i1=my_cursor.fetchone()
                i1="+".join(i1)

                my_cursor.execute("Select Dep from student where Student_ID="+str(id))
                i2=my_cursor.fetchone()
                i2="+".join(i2)

                my_cursor.execute("Select Student_ID from student where Student_ID="+str(id))
                i3=my_cursor.fetchone()
                i3="+".join(i3)

                if confidence>77:
                    cv2.putText(img,f"Student ID:{i3}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{i1}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{i}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{i2}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,i1,i2,i3)
                    
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                
                coord=[x,y,w,h]
            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)
            
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()




if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()