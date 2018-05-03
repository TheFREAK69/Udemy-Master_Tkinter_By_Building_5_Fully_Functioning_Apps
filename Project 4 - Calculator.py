#============================================= Tkinter Settings =======================================================#


from tkinter import *
import tkinter.messagebox


#============================================= Main Window Settings ===================================================#


main_window = Tk()
main_window.title('Calculator app')
main_window.geometry('400x150')
main_window.resizable(width=FALSE, height=FALSE)
main_window_bg_colour = 'gray55' # Set this as a variable that can be used across the code
main_window.configure(bg=main_window_bg_colour)


#============================================= Variables ==============================================================#


first_number_var = StringVar()
second_number_var = StringVar()
result_number_var = StringVar()


#============================================= Functions ==============================================================#


def error_message(message):
    if message == 'error':
        tkinter.messagebox.showinfo('Error!', 'Something went wrong!!')
    elif message == 'divisionerror':
        tkinter.messagebox.showinfo('Division Error!', 'Cannot divide by 0!')



def plus_function():
    try:
        value = float(first_number_var.get()) + float(second_number_var.get())
        result_number_var.set(value)
    except:
        error_message('error')


def minus_function():
    try:
        value = float(first_number_var.get()) - float(second_number_var.get())
        result_number_var.set(value)
    except:
        error_message('error')


def multiply_function():
    try:
        value = float(first_number_var.get()) * float(second_number_var.get())
        result_number_var.set(value)
    except:
        error_message('error')


def divide_function():
    if second_number_var.get() == '0':
        error_message('divisionerror')
    elif second_number_var.get() != '0':
        try:
            value = float(first_number_var.get()) / float(second_number_var.get())
            result_number_var.set(value)
        except:
            error_message('error')


#=============================================== Frames ===============================================================#


first_frame = Frame(main_window, width=800, height=35, bg=main_window_bg_colour)
first_frame.pack(side=TOP)

second_frame = Frame(main_window, width=800, height=35, bg=main_window_bg_colour)
second_frame.pack(side=TOP)

third_frame = Frame(main_window, width=800, height=40, bg=main_window_bg_colour)
third_frame.pack(side=TOP)

fourth_frame = Frame(main_window, width=800, height=40, bg=main_window_bg_colour)
fourth_frame.pack(side=TOP)


#=============================================== Buttons ==============================================================#


plus_button = Button(third_frame, text='+', width=9, highlightbackground=main_window_bg_colour,
                     command=lambda : plus_function())
plus_button.pack(side=LEFT, padx=5, pady=9)

minus_button = Button(third_frame, text='-', width=9, highlightbackground=main_window_bg_colour,
                      command=lambda: minus_function())
minus_button.pack(side=LEFT, padx=5, pady=9)

multiply_button = Button(third_frame, text='*', width=9, highlightbackground=main_window_bg_colour,
                         command=lambda: multiply_function())
multiply_button.pack(side=LEFT, padx=5, pady=9)

divide_button = Button(third_frame, text='/', width=9, highlightbackground=main_window_bg_colour,
                       command=lambda: divide_function())
divide_button.pack(side=LEFT, padx=5, pady=9)


#=========================================== Labels + Entries =========================================================#


label_first_number = Label(first_frame, text='Enter first number: ', bg=main_window_bg_colour)
label_first_number.pack(side=LEFT, padx=(23, 1), pady=5)

entry_first_number = Entry(first_frame, width=22, textvariable=first_number_var,
                           highlightbackground=main_window_bg_colour)
entry_first_number.pack(side=LEFT)


label_second_number = Label(second_frame, text='Enter second number: ', bg=main_window_bg_colour)
label_second_number.pack(side=LEFT, padx=(1, 1), pady=5)

entry_second_number = Entry(second_frame, width=22, textvariable=second_number_var,
                            highlightbackground=main_window_bg_colour)
entry_second_number.pack(side=LEFT)


label_output = Label(fourth_frame, text='Result: ', bg=main_window_bg_colour)
label_output.pack(side=LEFT, padx=(1, 1), pady=5)

entry_output = Entry(fourth_frame, width=33, textvariable=result_number_var,
                     highlightbackground=main_window_bg_colour)
entry_output.pack(side=LEFT, padx=(1, 1), pady=5)


#============================================== Main Loop =============================================================#


main_window.mainloop()