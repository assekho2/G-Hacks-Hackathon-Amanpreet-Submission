from tkinter import *
from pymongo import MongoClient
from datetime import datetime

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

    searchButton = Button(frame, text = "Search",font = ("Times New Roman", 20))
    searchButton.pack()

    searchNButton = Button(frame, text = "Search with no key words",font = ("Times New Roman", 20), command = lambda: go_to_stud2_page())
    searchNButton.pack()

    backButton = Button(frame, text = "Back",font = ("Times New Roman", 20), command = lambda: go_to_main_page())
    backButton.pack()

def go_to_stud2_page():
    clear_frame()
    
    # Set up the canvas and scrollbar
    canvas = Canvas(frame)
    scrollbar = Scrollbar(frame, orient="vertical", command=canvas.yview)
    entry_frame = Frame(canvas)
    
    canvas.create_window((0, 0), window=entry_frame, anchor="nw")
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Fetch entries from the database
    entries = opps.find()
    
    # Display each entry in the entry_frame
    for entry in entries:
        entry_text = f"Entry ID: {entry.get('_id')}\n"
        for key, value in entry.items():
            if key != '_id':
                entry_text += f"{key}: {value}\n"
        entry_label = Label(entry_frame, text=entry_text, relief="ridge", padx=10, pady=10)
        entry_label.pack(pady=5, fill="x")

    # Update the canvas scroll region and center the entry_frame
    entry_frame.update_idletasks()  # Ensure the frame is updated
    canvas.config(scrollregion=canvas.bbox("all"))
    
    # Center the frame in the canvas
    canvas_width = canvas.winfo_width()
    entry_frame_width = entry_frame.winfo_reqwidth()

    x = (canvas_width - entry_frame_width) // 2
    y = 0  # Start from the top of the canvas

    canvas.create_window((x, y), window=entry_frame, anchor="nw")

    # Set the scrollbar to the top
    canvas.yview_moveto(0)

    # Add a back button
    backButton = Button(frame, text="Back", font=("Times New Roman", 20), command=lambda: go_to_main_page())
    backButton.pack(pady=10)

    # Update the canvas scroll region
    canvas.config(scrollregion=canvas.bbox("all"))





def go_to_prof_page():
    clear_frame()

    global profName
    global profEmail
    global profSite
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

    profSiteText = Label(frame, text = 'The link to my UofA homepage is...', font=("Times New Roman", 14))
    profSiteText.pack()

    siteEntry = Entry(frame, textvariable = profSite, font=("Times New Roman", 14))
    siteEntry.pack(pady=10)

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
    global date

    profText = Label(frame, text = 'Add a description for the position.', font=("Times New Roman", 20) )
    profText.pack()

    descEntry = Entry(frame, textvariable = desc, font=("Times New Roman", 14))
    descEntry.pack(pady=10)

    profText2 = Label(frame, text = "Enter the application deadline. (YYYY-MM-DD):", font=("Times New Roman", 20))
    profText2.pack()

    dateEntry = Entry(frame, textvariable = date, font=("Times New Roman", 14))
    dateEntry.pack(pady=10)

    finishButton = Button(frame, text = "Finish",font = ("Times New Roman", 20), command = lambda: pp())
    finishButton.pack()

    backButton = Button(frame, text = "Back",font = ("Times New Roman", 20), command = lambda: go_to_prof2_page())
    backButton.pack()

    frame.update_idletasks()

def pp():
    specifiedDate = datetime.strptime(date.get(), "%Y-%m-%d")
    opps.insert_one({"Professors Name":profName.get(), "Professors email": profEmail.get(), "Professors Website":profSite.get(), "Description":desc.get(), "Application Deadline":specifiedDate, "graduate": gradVar.get(), "undergrad":uGradVar.get(), "compensation":paidVar.get(), "volunteer":volunteerVar.get(), 'grad_research':gResearchVar.get(), 'independent_study': iStudyVar.get()})

root = Tk()
frame = Frame(root)
frame.pack(fill="both", expand = True)
root.geometry("800x500")
root.title('Easy UofA Lab Finder')

# All global variables using this library must be declared after root = Tk().
global profName
global profEmail 
global profSite
global desc
global date
profName = StringVar()
profEmail = StringVar()
profSite = StringVar()
desc = StringVar()
date = StringVar()
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