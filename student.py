from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import os
import cv2



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x830")
        self.root.title("STUDENT MANAGEMENT SYSTEM")
        self.root.wm_iconbitmap("college_images/face.ico")
#variables
        self.var_dep=StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_proctor = StringVar()



#1st image
        img=Image.open("college_images/face-recognition.png")
        img=img.resize((510,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=510,height=130)
#2nd image
        img1=Image.open("college_images/smart-attendance.jpg")
        img1=img1.resize((520,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=510,y=0,width=520,height=130)
#3rd image
        img2=Image.open("college_images/iStock-182059956_18390_t12.jpg")
        img2=img2.resize((510,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1030,y=0,width=510,height=130)

#baground image
        img3=Image.open("college_images/bg1.jpg")
        img3=img3.resize((1540,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1540,height=710)

#Title Label
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman", 15," bold"),bg="pink",fg="dark green")
        title_lbl.place(x=0,y=0,width=1530,height=25)

        # back button
        button = Button(self.root, text="BACK", font=("times new roman", 15, " bold"), command=self.destroy_window,cursor="hand2", bg="red").place(x=1400, y=60, width=100, height=30)

#Main Frame
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=25,width=1530,height=640)
#Left Label Frame
        left_label_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_label_frame.place(x=5,y=5,width=730,height=620)
#Right Label Frame
        right_label_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_label_frame.place(x=710,y=5,width=800,height=620)

#left frame image
        img_left = Image.open("college_Images/AdobeStock_303989091.jpeg")
        img_left = img_left.resize((680, 130), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl = Label(left_label_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=680, height=130)

#current course Label Frame
        current_course_label_frame=LabelFrame(left_label_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_label_frame.place(x=5,y=135,width=680,height=120)
    #department label
        dept_label=Label(current_course_label_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dept_label.grid(row=0,column=0,padx=10)
        dept_combo=ttk.Combobox(current_course_label_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=20,state="readonly")
        dept_combo["values"]=("Select Department","AI&ML","Computer","Ise","Civil","Mechanical")
        dept_combo.current(0)
        dept_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
    #course label
        course_label = Label(current_course_label_frame, text="Course", font=("times new roman", 12, "bold"),bg="white")
        course_label.grid(row=0, column=2, padx=10)
        course_combo = ttk.Combobox(current_course_label_frame,textvariable=self.var_course, font=("times new roman", 12, "bold"), width=20,state="readonly")
        course_combo["values"] = ("Select Course", "BE", "B.Tech", "TE", "Architecture")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10,sticky=W)
    #year label
        year_label = Label(current_course_label_frame, text="Year", font=("times new roman", 12, "bold"),bg="white")
        year_label.grid(row=1, column=0, padx=10)
        year_combo = ttk.Combobox(current_course_label_frame,textvariable=self.var_year ,font=("times new roman", 12, "bold"), width=20,state="readonly")
        year_combo["values"] = ("Select Year", "2020-21", "2021-22", "2022-23")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10,sticky=W)

    #semester label
        semester_label = Label(current_course_label_frame, text="Semester", font=("times new roman", 12, "bold"),bg="white")
        semester_label.grid(row=1, column=2, padx=10)
        semester_combo = ttk.Combobox(current_course_label_frame,textvariable=self.var_semester ,font=("times new roman", 12, "bold"), width=20,state="readonly")
        semester_combo["values"] = ("Select Semester", "1-semester", "2-semester", "3-semester", "4-semester", "5-semester", "6-semester", "7-semester", "8-semester")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10,sticky=W)
#class student information Label Frame
        class_student_label_frame=LabelFrame(left_label_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_label_frame.place(x=5,y=260,width=680,height=335)
#USN
        student_USN_label = Label(class_student_label_frame, text="USN:", font=("times new roman", 12, "bold"),bg="white")
        student_USN_label.grid(row=0, column=0, padx=10,pady=10)
        student_USN_entry=ttk.Entry(class_student_label_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        student_USN_entry.grid(row=0,column=1,padx=2, pady=10,sticky=W)
#NAME
        student_name_label = Label(class_student_label_frame, text="STUDENT NAME:", font=("times new roman", 12, "bold"),bg="white")
        student_name_label.grid(row=0, column=2, padx=10,pady=10)
        student_name_entry=ttk.Entry(class_student_label_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        student_name_entry.grid(row=0,column=3,padx=2, pady=10,sticky=W)
#CLASS
        student_class_label = Label(class_student_label_frame, text="CLASS DIVISION:", font=("times new roman", 12, "bold"),bg="white")
        student_class_label.grid(row=1, column=0, padx=10,pady=10)
        div_combo = ttk.Combobox(class_student_label_frame, textvariable=self.var_div,font=("times new roman", 12, "bold"), width=20, state="readonly")
        div_combo["values"] = ("A", "B", "C")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)
#ROLL
        student_roll_no_label = Label(class_student_label_frame, text="ROLL NO:", font=("times new roman", 12, "bold"),bg="white")
        student_roll_no_label.grid(row=1, column=2, padx=10,pady=10)
        student_roll_no_entry=ttk.Entry(class_student_label_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        student_roll_no_entry.grid(row=1,column=3,padx=2, pady=10,sticky=W)
#GENDER
        student_gender_label = Label(class_student_label_frame, text="GENDER:", font=("times new roman", 12, "bold"),bg="white")
        student_gender_label.grid(row=2, column=0, padx=10,pady=10)
        # student_gender_entry=ttk.Entry(class_student_label_frame,textvariable=self.var_gender,width=20,font=("times new roman",12,"bold"))
        # student_gender_entry.grid(row=2,column=1,padx=2, pady=10,sticky=W)
        gender_combo = ttk.Combobox(class_student_label_frame, textvariable=self.var_gender,font=("times new roman", 12, "bold"), width=20, state="readonly")
        gender_combo["values"] = ("Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=2, pady=10, sticky=W)
#DOB
        student_dob_label = Label(class_student_label_frame, text="DOB:", font=("times new roman", 12, "bold"),bg="white")
        student_dob_label.grid(row=2, column=2, padx=10,pady=10)
        student_dob_entry=ttk.Entry(class_student_label_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        student_dob_entry.grid(row=2,column=3,padx=2, pady=10,sticky=W)
#EMAIL
        student_email_label = Label(class_student_label_frame, text="EMAIL:", font=("times new roman", 12, "bold"),bg="white")
        student_email_label.grid(row=3, column=0, padx=10,pady=10)
        student_email_entry=ttk.Entry(class_student_label_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        student_email_entry.grid(row=3,column=1,padx=2, pady=10,sticky=W)
#PHNO
        student_phno_label = Label(class_student_label_frame, text="PHONE NO:", font=("times new roman", 12, "bold"),bg="white")
        student_phno_label.grid(row=3, column=2, padx=10,pady=10)
        student_phno_entry=ttk.Entry(class_student_label_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        student_phno_entry.grid(row=3,column=3,padx=2, pady=10,sticky=W)
#ADDRESS
        student_address_label = Label(class_student_label_frame, text="ADDRESS:", font=("times new roman", 12, "bold"),bg="white")
        student_address_label.grid(row=4, column=0, padx=10,pady=10)
        student_address_entry=ttk.Entry(class_student_label_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        student_address_entry.grid(row=4,column=1,padx=2, pady=10,sticky=W)
#PROCTOR NAME
        student_proctor_label = Label(class_student_label_frame, text="PROCTOR NAME:", font=("times new roman", 12, "bold"),bg="white")
        student_proctor_label.grid(row=4, column=2, padx=10,pady=10)
        student_proctor_entry=ttk.Entry(class_student_label_frame,textvariable=self.var_proctor,width=20,font=("times new roman",12,"bold"))
        student_proctor_entry.grid(row=4,column=3,padx=2, pady=10,sticky=W)
#radio Buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_label_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0)
        radiobtn2 = ttk.Radiobutton(class_student_label_frame,variable=self.var_radio1, text="No Photo Sample", value="No")
        radiobtn2.grid(row=5, column=1)

#buttons frame
        btn_frame = Frame(class_student_label_frame,bd=3,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=250,width=667,height=30)
#buttons
        save_btn=Button(btn_frame,text="SAVE",font=("times new roman",10,"bold"),command=self.add_data,bg="blue",fg="white",width=23)
        save_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame, text="UPDATE", font=("times new roman", 10, "bold"),command=self.update_data, bg="blue", fg="white",width=23)
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="DELETE", font=("times new roman", 10, "bold"),command=self.delete_data, bg="blue", fg="white",width=23)
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="RESET", font=("times new roman", 10, "bold"),command=self.reset_data, bg="blue", fg="white",width=23)
        reset_btn.grid(row=0, column=3)


        btn_frame1 = Frame(class_student_label_frame, bd=3, relief=RIDGE, bg="white")
        btn_frame1.place(x=5, y=280, width=667, height=30)

        take_photo_btn = Button(btn_frame1, text="TAKE PHOTO SAMPLE", font=("times new roman", 10, "bold"), bg="blue",command=self.generate_dataset, fg="white", width=47)
        take_photo_btn.grid(row=0, column=0)

        update_photo_btn = Button(btn_frame1, text="UPDATE PHOTO SAMPLE", font=("times new roman", 10, "bold"), bg="blue", fg="white",width=47,command=self.generate_dataset)
        update_photo_btn.grid(row=0, column=1)

#right label frame image
        img_right = Image.open("college_Images/gettyimages-1022573162.jpg")
        img_right = img_right.resize((760, 130), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        f_lbl = Label(right_label_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=760, height=130)

# SEARCH SYSTEM
        search_frame = LabelFrame(right_label_frame, bd=2, bg="white", relief=RIDGE, text="Search System",font=("times new roman", 12, "bold"))
        search_frame.place(x=0, y=132, width=760, height=70)

        student_phno_label = Label(search_frame, text="Search By: ", font=("times new roman", 15, "bold"),bg="red",fg="white")
        student_phno_label.grid(row=0, column=0, padx=10,pady=10)

        search_combo = ttk.Combobox(search_frame, font=("times new roman", 12, "bold"), width=20,state="readonly")
        search_combo["values"] = ("Select ", "Roll_NO", "Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10,sticky=W)

        search_entry = ttk.Entry(search_frame, width=20, font=("times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=2, pady=10, sticky=W)

        search_btn = Button(search_frame, text="SEARCH", font=("times new roman", 10, "bold"), bg="blue", fg="white", width=15,padx=5)
        search_btn.grid(row=0, column=3)

        showall_btn = Button(search_frame, text="Show All", font=("times new roman", 10, "bold"), bg="blue", fg="white",width=15,padx=5)
        showall_btn.grid(row=0, column=4)

#table frame
        table_frame = Frame(right_label_frame, bd=3, relief=RIDGE, bg="white")
        table_frame.place(x=0, y=205, width=760, height=390)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","proctor","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student Id")
        self.student_table.heading("name", text="Student Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll NO")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("proctor", text="Proctor")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep", width=100 )
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("proctor", width=100)
        self.student_table.column("photo", width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        #functions declaration

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "ALL Fields Are Required !!", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="hpndjain",database="face_recognizer_2")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_proctor.get(),
                    self.var_radio1.get(),

                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details has been added succesfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To : {str(es)}", parent=self.root)

# fetch data
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="hpndjain", database="face_recognizer_2")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # get cursor

    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_proctor.set(data[13]),
        self.var_radio1.set(data[14]),
#update function
    def update_data(self):
        if (
                self.var_dep.get() == "Select Department"
                or self.var_std_name.get() == ""
                or self.var_std_id.get() == ""
        ):
            messagebox.showerror("Error", "ALL Fields Are Required !!")
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update this student details", parent=self.root)
                if Update:
                    conn = mysql.connector.connect(host="localhost", user="root", password="hpndjain",database="face_recognizer_2")
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "UPDATE student SET Dep=%s, course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s  WHERE Student_id=%s",
                        (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_std_name.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_proctor.get(),
                            self.var_radio1.get(),
                            self.var_std_id.get()
                        ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
                else:
                    return
            except Error as e:
                messagebox.showerror("Error", f"Due To: {str(e)}", parent=self.root)
#delete function
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student id must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root,)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="hpndjain",database="face_recognizer_2")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Sucessfully deleted student details", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

#reset function
    # =============reset==================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_year.set("Select Year")
        self.var_semester.set("Select semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_proctor.set("")
        self.var_radio1.set("")

    def generate_dataset(self):
        if (self.var_dep.get() == "Select Department"or self.var_std_name.get() == ""or self.var_std_id.get() == ""):
            messagebox.showerror("Error", "ALL Fields Are Required !!")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="hpndjain",database="face_recognizer_2")
                my_cursor = conn.cursor()
                my_cursor.execute("Select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute(
                    "UPDATE student SET Dep=%s, course=%s, Year=%s, Semester=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Address=%s, Teacher=%s, PhotoSample=%s WHERE Student_id=%s",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_address.get(),
                        self.var_proctor.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                # =========load predefined data on face frontal from open cv============

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # scaling factor=1.3
                    # minimum neighbour
                    for x, y, w, h in faces:
                        face_cropped = img[y: y + h, x: x + w]
                        return face_cropped

                # url = 'http://192.168.0.243:8080/video'
                cap = cv2.VideoCapture(0)


                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(
                            face,
                            str(img_id),
                            (50, 50),
                            cv2.FONT_HERSHEY_COMPLEX,
                            2,
                            (0, 255, 0),
                            2,
                        )
                        cv2.imshow("Cropped face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data set completed successfully")
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)


    def destroy_window(self):
        self.root.destroy()  # Destroy the root window


if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()