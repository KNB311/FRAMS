from os import close
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector.fabric import connect
import cv2

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION SYSTEM")

        title_lbl=Label(self.root,text="Help Desk",font=("Arial Black",35,"bold"),bg="WHITE",fg="BLUE")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"C:\Users\hp\Desktop\face_recognition_system\college_images\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img_top=img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)

        phone=Label(f_lbl,text="Email:ASRK@vit.edu.in",font=("Arial Black",20,"bold"),bg="white",fg="Magenta")
        phone.place(x=550,y=150)

        phone1=Label(f_lbl,text="Phone:+91XXXXXXXX",font=("Arial Black",20,"bold"),bg="white",fg="Magenta")
        phone1.place(x=550,y=200)

if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()
