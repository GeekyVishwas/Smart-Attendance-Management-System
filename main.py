from time import strftime
from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from student import Student
import mysql.connector
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import attendance
from developer import Developer
from help import Help
from datetime import datetime

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        # first image

        img=Image.open(r"college_images\BestFacialRecognition.jpg")
        img=img.resize((515,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)


        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=515,height=130)

        # Second Image

        img1=Image.open(r"college_images\business.jpg")
        img1=img1.resize((515,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)


        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=515,height=130)

        # Third Image

        img2=Image.open(r"college_images\images.jpg")
        img2=img2.resize((515,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)


        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=515,height=130)


        # background image

        img3=Image.open(r"college_images\1500115666cvr.webp")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)


        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="SMART ATTENDANCE MONITORING SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #************** TIME *******
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000,time)

        lbl=Label(title_lbl, font=('times new roman',20,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=(-15),width=170,height=65)
        time()


        # Student Button

        img4=Image.open(r"college_images\gettyimages-1022573162.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        # BUTTON

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details1,cursor="hand2")
        b1.place(x=320,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details1,cursor="hand2",font=("times new roman",20,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=320,y=300,width=220,height=40)


        # Detect Face Button

        img5=Image.open(r"college_images\face_detector1.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=620,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",20,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=620,y=300,width=220,height=40)

        # Attendance Button

        img6=Image.open(r"college_images\report.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=920,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",20,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=920,y=300,width=220,height=40)
        

        # Help Desk Button

        #img11=Image.open(r"college_images\Help Desk.jpg")
        #img11=img11.resize((220,220),Image.ANTIALIAS)
        #self.photoimg11=ImageTk.PhotoImage(img11)

        #b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.help_data)
        #b1.place(x=1100,y=100,width=220,height=220)

        #b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",20,"bold"),bg="darkblue",fg="white")
        #b1_1.place(x=1100,y=300,width=220,height=40)

        # Train Face Button

        img7=Image.open(r"college_images\Train.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.train_data)
        b1.place(x=320,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Train Face",cursor="hand2",command=self.train_data,font=("times new roman",20,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=320,y=580,width=220,height=40)

        # Photos Face Button

        img8=Image.open(r"college_images\opencv_face_reco_more_data.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.open_img,)
        b1.place(x=620,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",20,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=620,y=580,width=220,height=40)

        # Developer Button

        #img9=Image.open(r"college_images\Team-Management-Software-Development.jpg")
        #img9=img9.resize((220,220),Image.ANTIALIAS)
        #self.photoimg9=ImageTk.PhotoImage(img9)

        #b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.developer_data)
        #b1.place(x=800,y=380,width=220,height=220)

        #b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",20,"bold"),bg="darkblue",fg="white")
        #b1_1.place(x=800,y=580,width=220,height=40)

        # Exit Button

        img10=Image.open(r"college_images\exit.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.iExit)
        b1.place(x=920,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="EXIT",cursor="hand2",command=self.iExit,font=("times new roman",20,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=920,y=580,width=220,height=40)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are You Sure You Want To Exit",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return

        #******************FUNCTION BUTTON************
        
    def student_details1(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=attendance(self.new_window)
    
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
    

if __name__ =="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()