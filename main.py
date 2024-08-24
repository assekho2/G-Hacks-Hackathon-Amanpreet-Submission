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
    frame.update_idletasks() # This makes the entry render.

    nextButton = Button(frame, text = "Next",font = ("Times New Roman", 20))
    nextButton.pack()

    backButton = Button(frame, text = "Back",font = ("Times New Roman", 20), command = lambda: go_to_main_page())
    backButton.pack()


    
def go_to_prof_page():
    clear_frame()

    profText = Label(frame, text = 'My full name is...', font=("Times New Roman", 14))
    profText.pack()

    profName = StringVar(value = '')
    nameEntry = Entry(frame, textvariable = profName, font=("Times New Roman", 14))
    nameEntry.pack(pady=10)

    profText2 = Label(frame, text = 'My UofA email is...', font=("Times New Roman", 14))
    profText2.pack()

    profEmail = StringVar(value = '')
    emailEntry = Entry(frame, textvariable = profEmail, font=("Times New Roman", 14))
    emailEntry.pack(pady=10)

    profText3 = Label(frame, text = 'I am looking for ...', font=("Times New Roman", 14))
    profText3.pack()

    grads = Checkbutton(frame, text = "Grad(s)")
    grads.pack()
    uGrads = Checkbutton(frame,text = "UnderGrad(s)")
    uGrads.pack()

    nextButton = Button(frame, text = "Next",font = ("Times New Roman", 20), command = lambda: go_to_prof2_page())
    nextButton.pack()

    backButton = Button(frame, text = "Back",font = ("Times New Roman", 20), command = lambda: go_to_main_page())
    backButton.pack()

    frame.update_idletasks() # This makes the entries render.

def go_to_prof2_page():
    clear_frame()

    profText = Label(frame, text = 'This is a...', font=("Times New Roman", 20))
    profText.pack()

    paid = Checkbutton(frame, text = "paid")
    paid.pack()
    uPaid = Checkbutton(frame,text = "unpaid")
    uPaid.pack()

    profText2 = Label(frame, text = '...', font=("Times New Roman", 20))
    profText2.pack()

    volunteer = Checkbutton(frame, text = "volunteer")
    volunteer.pack()
    gradR = Checkbutton(frame,text = "grad research")
    gradR.pack()
    iStudy = Checkbutton(frame, text = "independent study")
    iStudy.pack()

    profText3 = Label(frame, text = '...oppurtunity.', font=("Times New Roman", 20))
    profText3.pack()
    
    finishButton = Button(frame, text = "Finish",font = ("Times New Roman", 20))
    finishButton.pack()

    backButton = Button(frame, text = "Back",font = ("Times New Roman", 20), command = lambda: go_to_prof_page())
    backButton.pack()



    frame.update_idletasks()


root = Tk()
frame = Frame(root)
frame.pack(fill="both", expand = True)
root.geometry("800x500")
root.title('Easy UofA Lab Finder')

go_to_main_page()

root.mainloop()