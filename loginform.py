from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
def handle_login():
        email=email_input.get()
        password=Password_input.get()
        if email=='sinhashivani312@gmail.com' and password=='1234':
           messagebox.showinfo('yes','Login Successful')
        else:   
                messagebox.showinfo('error','Login failed')
root=Tk()
root.title("Login Form")

#set the position of the window
root.geometry('350x500')

#allow you to modify the parametres of a widget
root.configure(background='sky blue')

img=Image.open('login.png')

#return a resize copy of this image
resize_img=img.resize((100,100))
img=ImageTk.PhotoImage(resize_img)
img_label=Label(root,image=img)

#organizes widgets in horizontal and vertical boxesgit
img_label.pack(pady=(20,20))
text_label=Label(root,text='Login form',fg='black',bg='white')
text_label.pack()

#to change the label content
text_label.config(font=('monospace',24))
email_label=Label(root,text='Enter Email',fg='white',bg='black')
email_label.pack(pady=(20,5))
email_label.config(font=('monospace',14))
email_input=Entry(root,width=50)
email_input.pack(ipady=4,pady=(1,15))
Password_label=Label(root,text='Enter Password',fg='white',bg='black')
Password_label.pack(pady=(20,5))
Password_label.config(font=('monospace',14))
Password_input=Entry(root,width=50)
Password_input.pack(ipady=4,pady=(1,15))
login_btn=Button(root,text='Login Here',bg='white',fg='black',width=20,height=2,command=handle_login)
login_btn.pack(pady=(10,20))
root.mainloop()
