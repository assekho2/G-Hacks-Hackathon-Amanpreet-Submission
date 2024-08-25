import tkinter as tk

# Step 1: Create the main window
root = tk.Tk()
root.title("Multi-Select Keyword Selector")

# Step 2: Create a list of keywords
sKeyWords = ['AI', 'ML', 'Statistics', 'Data Science', 'Cybersecurity']

# Step 3: Create a Listbox widget for the multi-select dropdown
keyword_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, height=len(sKeyWords))

# Step 4: Add the keywords to the Listbox
for keyword in sKeyWords:
    keyword_listbox.insert(tk.END, keyword)

# Step 5: Pack the Listbox to make it visible
keyword_listbox.pack(padx=20, pady=20)

# Function to handle the selection and print selected keywords
def print_selected_keywords():
    selected_indices = keyword_listbox.curselection()  # Get selected indices
    selected_keywords = [keyword_listbox.get(i) for i in selected_indices]  # Get selected keywords
    print("Selected Keywords:", selected_keywords)

# Step 6: Add a button to print selected keywords
select_button = tk.Button(root, text="Select Keywords", command=print_selected_keywords)
select_button.pack(pady=10)

# Step 7: Run the main loop
root.mainloop()
