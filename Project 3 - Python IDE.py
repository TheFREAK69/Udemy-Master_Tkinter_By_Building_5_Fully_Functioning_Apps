from tkinter import *
import tkinter.messagebox
from io import StringIO

main_window = Tk()
main_window.title('Python IDE app')
main_window.geometry('800x500')
main_window.resizable(width=FALSE, height=FALSE)
main_window_bg_colour = 'gray55' # Set this as a variable that can be used across the code
main_window.configure(bg=main_window_bg_colour)


def clear_python():
    python_code_entry.delete('1.0', END)

def run_python():
    # run python code.
    # show python code to user.
    old_stdout = sys.stdout
    redirect_output = sys.stdout = StringIO()
    exec(python_code_entry.get('1.0', END))
    sys.stdout = old_stdout

    tkinter.messagebox.showinfo('Output', redirect_output.getvalue())


top_frame = Frame(main_window, width=800, height=150, bg=main_window_bg_colour)
top_frame.pack(side=TOP)


#middle_frame = Frame(main_window, width=800, height=200, bg='red')
#middle_frame.pack(side=TOP)


bottom_frame = Frame(main_window, width=800, height=350, bg='black')
bottom_frame.pack(side=BOTTOM)


button_clear = Button(top_frame, width=10, text="Clear", font=('', 14, 'bold'), command= lambda : clear_python())
button_clear.configure(highlightbackground=main_window_bg_colour)
button_clear.pack(side=TOP)


button_run = Button(top_frame, text="RUN", font=('', 14, 'bold'), command= lambda : run_python())
button_run.configure(highlightbackground=main_window_bg_colour)
button_run.pack(side=TOP)


python_code_entry = Text(bottom_frame, font=('', 14, 'bold'))
python_code_entry.configure(bg='gray77')
python_code_entry.pack(side=BOTTOM)

#python_code_output = Text(bottom_frame, width=800, height=200, font=('', 14, 'italic'))
#python_code_output.configure(bg='black')
#python_code_output.pack(side=BOTTOM)

main_window.mainloop()