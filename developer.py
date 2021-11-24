from os import close
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector.fabric import connect
import cv2

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION SYSTEM")

        title_lbl=Label(self.root,text="Developer",font=("Arial Black",35,"bold"),bg="WHITE",fg="BLUE")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"C:\Users\hp\Desktop\face_recognition_system\college_images\dev.jpg")
        img_top=img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)

        btn_frame=Frame(f_lbl,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=1000,y=0,width=500,height=600)
        
        img_t=Image.open(r"C:\Users\hp\Desktop\face_recognition_system\college_images\VIT2.jpg")
        img_t=img_t.resize((200,200),Image.ANTIALIAS)
        self.photoimg_t=ImageTk.PhotoImage(img_t)

        f_lbl=Label(btn_frame,image=self.photoimg_t)
        f_lbl.place(x=300,y=0,width=200,height=200)
        
        phone_label=Label(btn_frame,text="Hello, We are team FRAMS:",font=("Arial Black",13,"bold"),bg="white")
        phone_label.place(x=0,y=5)
        phone=Label(btn_frame,text="1.Miss.Amruta Gulekar",font=("Arial Black",13,"bold"),bg="white")
        phone.place(x=0,y=30)
        phone1=Label(btn_frame,text="2.Miss.Sakshi Indulkar",font=("Arial Black",13,"bold"),bg="white")
        phone1.place(x=0,y=55)
        phone2=Label(btn_frame,text="3.Mr.Rajat Amate",font=("Arial Black",13,"bold"),bg="white")
        phone2.place(x=0,y=80)
        phone3=Label(btn_frame,text="4.Mr.Krunal Badgujar",font=("Arial Black",13,"bold"),bg="white")
        phone3.place(x=0,y=105)

        img_t1=Image.open(r"C:\Users\hp\Desktop\face_recognition_system\college_images\VIT1.jpg")
        img_t1=img_t1.resize((200,200),Image.ANTIALIAS)
        self.photoimg_t1=ImageTk.PhotoImage(img_t1)

        f_lbl=Label(btn_frame,image=self.photoimg_t1)
        f_lbl.place(x=300,y=400,width=200,height=200)

        img_t2=Image.open(r"C:\Users\hp\Desktop\face_recognition_system\college_images\VITLOGO.jpg")
        img_t2=img_t2.resize((200,200),Image.ANTIALIAS)
        self.photoimg_t2=ImageTk.PhotoImage(img_t2)

        f_lbl=Label(btn_frame,image=self.photoimg_t2)
        f_lbl.place(x=300,y=200,width=200,height=200)



if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()