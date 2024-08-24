from tkinter import *

def go_to_main_page():
    openingText = Label(root, text = "I am a...", font = ("Times New Roman", 30))
    openingText.pack()

    studentButton = Button(root, text = 'Student', font = ("Times New Roman", 20), command = lambda: stud_func())
    studentButton.pack()

    professorButton = Button(root, text = 'Professor', font = ("Times New Roman", 20), command = lambda: prof_func())
    professorButton.pack()

def clear_frame():
    for widget in frame.winfo_children():
        widget.destroy()


def stud_func():
    clear_frame()
    openingText = Label(root, text = "bark bark bark", font = ("Times New Roman", 30))
    openingText.pack()


def prof_func():
    return


root = Tk()
frame = Frame(root)
root.geometry("400x200")
root.title('Easy UofA Lab Finder')

go_to_main_page()

root.mainloop()