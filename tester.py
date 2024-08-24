import tkinter as tk

def clear_frame():
    # Delete all widgets in the frame
    for widget in frame.winfo_children():
        widget.destroy()

def go_to_new_page():
    clear_frame()  # Clear the current page
    
    # Add new widgets for the new page
    new_label = tk.Label(frame, text="This is the new page!")
    new_label.pack()
    
    back_button = tk.Button(frame, text="Back", command=go_to_main_page)
    back_button.pack()

def go_to_main_page():
    clear_frame()  # Clear the current page
    
    # Add widgets for the main page
    main_label = tk.Label(frame, text="This is the main page.")
    main_label.pack()
    
    next_button = tk.Button(frame, text="Go to new page", command=go_to_new_page)
    next_button.pack()

# Create the main window
root = tk.Tk()
root.title("Page Navigation Example")

# Create a frame to hold the widgets
frame = tk.Frame(root)
frame.pack()

# Initialize the main page
go_to_main_page()

# Start the Tkinter event loop
root.mainloop()
