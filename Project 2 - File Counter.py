#pip install more-itertools
from tkinter import *
from tkinter import filedialog
from more_itertools import unique_everseen

main_window = Tk()
main_window.title('File Counter')
main_window.geometry('500x500')
main_window.resizable(width=FALSE, height=FALSE)
main_window_bg_colour = 'gray77' # Set this as a variable that can be used across the code
main_window.configure(bg=main_window_bg_colour)


main_label_01 = Label(main_window, text="Welcome to the Word Counter app.\n Please follow these steps:\n")
main_label_01.place(relx=0.5, y=30, anchor=CENTER)
main_label_01.configure(bg=main_window_bg_colour)

main_label_02 = Label(main_window, text="1 - Write the words you want to search seperated by a comma (,)\n"
"2 - Press the Select File button and select the text file you want to search\n"
"3 - Press the Count Words button")
main_label_02.place(x=5, y=40)
main_label_02.configure(bg=main_window_bg_colour)


def open_file():
    main_window.filename = filedialog.askopenfilename()

def clear_text():
    input_word_list_entry.delete(0, END)# Since this is a entry field, we specify the index number we want to start deleting
    result_area.delete('1.0', END) # Since this is a text field, we specify the line number we want to start deleting


#######################################################################################################################
#                       #
# Function "count_text" #
#                       #
#########################

count_text_results = {}
#count_text_results = dict() # Another way to creat a dictionary

def count_text(file):
    result_area.delete('1.0', END)
    file_open = open(str(file), 'r')
    read_file = file_open.readlines()
    #print(read_file)
    file_open.close()
    word_list_formated = input_word_list_entry.get().split(',') # Splits the words and adds them to a list
    radio_button_value = int(radio_button_variable.get())
    #print(word_list_formated)
    #print(radio_button_value)



    # This loop makes sure the words have a space before and after so they are evaluated
    #  as a word and not just part of a word
    x = 0
    counter_variable_loop = len(word_list_formated)
    while x < counter_variable_loop:
    #for item in word_list_formated:
        if radio_button_value == 1:
            word_list_formated[x] = word_list_formated[x].strip()# Striping any unwanted leading or trailing spaces
            word_list_formated[x] = ' ' + word_list_formated[x] + ' '
        else:
            print(x)
            word_list_formated[x] = word_list_formated[x].strip().lower()
            word_list_formated[x] = ' ' + word_list_formated[x] + ' '
            print(word_list_formated[x])
            word_list_formated_append_temp = word_list_formated[x].strip().title()
            print(word_list_formated_append_temp)
            x = x + 1
            word_list_formated.insert(x, ' ' + word_list_formated_append_temp + ' ')
            word_list_formated_append_temp = word_list_formated[x].strip().upper()
            print(word_list_formated_append_temp)
            x = x + 1
            word_list_formated.insert(x, ' ' + word_list_formated_append_temp + ' ')
            print(x)


        #print(word_list_formated)
        x = x + 1
        print(x)
        counter_variable_loop = len(word_list_formated)
        print(counter_variable_loop)
    print(word_list_formated)
    word_list_formated = list(unique_everseen(word_list_formated))
    print(word_list_formated)

    for word in word_list_formated:
        # This loop adds values to the dictionary
        # If true it adds the word plus how many times it is found
        # If false it adds the word plus the value 0
        for word_count in read_file:
            if word in count_text_results:
                count_text_results[word] = count_text_results[word] + word_count.count(word)
            else:
                count_text_results[word] = word_count.count(word)
    print(count_text_results)

    for k, v in count_text_results.items():
        result_area.insert('1.0', '{0} {1} \n'.format(k, v))

    # This clears the dictionary so if we press the "count" button again it provides the correct numbers
    count_text_results.clear()

#######################################################################################################################
#######################################################################################################################

radio_button_variable = IntVar() # Define variable as integer

radio_button_case_sensitive = Radiobutton(main_window, text="Case Sensitive", variable=radio_button_variable, value=1)
radio_button_case_sensitive.place(x=10, y=140)
radio_button_case_sensitive.configure(bg=main_window_bg_colour)

radio_button_no_case_sensitive = Radiobutton(main_window, text="No Case Sensitive", variable=radio_button_variable, value=2)
radio_button_no_case_sensitive.place(x=10, y=165)
radio_button_no_case_sensitive.configure(bg=main_window_bg_colour)


input_word_list_entry = Entry(main_window, width=50) # Set this variable as an "entry" type one in the window called "main_window"
input_word_list_entry.place(relx=0.5, y=120, anchor=CENTER)


select_file_button = Button(main_window, text="Select File", width=10, command=lambda : open_file())
select_file_button.place(x=170, y=149)
select_file_button.configure(highlightbackground=main_window_bg_colour)

count_words_button = Button(main_window, text="Count Words", width=10, command=lambda : count_text(main_window.filename))
count_words_button.place(x=275, y=149)
count_words_button.configure(highlightbackground=main_window_bg_colour)

clear_text_button = Button(main_window, text="Clear Text", width=10, command=lambda : clear_text())
clear_text_button.place(x=380, y=149)
clear_text_button.configure(highlightbackground=main_window_bg_colour)

result_area = Text(main_window, height=19, width=69)
result_area.place(x=4, y=200)
result_area.configure(bg=main_window_bg_colour)


main_window.mainloop()