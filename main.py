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
    
    

def go_to_prof_page():
    clear_frame()



root = Tk()
frame = Frame(root)
frame.pack(fill="both", expand = True)
root.geometry("400x200")
root.title('Easy UofA Lab Finder')

go_to_main_page()

root.mainloop()