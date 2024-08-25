from tkinter import *
from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000")

db = client.oppurtunitiesdb

opps = db.opps 

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

    global profName
    global profEmail
    global gradVar
    global uGradVar

    profText = Label(frame, text = 'My full name is...', font=("Times New Roman", 14))
    profText.pack()

    nameEntry = Entry(frame, textvariable = profName, font=("Times New Roman", 14))
    nameEntry.pack(pady=10)

    profText2 = Label(frame, text = 'My UofA email is...', font=("Times New Roman", 14))
    profText2.pack()

    emailEntry = Entry(frame, textvariable = profEmail, font=("Times New Roman", 14))
    emailEntry.pack(pady=10)

    profText3 = Label(frame, text = 'I am looking for ...', font=("Times New Roman", 14))
    profText3.pack()

    grads = Checkbutton(frame, text = "Grad(s)", variable = gradVar, onvalue = 1, offvalue = 0)
    grads.pack()
    uGrads = Checkbutton(frame,text = "UnderGrad(s)", variable = uGradVar, onvalue = 1, offvalue = 0)
    uGrads.pack()

    nextButton = Button(frame, text = "Next",font = ("Times New Roman", 20), command = lambda: go_to_prof2_page())
    nextButton.pack()

    backButton = Button(frame, text = "Back",font = ("Times New Roman", 20), command = lambda: go_to_main_page())
    backButton.pack()

    frame.update_idletasks() # This makes the entries render.

def go_to_prof2_page():
    clear_frame()
    
    global paidVar
    global volunteerVar
    global gResearchVar
    global iStudyVar

    profText = Label(frame, text = 'This is a...', font=("Times New Roman", 20))
    profText.pack()

    paid = Checkbutton(frame, text = "paid", variable = paidVar, onvalue = 1, offvalue = 0)
    paid.pack()
    paidText = Label(frame, text = "(Leave blank for unpaid)")
    paidText.pack()

    profText2 = Label(frame, text = '...', font=("Times New Roman", 20))
    profText2.pack()

    volunteer = Checkbutton(frame, text = "volunteer", variable = volunteerVar, onvalue = 1, offvalue = 0)
    volunteer.pack()
    gradR = Checkbutton(frame,text = "grad research", variable = gResearchVar, onvalue = 1, offvalue = 0)
    gradR.pack()
    iStudy = Checkbutton(frame, text = "independent study", variable = iStudyVar, onvalue = 1, offvalue = 0)
    iStudy.pack()

    profText3 = Label(frame, text = '...oppurtunity.', font=("Times New Roman", 20))
    profText3.pack()
    
    nextButton = Button(frame, text = "Next",font = ("Times New Roman", 20), command = lambda: go_to_prof3_page())
    nextButton.pack()

    backButton = Button(frame, text = "Back",font = ("Times New Roman", 20), command = lambda: go_to_prof_page())
    backButton.pack()

    frame.update_idletasks()



def go_to_prof3_page():
    clear_frame()

    global desc

    profText = Label(frame, text = 'Finally, add a description for the position', font=("Times New Roman", 20) )
    profText.pack()

    descEntry = Entry(frame, textvariable = desc, font=("Times New Roman", 14))
    descEntry.pack(pady=10)

    finishButton = Button(frame, text = "Finish",font = ("Times New Roman", 20), command = lambda: pp(profName, profEmail))
    finishButton.pack()

    backButton = Button(frame, text = "Back",font = ("Times New Roman", 20), command = lambda: go_to_prof2_page())
    backButton.pack()

    frame.update_idletasks()

def pp(name, email):
    print(name.get())
    print(email.get())
    print(desc.get())
    print(uGradVar.get())
    print(gradVar.get())
    print(volunteerVar.get())
    print(gResearchVar.get())
    print(iStudyVar.get())

root = Tk()
frame = Frame(root)
frame.pack(fill="both", expand = True)
root.geometry("800x500")
root.title('Easy UofA Lab Finder')

# All global variables using this library must be declared after root = Tk().
global profName
global profEmail 
global desc
profName = StringVar()
profEmail = StringVar()
desc = StringVar()
global gradVar
global uGradVar
global paidVar
global volunteerVar
global gResearchVar
global iStudyVar
gradVar = IntVar()
uGradVar = IntVar()
paidVar = IntVar() 
volunteerVar = IntVar()
gResearchVar = IntVar()
iStudyVar = IntVar()

go_to_main_page()

root.mainloop()