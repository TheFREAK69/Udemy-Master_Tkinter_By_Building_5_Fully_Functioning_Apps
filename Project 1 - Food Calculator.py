from tkinter import *

main_window = Tk()
main_window.title('Food Calculator')
main_window.geometry('300x200')
main_window.resizable(width=FALSE, height=FALSE)
main_window_bg_colour = 'gray77' # Set this as a variable that can be used across the code
main_window.configure(bg=main_window_bg_colour)


main_label = Label(main_window, text="Choose your fruit")
main_label.place(relx=0.5, y=15, anchor=CENTER)
main_label.configure(bg=main_window_bg_colour)

radio_button_variable = IntVar() # Define variable as integer
price_result = IntVar() # Define variable as integer


def calculate_price():
    radio_button_value = int(radio_button_variable.get()) # Make sure this variable is an integer
    input_weight_value = int(input_weight_entry.get()) # Make sure this variable is an integer
    price = radio_button_value * input_weight_value # Make the calculations and assign the value to a variable
    price_result.set(price) # Set the "price_result" variable as the value of the "price" variable

    # price_result.set(int(radio_button_variable.get()) * int(input_weight_entry.get())) # Same as the above in one line


radio_button_apple = Radiobutton(main_window, text="Apple", variable=radio_button_variable, value=10)
radio_button_apple.place(x=5, y=40)
radio_button_apple.configure(bg=main_window_bg_colour)

radio_button_banana = Radiobutton(main_window, text="Banana", variable=radio_button_variable, value=11)
radio_button_banana.place(x=5, y=60)
radio_button_banana.configure(bg=main_window_bg_colour)

radio_button_orange = Radiobutton(main_window, text="Grapes", variable=radio_button_variable, value=15)
radio_button_orange.place(x=5, y=80)
radio_button_orange.configure(bg=main_window_bg_colour)

radio_button_apple = Radiobutton(main_window, text="Kiwi", variable=radio_button_variable, value=12)
radio_button_apple.place(x=100, y=40)
radio_button_apple.configure(bg=main_window_bg_colour)

radio_button_banana = Radiobutton(main_window, text="Pear", variable=radio_button_variable, value=8)
radio_button_banana.place(x=100, y=60)
radio_button_banana.configure(bg=main_window_bg_colour)

radio_button_orange = Radiobutton(main_window, text="Orange", variable=radio_button_variable, value=5)
radio_button_orange.place(x=100, y=80)
radio_button_orange.configure(bg=main_window_bg_colour)


input_weight_entry = Entry(main_window, width=10) # Set this variable as an "entry" type one in the window called "main_window"
input_weight_entry.place(x=100, y=130)

input_weight_entry_label = Label(main_window, text="Weight (kg): ")
input_weight_entry_label.place(x=5, y=132)
input_weight_entry_label.configure(bg=main_window_bg_colour)

calculate_price_entry = Entry(main_window, width=10, textvariable=price_result) # Output the "price_result" variable value
calculate_price_entry.place(x=100, y=160)

calculate_price_button = Button(main_window, text='Calc', command= lambda : calculate_price()) # When clicked run the "calculate_price" function
calculate_price_button.place(x=50, y=162)
calculate_price_button.configure(highlightbackground=main_window_bg_colour)

main_window.mainloop()