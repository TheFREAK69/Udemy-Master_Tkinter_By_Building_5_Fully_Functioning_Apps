########################################################################################################################
#
# DATE: 2018-05-01
#
# RELEASE Notes:
#   - Email function not working.
#   - Everything else is ok.
#
########################################################################################################################


#============================================= Tkinter Settings =======================================================#


from tkinter import *   # Not ready because cannot send mail.
from smtplib import SMTP_SSL as SMTP
from email.mime.text import MIMEText


#============================================= Main Window Settings ===================================================#


main_window = Tk()
main_window.title('Email Sender app')
main_window.geometry('800x500')
main_window.resizable(width=FALSE, height=FALSE)
main_window_bg_colour = 'gray30' # Set this as a variable that can be used across the code
main_window.configure(bg=main_window_bg_colour)


#============================================= Variables ==============================================================#


send_from_variable = StringVar()
send_to_variable = StringVar()
email_message_variable = StringVar()


#============================================= Functions ==============================================================#


def clear_from_function():
    send_from_entry.delete(0, END)


def clear_to_function():
    send_to_entry.delete(0, END)


def clear_all_function():
    clear_from_function()
    clear_to_function()
    email_message.delete('1.0', END)


def send_email_function():
    HOST = 'smtp.gmail.com'
    PORT = 465

    USERNAME = send_from_entry.get()
    PASSWORD = 'Appolo!7'

    SENDER = send_from_entry.get()
    RECIPIENT = send_to_entry.get()

    text_subtype = 'plain'

    msg = MIMEText('text', text_subtype)

    msg['Subject'] = 'Python Script'
    msg['From'] = SENDER
    msg['To'] = RECIPIENT

    try:
        connection = SMTP(HOST, PORT)
        connection.login(USERNAME, PASSWORD)
        connection.sendmail(SENDER, RECIPIENT, msg.as_string())
    except Exception as e:
        print(e)


#=============================================== Frames ===============================================================#


top_frame = Frame(main_window, width=900, height=50, bg=main_window_bg_colour)
top_frame.pack(side=TOP)

bottom_frame = Frame(main_window, width=800, height=50, bg='black')
bottom_frame.pack(side=BOTTOM)

left_frame = Frame(main_window, width=600, height=400, bg=main_window_bg_colour)
left_frame.pack(side=LEFT)

right_frame = Frame(main_window, width=200, height=400, bg=main_window_bg_colour)
right_frame.pack(side=RIGHT)




#=============================================== Buttons ==============================================================#


clear_from_button = Button(right_frame, text="Clear From", width=10, highlightbackground=main_window_bg_colour,
                           command=lambda : clear_from_function())
clear_from_button.pack(side=TOP, padx=(0,8), pady=(0,5))

clear_to_button = Button(right_frame, text="Clear To", width=10, highlightbackground=main_window_bg_colour,
                         command=lambda: clear_to_function())
clear_to_button.pack(side=TOP, padx=(0,8), pady=(0,5))

clear_all_button = Button(right_frame, text="Clear All", width=15, highlightbackground=main_window_bg_colour,
                          command=lambda: clear_all_function())
clear_all_button.pack(side=TOP, padx=(0,8), pady=(0,5))

send_button = Button(right_frame, text="Send Email", width=20, highlightbackground=main_window_bg_colour,
                     command=lambda: send_email_function())
send_button.pack(side=TOP, padx=(0,8), pady=(20,0))

#=========================================== Labels + Entries =========================================================#


send_from_label = Label(top_frame, text="From:", font=('', 25, 'bold'), fg='white', bg=main_window_bg_colour)
send_from_label.pack(side=LEFT, padx=(0,0), pady=(5,5))

send_from_entry = Entry(top_frame, width=30, textvariable=send_from_variable, fg='white', font=('', 15),
                        bg=main_window_bg_colour, bd=4)
send_from_entry.pack(side=LEFT, padx=(0,10), pady=(5,5))


send_to_label = Label(top_frame, text="To:", font=('', 25, 'bold'), fg='white', bg=main_window_bg_colour)
send_to_label.pack(side=LEFT, padx=(0,0), pady=(5,5))

send_to_entry = Entry(top_frame, width=30, textvariable=send_to_variable, fg='white', font=('', 15),
                      bg=main_window_bg_colour, bd=4)
send_to_entry.pack(side=LEFT, padx=(0,10), pady=(5,5))


#==================================================== Text ============================================================#


email_message = Text(left_frame, font=('', 15), width=59, bg='white')
email_message.pack(side=LEFT, padx=(1,1), pady=(1,1))


#================================================== Main Loop =========================================================#


main_window.mainloop()