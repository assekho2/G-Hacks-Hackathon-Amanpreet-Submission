from tkinter import *

def clear_frame():
    for widget in frame.winfo_children():
        widget.destroy()

def go_to_main_page():
    clear_frame()
    openingText = Label(frame, text = "I am a...", font = ("Times New Roman", 30))
    openingText.pack()

    studentButton = Button(frame, text = 'Student', font = ("Times New Roman", 20), command = lambda: go_to_stud_page())
    studentButton.pack()

    professorButton = Button(frame, text = 'Professor', font = ("Times New Roman", 20), command = lambda: go_to_prof_page())
    professorButton.pack()

def go_to_stud_page():
    clear_frame()
    studText = Label(frame, text = 'Enter keywords to search professors by. Sepearted by commas like so, "Computer Science, Machine Learning, AI". Case insensitive', font = ("Times New Roman", 20), wraplength= 800)
    studText.pack()
    keyWords = StringVar(value = '')
    keyWordEntry = Entry(frame, textvariable = keyWords, font=("Times New Roman", 14))
    keyWordEntry.pack(pady=10)
    frame.update_idletasks()
    nextButton = Button(frame, text = "Next",font = ("Times New Roman", 20))
    nextButton.pack()

    

def go_to_prof_page():
    clear_frame()



root = Tk()
frame = Frame(root)
frame.pack(fill="both", expand = True)
root.geometry("800x500")
root.title('Easy UofA Lab Finder')

go_to_main_page()

root.mainloop()