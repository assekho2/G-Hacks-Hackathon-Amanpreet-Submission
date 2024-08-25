import constants as c
import imports as i

client = i.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000")
db = client.oppurtunitiesdb
opps = db.opps

# Helper function to get keywords
def keyword_parser(keywords):
    # Split the input string by commas and strip any leading or trailing whitespace from each keyword
    keywordList = [keyword.strip() for keyword in keywords.split(',')]
    return keywordList

# Helper function to clear pages
def clear_frame():
    for widget in frame.winfo_children():
        widget.destroy()

# Helper function to create the descriptive text
def format_description(entry):
    description = ""
    
    # Determine student type
    if entry.get('graduate') == 1 and entry.get('undergrad') == 1:
        description += "This position is for undergraduate and graduate students. "
    elif entry.get('graduate') == 1:
        description += "This position is for graduate students. "
    elif entry.get('undergrad') == 1:
        description += "This position is for undergraduate students. "

    # Determine compensation
    if entry.get('compensation') == 1:
        description += "This position is paid. "
    else:
        description += "This position is unpaid. "
    
    # Determine available positions
    positions = []
    if entry.get('volunteer') == 1:
        positions.append("volunteer")
    if entry.get('grad_research') == 1:
        positions.append("graduate research")
    if entry.get('independent_study') == 1:
        positions.append("independent study")
    
    if positions:
        description += "The positions available are: " + ", ".join(positions) + "."
    
    return description

def go_to_main_page():
    clear_frame()

    openingText = i.Label(frame, text = "I am a...", font = ("Times New Roman", 30))
    openingText.pack()

    studentButton = i.Button(frame, text = 'Student', font = ("Times New Roman", 20), command = lambda: go_to_stud_page())
    studentButton.pack()

    professorButton = i.Button(frame, text = 'Professor', font = ("Times New Roman", 20), command = lambda: go_to_prof_page())
    professorButton.pack()

    descriptionText = i.Label(frame, text = c.description, font = ("Times New Roman", 18), wraplength=700)
    descriptionText.pack()

def go_to_stud_page():
    clear_frame()

    entries = opps.find()
    sKeyWords = []
    for entry in entries:
        for keyWord in entry.get("KeyWords", []):  # Add a default empty list to avoid NoneType error
            x = keyWord.lower()
            if x not in sKeyWords:
                sKeyWords.append(x)

    studText = i.Label(frame, text='Choose keywords to search professors by. Separated by commas like so, "Computer Science, Machine Learning, AI". Case insensitive', font=("Times New Roman", 20), wraplength=800)
    studText.pack()

    # Create a frame to center the Listbox
    listbox_frame = i.Frame(frame)
    listbox_frame.pack(padx=20, pady=20, fill="both", expand=True)

    # Create the Listbox
    keyword_listbox = i.Listbox(listbox_frame, selectmode=i.MULTIPLE, height=10)  # Adjust height as needed
    keyword_listbox.pack(pady=20, fill="x", expand=True)
    
    # Insert keywords into the Listbox
    for keyword in sKeyWords:
        keyword_listbox.insert(i.END, keyword)

    # Center the Listbox within the frame
    listbox_frame.grid_rowconfigure(0, weight=1)
    listbox_frame.grid_columnconfigure(0, weight=1)
    keyword_listbox.grid(row=0, column=0, padx=10, pady=10)

    frame.update_idletasks()  # This makes the entry render.

    # Update selected_keywords when the "Search" button is clicked
    searchButton = i.Button(
        frame,
        text="Search",
        font=("Times New Roman", 20),
        command=lambda: go_to_stud3_page([keyword_listbox.get(i) for i in keyword_listbox.curselection()])
    )
    searchButton.pack(pady=10)

    searchNButton = i.Button(frame, text="Search with no key words", font=("Times New Roman", 20), command=go_to_stud2_page)
    searchNButton.pack(pady=10)

    backButton = i.Button(frame, text="Back", font=("Times New Roman", 20), command=go_to_main_page)
    backButton.pack(pady=10)



def go_to_stud2_page():
    clear_frame()  # Clear the current frame to refresh the view
    
    canvas = i.Canvas(frame)
    scrollbar = i.Scrollbar(frame, orient="vertical", command=canvas.yview)
    entry_frame = i.Frame(canvas)
    
    # Create a window on the canvas to contain the entry_frame
    window_id = canvas.create_window((0, 0), window=entry_frame, anchor="nw")
    canvas.grid(row=0, column=0, sticky="nsew")
    scrollbar.grid(row=0, column=1, sticky="ns")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    # Configure grid row and column weights to make sure they expand properly
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    
    # Fetch entries from the database
    entries = opps.find()
    

    # Display each filtered entry in the entry_frame
    for entry in entries:
        entry_text = f"Professors Name: {entry.get('name')}\n"
        entry_text += f"Professors Email: {entry.get('email')}\n"
        entry_text += f"Website: {entry.get('site')}\n"
        entry_text += f"Description: {entry.get('description')}\n"
        entry_text += f"{format_description(entry)}\n"
        entry_text += f"Application Deadline: {entry.get('Application Deadline')}\n"
        entry_text += f"Keywords: {', '.join(entry.get('KeyWords'))}"
        
        entry_label = i.Label(entry_frame, text=entry_text, relief="ridge", padx=10, pady=10, anchor="w", justify="left")
        entry_label.pack(pady=5, fill="x")
    
    # Update the canvas scroll region
    entry_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    # Adjust the canvas scrolling region and position the window
    canvas_width = canvas.winfo_width()
    entry_frame_width = entry_frame.winfo_reqwidth()
    
    # Center the entry_frame within the canvas
    x = max(0, (canvas_width - entry_frame_width) // 2)
    y = 0  # Start from the top of the canvas

    # Update the position of entry_frame using the window ID
    canvas.coords(window_id, x, y)  # Adjust the window position
    canvas.yview_moveto(0)
    
    backButton = i.Button(frame, text="Back", font=("Times New Roman", 20), command=lambda: go_to_main_page())
    backButton.grid(row=1, column=0, pady=10, sticky="s")

    frame.grid_rowconfigure(0, weight=1)
    frame.grid_rowconfigure(1, weight=0)
    frame.grid_columnconfigure(0, weight=1)


def go_to_stud3_page(selected_keywords):
    clear_frame()  # Clear the current frame to refresh the view
    
    canvas = i.Canvas(frame)
    scrollbar = i.Scrollbar(frame, orient="vertical", command=canvas.yview)
    entry_frame = i.Frame(canvas)
    
    # Create a window on the canvas to contain the entry_frame
    window_id = canvas.create_window((0, 0), window=entry_frame, anchor="nw")
    canvas.grid(row=0, column=0, sticky="nsew")
    scrollbar.grid(row=0, column=1, sticky="ns")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    # Configure grid row and column weights to make sure they expand properly
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    
    # Fetch entries from the database
    entries = opps.find()
    
    # Filter entries based on the selected keywords
    filtered_entries = []
    for entry in entries:
        entry_keywords = [kw.lower() for kw in entry.get("KeyWords", [])]  # Lowercase keywords for case-insensitive matching
        for keyword in selected_keywords:
            if keyword.lower() in entry_keywords:
                filtered_entries.append(entry)
                break  # Stop checking after finding the first matching keyword

    # Display each filtered entry in the entry_frame
    for entry in filtered_entries:
        entry_text = f"Professors Name: {entry.get('name')}\n"
        entry_text += f"Professors Email: {entry.get('email')}\n"
        entry_text += f"Website: {entry.get('site')}\n"
        entry_text += f"Description: {entry.get('description')}\n"
        entry_text += f"{format_description(entry)}\n"
        entry_text += f"Application Deadline: {entry.get('Application Deadline')}\n"
        entry_text += f"Keywords: {', '.join(entry.get('KeyWords'))}"
        
        entry_label = i.Label(entry_frame, text=entry_text, relief="ridge", padx=10, pady=10, anchor="w", justify="left")
        entry_label.pack(pady=5, fill="x")
    
    # Update the canvas scroll region
    entry_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    # Adjust the canvas scrolling region and position the window
    canvas_width = canvas.winfo_width()
    entry_frame_width = entry_frame.winfo_reqwidth()
    
    # Center the entry_frame within the canvas
    x = max(0, (canvas_width - entry_frame_width) // 2)
    y = 0  # Start from the top of the canvas

    # Update the position of entry_frame using the window ID
    canvas.coords(window_id, x, y)  # Adjust the window position
    canvas.yview_moveto(0)
    
    backButton = i.Button(frame, text="Back", font=("Times New Roman", 20), command=lambda: go_to_main_page())
    backButton.grid(row=1, column=0, pady=10, sticky="s")

    frame.grid_rowconfigure(0, weight=1)
    frame.grid_rowconfigure(1, weight=0)
    frame.grid_columnconfigure(0, weight=1)



def go_to_prof_page():
    clear_frame()

    global profName
    global profEmail
    global profSite
    global gradVar
    global uGradVar

    profText = i.Label(frame, text = 'My full name is...', font=("Times New Roman", 14))
    profText.pack()

    nameEntry = i.Entry(frame, textvariable = profName, font=("Times New Roman", 14))
    nameEntry.pack(pady=10)

    profText2 = i.Label(frame, text = 'My UofA email is...', font=("Times New Roman", 14))
    profText2.pack()

    emailEntry = i.Entry(frame, textvariable = profEmail, font=("Times New Roman", 14))
    emailEntry.pack(pady=10)

    profSiteText = i.Label(frame, text = 'The link to my UofA homepage is...', font=("Times New Roman", 14))
    profSiteText.pack()

    siteEntry = i.Entry(frame, textvariable = profSite, font=("Times New Roman", 14))
    siteEntry.pack(pady=10)

    profText3 = i.Label(frame, text = 'I am looking for ...', font=("Times New Roman", 14))
    profText3.pack()

    grads = i.Checkbutton(frame, text = "Grad(s)", variable = gradVar, onvalue = 1, offvalue = 0)
    grads.pack()
    uGrads = i.Checkbutton(frame,text = "UnderGrad(s)", variable = uGradVar, onvalue = 1, offvalue = 0)
    uGrads.pack()

    nextButton = i.Button(frame, text = "Next",font = ("Times New Roman", 20), command = lambda: go_to_prof2_page())
    nextButton.pack()

    backButton = i.Button(frame, text = "Back",font = ("Times New Roman", 20), command = lambda: go_to_main_page())
    backButton.pack()

    frame.update_idletasks() # This makes the entries render.

def go_to_prof2_page():
    clear_frame()
    
    global paidVar
    global volunteerVar
    global gResearchVar
    global iStudyVar

    profText = i.Label(frame, text = 'This is a...', font=("Times New Roman", 20))
    profText.pack()

    paid = i.Checkbutton(frame, text = "paid", variable = paidVar, onvalue = 1, offvalue = 0)
    paid.pack()
    paidText = i.Label(frame, text = "(Leave blank for unpaid)")
    paidText.pack()

    profText2 = i.Label(frame, text = '...', font=("Times New Roman", 20))
    profText2.pack()

    volunteer = i.Checkbutton(frame, text = "volunteer", variable = volunteerVar, onvalue = 1, offvalue = 0)
    volunteer.pack()
    gradR = i.Checkbutton(frame,text = "grad research", variable = gResearchVar, onvalue = 1, offvalue = 0)
    gradR.pack()
    iStudy = i.Checkbutton(frame, text = "independent study", variable = iStudyVar, onvalue = 1, offvalue = 0)
    iStudy.pack()

    profText3 = i.Label(frame, text = '...oppurtunity.', font=("Times New Roman", 20))
    profText3.pack()
    
    nextButton = i.Button(frame, text = "Next",font = ("Times New Roman", 20), command = lambda: go_to_prof3_page())
    nextButton.pack()

    backButton = i.Button(frame, text = "Back",font = ("Times New Roman", 20), command = lambda: go_to_prof_page())
    backButton.pack()

    frame.update_idletasks()


def go_to_prof3_page():
    clear_frame()

    global desc
    global date
    global pKeyWords

    profText = i.Label(frame, text = 'Add a description for the position.', font=("Times New Roman", 20) )
    profText.pack()

    descEntry = i.Entry(frame, textvariable = desc, font=("Times New Roman", 14))
    descEntry.pack(pady=10)

    profText2 = i.Label(frame, text = "Enter the application deadline. (YYYY-MM-DD):", font=("Times New Roman", 20))
    profText2.pack()

    dateEntry = i.Entry(frame, textvariable = date, font=("Times New Roman", 14))
    dateEntry.pack(pady=10)

    profText3 = i.Label(frame, text = 'Finally, add some keywords for this. They should be related to what the research/work this position is related to. For example for a AI position the key words might be, "AI, Artificial intelligence, ML." Make sure to seperate them with commas!', font=("Times New Roman", 15), wraplength= 400)
    profText3.pack()

    keyWordEntry = i.Entry(frame, textvariable = pKeyWords, font=("Times New Roman", 14))
    keyWordEntry.pack(pady=10)

    finishButton = i.Button(frame, text = "Finish",font = ("Times New Roman", 20), command = lambda: pp())
    finishButton.pack()

    backButton = i.Button(frame, text = "Back",font = ("Times New Roman", 20), command = lambda: go_to_prof2_page())
    backButton.pack()

    frame.update_idletasks()

def pp():

    keyWords = keyword_parser(pKeyWords.get())

    try:
        specifiedDate = i.datetime.strptime(date.get(), "%Y-%m-%d")
    except:
        profText1 = i.Label(frame, text = "Invalid date, wrong format", font=("Times New Roman", 20))
        profText1.pack()

    if specifiedDate < i.datetime.now():
        profText2 = i.Label(frame, text = "Invalid date, date has already passed", font=("Times New Roman", 20))
        profText2.pack()
    else:
        opps.insert_one({"name":profName.get(), "email": profEmail.get(), "site":profSite.get(), "description":desc.get(), "Application Deadline":specifiedDate, "graduate": gradVar.get(), "undergrad":uGradVar.get(), "compensation":paidVar.get(), "volunteer":volunteerVar.get(), 'grad_research':gResearchVar.get(), 'independent_study': iStudyVar.get(), "KeyWords": keyWords })
        go_to_main_page()

root = i.Tk()
frame = i.Frame(root)
frame.pack(fill="both", expand = True)
root.geometry("800x500")
root.title('Easy UofA Lab Finder')

# All global variables using this library must be declared after root = Tk().
global profName
global profEmail 
global profSite
global desc
global date
global pKeyWords
profName = i.StringVar()
profEmail = i.StringVar()
profSite = i.StringVar()
desc = i.StringVar()
date = i.StringVar()
pKeyWords = i.StringVar()
global gradVar
global uGradVar
global paidVar
global volunteerVar
global gResearchVar
global iStudyVar
gradVar = i.IntVar()
uGradVar = i.IntVar()
paidVar = i.IntVar() 
volunteerVar = i.IntVar()
gResearchVar = i.IntVar()
iStudyVar = i.IntVar()




go_to_main_page()
root.mainloop()