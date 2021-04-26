from tkinter import *
import smtplib
from tkinter import messagebox

f = Tk()
f.title("Email App")

send_email=StringVar()
send_pass=StringVar()
recv_email=StringVar()

sender_email= Label(f, text="Sender’s Gmail ID: ")
sender_entry= Entry(f, textvariable=send_email,bd=3)
sender_pass= Label(f, text="Sender’s Gmail Pass: ")
sender_passentry = Entry(f, show='*', textvariable=send_pass,bd=3)

receiver_email=Label(f, text="Receiver’s Email: ")
receiver_entry=Entry(f, textvariable=recv_email, bd=3)

msg_label=Label(f, text='Message')
msg_body=Text(f, height=10, width=25, bd=3)

status_message = "Message sent successfully...."

def msg_box():
    messagebox.showinfo("Email Info", "Mail Sent")

def mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    sender_emailID = send_email.get()
    sender_password = send_pass.get()
    message = msg_body.get('1.0', END)
    receiver_emailID = recv_email.get()
    server.login(sender_emailID, sender_password)
    server.sendmail(sender_emailID, receiver_emailID, message)
    server.close()
    msg_box()
    print(status_message)


send=Button(f, text='Send', width=15, command=mail, bd=3)


def destroy():
    f.destroy()

cancel=Button(f, text='Cancel', width=15, command=destroy, bd=3)

sender_email.grid(row=0, column=0, padx=5, pady=3)
sender_entry.grid(row=0, column=1, padx=5, pady=3)
sender_pass.grid(row=1, column=0, padx=5, pady=3)
sender_passentry.grid(row=1, column=1, padx=5, pady=3)
receiver_email.grid(row=2, column=0, padx=5, pady=3)
receiver_entry.grid(row=2, column=1, padx=5, pady=3)
msg_label.grid(row=3, column=0, padx=5, pady=3)
msg_body.grid(row=3, column=1, padx=5, pady=3)
send.grid(row=4, column=0, padx=5, pady=3)
cancel.grid(row=4, column=1, padx=5, pady=3)
f.mainloop()