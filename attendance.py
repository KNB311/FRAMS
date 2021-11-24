from os import close
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector.fabric import connect
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION SYSTEM")
        
        #variables
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        #IMG1
        img=Image.open(r"C:\Users\hp\Desktop\face_recognition_system\college_images\smart-attendance.jpg")
        img=img.resize((800,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)

        #IMG2
        img1=Image.open(r"C:\Users\hp\Desktop\face_recognition_system\college_images\iStock-182059956_18390_t12.jpg")
        img1=img1.resize((800,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=200)

        #bg image
        img3=Image.open(r"C:\Users\hp\Desktop\face_recognition_system\college_images\bg.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=710)

        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("Arial Black",35,"bold"),bg="WHITE",fg="DARKGREEN")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=55,width=1480,height=600)

        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student attendance Details",font=("Arial Black",12,"bold"))
        left_frame.place(x=10,y=10,width=730,height=580)

        img_left=Image.open(r"C:\Users\hp\Desktop\face_recognition_system\college_images\AdobeStock_303989091.jpeg")
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

        left_inside_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Student attendance Details",font=("Arial Black",12,"bold"))
        left_inside_frame.place(x=0,y=135,width=726,height=370)

        #LABLE and ENTRY
        #Attendance ID
        attendanceId_label=Label(left_inside_frame,text="Attendance ID:",font=("Arial Black",13,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        attendanceId_entry=ttk.Entry(left_inside_frame,width=17,textvariable=self.var_atten_id,font=("Arial Black",13,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        #Roll
        rollLabel=Label(left_inside_frame,text="Roll:",font=("Arial Black",13,"bold"),bg="white")
        rollLabel.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        atten_roll=ttk.Entry(left_inside_frame,width=17,textvariable=self.var_atten_roll,font=("Arial Black",13,"bold"))
        atten_roll.grid(row=0,column=3,padx=5,pady=5,sticky=W)

        #Name
        NameLabel=Label(left_inside_frame,text="Name:",font=("Arial Black",13,"bold"),bg="white")
        NameLabel.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        atten_name=ttk.Entry(left_inside_frame,width=17,textvariable=self.var_atten_name,font=("Arial Black",13,"bold"))
        atten_name.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        #Dep
        depLabel=Label(left_inside_frame,text="Department:",font=("Arial Black",13,"bold"),bg="white")
        depLabel.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        atten_dep=ttk.Entry(left_inside_frame,width=17,textvariable=self.var_atten_dep,font=("Arial Black",13,"bold"))
        atten_dep.grid(row=1,column=3,padx=5,pady=5,sticky=W)

        #time
        timeLabel=Label(left_inside_frame,text="Time:",font=("Arial Black",13,"bold"),bg="white")
        timeLabel.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        atten_time=ttk.Entry(left_inside_frame,width=17,textvariable=self.var_atten_time,font=("Arial Black",13,"bold"))
        atten_time.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        #date
        dateLabel=Label(left_inside_frame,text="Date:",font=("Arial Black",13,"bold"),bg="white")
        dateLabel.grid(row=2,column=2,padx=5,pady=5,sticky=W)

        atten_date=ttk.Entry(left_inside_frame,width=17,textvariable=self.var_atten_date,font=("Arial Black",13,"bold"))
        atten_date.grid(row=2,column=3,padx=5,pady=5,sticky=W)

        #attendance
        atLabel=Label(left_inside_frame,text="Attendance:",font=("Arial Black",13,"bold"),bg="white")
        atLabel.grid(row=3,column=0,padx=5,pady=5,sticky=W)

        self.atten_status=ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance,font=("Arial Black",13,"bold"),state="readonly",width=16)
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3,column=1,padx=5,pady=5,sticky=W)

        #bbuttons frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=270,width=715,height=200)
        
        Import_btn=Button(btn_frame,text="Import",command=self.importCSV,width=19,height=1,font=("Arial Black",13,"bold"),bg="blue",fg="white")
        Import_btn.grid(row=0,column=0)

        Export_btn=Button(btn_frame,text="Export",command=self.exportCSV,width=19,font=("Arial Black",13,"bold"),bg="blue",fg="white")
        Export_btn.grid(row=0,column=1)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=19,font=("Arial Black",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=2)
        
        
        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("Arial Black",12,"bold"))
        right_frame.place(x=750,y=10,width=720,height=580)

        table_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,font=("Arial Black",12,"bold"))
        table_frame.place(x=5,y=5,width=710,height=455)

        #Scroll BAr Table
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.attendanceReportTable=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.attendanceReportTable.xview)
        scroll_y.config(command=self.attendanceReportTable.yview)

        self.attendanceReportTable.heading("id",text="Attendance ID")
        self.attendanceReportTable.heading("roll",text="Roll")
        self.attendanceReportTable.heading("name",text="Name")
        self.attendanceReportTable.heading("department",text="Department")
        self.attendanceReportTable.heading("time",text="Time")
        self.attendanceReportTable.heading("date",text="Date")
        self.attendanceReportTable.heading("attendance",text="Attendance")
        
        self.attendanceReportTable["show"]="headings"

        self.attendanceReportTable.column("id",width=100)
        self.attendanceReportTable.column("roll",width=100)
        self.attendanceReportTable.column("name",width=100)
        self.attendanceReportTable.column("department",width=100)
        self.attendanceReportTable.column("time",width=100)
        self.attendanceReportTable.column("date",width=100)
        self.attendanceReportTable.column("attendance",width=100)


        self.attendanceReportTable.pack(fill=BOTH,expand=1)

        self.attendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    #Fetch Data

    def fetchData(self,rows):
        self.attendanceReportTable.delete(*self.attendanceReportTable.get_children())
        for i in rows:
            self.attendanceReportTable.insert("",END,values=i)
    
    def importCSV(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    def exportCSV(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found To Export",parent=self.root)
                return False

            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                export=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    export.writerow(i)
                messagebox.showinfo("Data Exported","Your Data Has Been Exported to"+os.path.basename(fln)+"successfully")
        except Exception as es:
                messagebox,messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    def get_cursor(self,events=""):
        cursor_row=self.attendanceReportTable.focus()
        content=self.attendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])
    
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
        

if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()