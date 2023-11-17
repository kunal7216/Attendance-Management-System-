from tkinter import*
from PIL import Image,ImageTk
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import csv
from twilio.rest import Client

# Twilio credentials
account_sid = 'ACf8061d95f1b4eb38a1b695f75c682558'
auth_token = '42c873788e68bfbdc4bece317cdbb6d6'
twilio_phone_number = '+15737664870'


# Initialize Twilio client
client = Client(account_sid, auth_token)


email_user = "g7@bmsit.in"
email_password = "yxgcyxfzgdihxowa"
subject = "Attendance alert"

class send_notification:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x830+0+0")
        self.root.title("Send Notification")
        self.root.wm_iconbitmap("college_Images/face.ico")
#baground image
        img3=Image.open("college_images/notification.jpeg")
        img3=img3.resize((1540,830),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1540,height=830)

#Title Label
        title_lbl=Label(bg_img,text="SEND NOTIFICATION",font=("times new roman", 35," bold"),bg="lavender",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)


#1st button student button
        img4=Image.open("college_images/gmail.png")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(bg_img,image=self.photoimg4,cursor="hand2",command=self.email).place(x=400,y=300,width=220,height=220)
        b1_lbl=Button(bg_img,text="SEND MAIL",cursor="hand2",font=("times new roman", 15," bold"),bg="darkblue",fg="red",command=self.email).place(x=400,y=520,width=220,height=40)

#2nd button student button
        img5=Image.open("college_images/sms.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b2=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.sms).place(x=870,y=300,width=220,height=220)
        b2_lbl=Button(bg_img,text="SEND SMS",cursor="hand2",font=("times new roman", 15," bold"),bg="darkblue",fg="red",command=self.sms).place(x=870,y=520,width=220,height=40)

#back button
        button = Button(bg_img, text="BACK",font=("times new roman", 15," bold") ,command=self.destroy_window,cursor="hand2",bg="red").place(x=1400,y=60,width=100,height=30)




    def email(self):
        with open('attendance_report/Student_daily_record.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for line in reader:
                text = "Hello " + line[0] + ", you were marked present today."
                send_email = line[1]
                print(send_email)
                msg = MIMEMultipart()
                msg['From'] = email_user
                msg['To'] = send_email
                msg['Subject'] = subject
                msg.attach(MIMEText(text, "plain"))

                text = msg.as_string()

                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()  # Use STARTTLS encryption

                server.login(email_user, email_password)
                print("login successfull")
                server.sendmail(email_user, send_email, text)
                server.quit()


    def sms(self):
        with open('attendance_report/Student_daily_record.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for line in reader:
                text = "Hello " + line[0] + ", you were marked present today."
                print(text)
                phone_number = line[2]

                # Send SMS
                message = client.messages.create(
                    body=text,
                    from_=twilio_phone_number,
                    to=phone_number
                )
                print(f"SMS sent to {line[0]} with SID: {message.sid}")

    def destroy_window(self):
        self.root.destroy()  # Destroy the root window

if __name__ == "__main__":
    root=Tk()
    obj=send_notification(root)
    root.mainloop()