from __future__ import print_function
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import sys
from mysql.connector.constants import ClientFlag
import cv2


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")


        #*****VARIABLES***********


        self.var_Department=StringVar()
        self.var_Course=StringVar()
        self.var_Year=StringVar()
        self.var_Semester=StringVar()
        self.var_ID=StringVar()
        self.var_Name=StringVar()
        self.var_Roll_Number=StringVar()
        self.var_Phone_Number=StringVar()
        self.var_Gender=StringVar()
        self.var_DOB=StringVar()
        self.var_Email=StringVar()
        self.var_Address=StringVar()


        # first image

        img=Image.open(r"D:\Face\college_images\face-recognition.png")
        img=img.resize((515,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)


        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=515,height=130)

        # Second Image

        img1=Image.open(r"D:\Face\college_images\smart-attendance.jpg")
        img1=img1.resize((515,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)


        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=515,height=130)

        # Third Image

        img2=Image.open(r"D:\Face\college_images\iStock-182059956_18390_t12.jpg")
        img2=img2.resize((515,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)


        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=515,height=130)

        # background image

        img3=Image.open(r"D:\Face\college_images\wp2551980.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)


        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="Red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=50,width=1520,height=600)

        #left label Frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=755,height=580)

        img_left=Image.open(r"D:\Face\college_images\AdobeStock_303989091.jpeg")
        img_left=img_left.resize((745,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)


        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=745,height=130)

        #Current Course Information

        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=745,height=150)

        # Department

        dep_label=Label(current_course_frame,text="Department",cursor="hand2",font=("times new roman",13,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_Department,font=("times new roman",13,"bold"),state="readonly")
        dep_combo['values']=("Select Department","Computer Science And Engineering","Information Technology","Electronics And Communications","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # Course

        course_label=Label(current_course_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_Course,font=("times new roman",13,"bold"),state="readonly",width=20)
        course_combo['values']=("Select Course","B.tech","M.tech","B.E","BCA")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # Year

        Year_label=Label(current_course_frame,text="Year",font=("times new roman",13,"bold"),bg="white")
        Year_label.grid(row=1,column=0,padx=10,sticky=W)

        Year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_Year,font=("times new roman",13,"bold"),state="readonly",width=20)
        Year_combo['values']=("Select Year","1","2","3","4")
        Year_combo.current(0)
        Year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # Semester

        Semester_label=Label(current_course_frame,text="Semester",font=("times new roman",13,"bold"),bg="white")
        Semester_label.grid(row=1,column=2,padx=10,sticky=W)

        Semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_Semester,font=("times new roman",13,"bold"),state="readonly",width=20)
        Semester_combo['values']=("Select Semester","1","2","3","4","5","6","7","8")
        Semester_combo.current(0)
        Semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Class Student Information

        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Student Class Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=285,width=745,height=265)

        #student-id

        studentId_label=Label(class_student_frame,text="Student-ID",font=("times new roman",13,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_ID,width=20,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student-Name

        student_name_label=Label(class_student_frame,text="Student Name",font=("times new roman",13,"bold"),bg="white")
        student_name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        student_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_Name,width=20,font=("times new roman",13,"bold"))
        student_name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Roll number

        roll_no_label=Label(class_student_frame,text="Roll Number",font=("times new roman",13,"bold"),bg="white")
        roll_no_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_Roll_Number,width=20,font=("times new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Phone Number

        phone_no_label=Label(class_student_frame,text="Phone Number",font=("times new roman",13,"bold"),bg="white")
        phone_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        phone_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_Phone_Number,width=20,font=("times new roman",13,"bold"))
        phone_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # Gender 

        gender_label=Label(class_student_frame,text="Gender",font=("times new roman",13,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_Gender,font=("times new roman",13,"bold"),state="readonly",width=18)
        gender_combo['values']=("Select Gender","Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        

        # DOB

        dob_label=Label(class_student_frame,text="Date Of Birth",font=("times new roman",13,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_DOB,width=20,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #email

        email_label=Label(class_student_frame,text="E-mail",font=("times new roman",13,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_Email,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        # Address

        Address_label=Label(class_student_frame,text="Address",font=("times new roman",13,"bold"),bg="white")
        Address_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        Address_entry=ttk.Entry(class_student_frame,textvariable=self.var_Address,width=20,font=("times new roman",13,"bold"))
        Address_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)


        # radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",cursor="hand2",value="Yes")
        radiobtn1.grid(row=4,column=0)
        
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",cursor="hand2",value="No")
        radiobtn2.grid(row=4,column=1)

        #button frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=170,width=740,height=38)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,cursor="hand2",width=18,font=("times new roman",13,"bold"),bg="skyblue",fg="black")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,cursor="hand2",width=18,font=("times new roman",13,"bold"),bg="pink",fg="black")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,cursor="hand2",width=18,font=("times new roman",13,"bold"),bg="skyblue",fg="black")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,cursor="hand2",width=18,font=("times new roman",13,"bold"),bg="pink",fg="black")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=210,width=740,height=30)

        take_photo_sample_btn=Button(btn_frame1,command=self.generate_dataset,cursor="hand2",text="Take Photo Sample",width=73,font=("times new roman",13,"bold"),bg="violet",fg="black")
        take_photo_sample_btn.grid(row=0,column=0)

        #take_photo_sample_btn=Button(btn_frame1,command=self.generate_dataset,cursor="hand2",text="Take Photo Sample",width=36,font=("times new roman",13,"bold"),bg="violet",fg="black")
        #take_photo_sample_btn.grid(row=0,column=1)

        #update_photo_sample_btn=Button(btn_frame1,text="Update Photo Sample",width=36,font=("times new roman",13,"bold"),bg="violet",fg="black")
        #update_photo_sample_btn.grid(row=0,column=1)

        
        #Right label Frame

        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=770,y=10,width=740,height=580)

        img_right=Image.open(r"D:\Face\college_images\gettyimages-1022573162.jpg")
        img_right=img_right.resize((745,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)


        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=745,height=130)

        #*********SEARCH SYSTEM***********

        #search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        #search_frame.place(x=5,y=135,width=745,height=60)

        #search

        #search_label=Label(search_frame,text="Search By:",font=("times new roman",15,"bold"),bg="violet",fg="black")
        #search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        #search_combo=ttk.Combobox(search_frame,font=("times new roman",13,"bold"),state="readonly",width=15)
        #search_combo['values']=("Select ","Department","Course","Year","Semester","ID","Name","Roll Number","Phone Number","Gender","Date Of Birth","Email","Address","Photo_Sample")
        #search_combo.current(0)
        #search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #search_entry=ttk.Entry(search_frame,width=18,font=("times new roman",13,"bold"))
        #search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        #search_btn=Button(search_frame,text="Search",width=12,font=("times new roman",12,"bold"),bg="skyblue",fg="black")
        #search_btn.grid(row=0,column=3,padx=4)

        #showall_btn=Button(search_frame,text="Show All",width=12,font=("times new roman",12,"bold"),bg="pink",fg="black")
        #showall_btn.grid(row=0,column=4,padx=4)

        #*********TABLE***********

        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=145,width=725,height=400)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("Department","Course","Year","Semester","ID","Name","Roll_Number","Phone Number","Gender","DOB","Email","Address","Photo_Sample"),xscrollcommand=scroll_x.set , yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Department",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("ID",text="ID")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Roll_Number",text="Roll Number")
        self.student_table.heading("Phone Number",text="Phone Number")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Photo_Sample",text="Photo_Sample")
        self.student_table["show"]="headings"

        self.student_table.column("Department",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Semester",width=100)
        self.student_table.column("ID",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Roll_Number",width=100)
        self.student_table.column("Phone Number",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Photo_Sample",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    #**********FUNCTION DECLARATION*********
    def add_data(self):
        if self.var_Department.get()=="Select Department" or self.var_Course.get()=="Select Course" or  self.var_Year.get()=="Select Year" or self.var_Semester.get()=="Select Semester" or self.var_ID.get()=="" or self.var_Name.get()=="" or self.var_Roll_Number.get()=="" or self.var_Phone_Number.get()=="" or self.var_Gender.get()=="Select Gender" or self.var_DOB.get()=="" or self.var_Email.get()=="" or self.var_Address.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", password="Test@123", username="root", database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_Department.get(),
                                                                                                            self.var_Course.get(),
                                                                                                            self.var_Year.get(),
                                                                                                            self.var_Semester.get(),
                                                                                                            self.var_ID.get(),
                                                                                                            self.var_Name.get(),
                                                                                                            self.var_Roll_Number.get(),
                                                                                                            self.var_Phone_Number.get(),
                                                                                                            self.var_Gender.get(),
                                                                                                            self.var_DOB.get(),
                                                                                                            self.var_Email.get(),
                                                                                                            self.var_Address.get(),
                                                                                                            self.var_radio1.get()
                                                                                                        ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To : {str(es)}",parent=self.root)


#*******************FETCH DATABASE***********
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost", password="Test@123", username="root", database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
#**********************GET CURSOR**********
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_Department.set(data[0]),
        self.var_Course.set(data[1]),
        self.var_Year.set(data[2]),
        self.var_Semester.set(data[3]),
        self.var_ID.set(data[4]),
        self.var_Name.set(data[5]),
        self.var_Roll_Number.set(data[6]),
        self.var_Phone_Number.set(data[7]),
        self.var_Gender.set(data[8]),
        self.var_DOB.set(data[9]),
        self.var_Email.set(data[10]),
        self.var_Address.set(data[11]),
        self.var_radio1.set(data[12]),

#*****************UPDATE FUNCTION*****
    def update_data(self):
        if self.var_Department.get()=="Select Department" or self.var_Course.get()=="Select Course" or  self.var_Year.get()=="Select Year" or self.var_Semester.get()=="Select Semester" or self.var_ID.get()=="" or self.var_Name.get()=="" or self.var_Roll_Number.get()=="" or self.var_Phone_Number.get()=="" or self.var_Gender.get()=="Select Gender" or self.var_DOB.get()=="" or self.var_Email.get()=="" or self.var_Address.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost", password="Test@123", username="root", database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Roll_Number=%s,Phone_Number=%s,Gender=%s,DOB=%s,Email=%s,Address=%s,Photo_Sample=%s where ID=%s",(
                                                                                                                                                                                                                        self.var_Department.get(),
                                                                                                                                                                                                                        self.var_Course.get(),
                                                                                                                                                                                                                        self.var_Year.get(),
                                                                                                                                                                                                                        self.var_Semester.get(),
                                                                                                                                                                                                                        self.var_Name.get(),
                                                                                                                                                                                                                        self.var_Roll_Number.get(),
                                                                                                                                                                                                                        self.var_Phone_Number.get(),
                                                                                                                                                                                                                        self.var_Gender.get(),
                                                                                                                                                                                                                        self.var_DOB.get(),
                                                                                                                                                                                                                        self.var_Email.get(),
                                                                                                                                                                                                                        self.var_Address.get(),
                                                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                                                        self.var_ID.get()
                                                                                                                                                                                                                     ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Successful","Student Details Updated Successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To: {str(es)}",parent=self.root)

#*******************DELETE FUNCTION******
    def delete_data(self):
        if self.var_ID.get()=="":
            messagebox.showerror("Error","Student ID is must required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost", password="Test@123", username="root", database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where ID=%s"
                    val=(self.var_ID.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted Student Details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To: {str(es)}",parent=self.root)

#************RESET FUNCTION*********
    def reset_data(self):
        self.var_Department.set("Select Department")
        self.var_Course.set("Select Course")
        self.var_Year.set("Select Year")
        self.var_Semester.set("Select Semester")
        self.var_ID.set("")
        self.var_Name.set("")
        self.var_Roll_Number.set("")
        self.var_Phone_Number.set("")
        self.var_Gender.set("Select Gender")
        self.var_DOB.set("")
        self.var_Email.set("")
        self.var_Address.set("")
        self.var_radio1.set("")

#*************GENERATE DATA SET OR PHOTO SAMPLES********

    def generate_dataset(self):
        if self.var_Department.get()=="Select Department" or self.var_Course.get()=="Select Course" or  self.var_Year.get()=="Select Year" or self.var_Semester.get()=="Select Semester" or self.var_ID.get()=="" or self.var_Name.get()=="" or self.var_Roll_Number.get()=="" or self.var_Phone_Number.get()=="" or self.var_Gender.get()=="Select Gender" or self.var_DOB.get()=="" or self.var_Email.get()=="" or self.var_Address.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", password="Test@123", username="root", database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("UPDATE student SET Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Roll_Number=%s,Phone_Number=%s,Gender=%s,DOB=%s,Email=%s,Address=%s,Photo_Sample=%s WHERE ID=%s",(
                                                                                                                                                                                                            self.var_Department.get(),
                                                                                                                                                                                                            self.var_Course.get(),
                                                                                                                                                                                                            self.var_Year.get(),
                                                                                                                                                                                                            self.var_Semester.get(),
                                                                                                                                                                                                            self.var_Name.get(),
                                                                                                                                                                                                            self.var_Roll_Number.get(),
                                                                                                                                                                                                            self.var_Phone_Number.get(),
                                                                                                                                                                                                            self.var_Gender.get(),
                                                                                                                                                                                                            self.var_DOB.get(),
                                                                                                                                                                                                            self.var_Email.get(),
                                                                                                                                                                                                            self.var_Address.get(),
                                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                                            self.var_ID.get()==id+1
                                                                                                                                                                                                                    
                                                                                                                                                                                                         ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()


#******************** LOAD PREDEFINED DATA ON FACE FRONTALS FROM OPENCV*********
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    # Minimum Neighbour=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==150:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Data Sets Completed!!!")                                                                                                                                                                                                 
            except Exception as es:
                messagebox.showerror("Error",f"Due To: {str(es)}",parent=self.root)


if __name__ =="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()