import tkinter as tk

# Step 1: Create a global StringVar


def update_variable():
    """
    This function will be called to demonstrate that the global_string_var
    can be accessed and used in different functions.
    """
    global global_string_var
    print("Current value of the variable:", global_string_var.get())

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Tkinter StringVar Exa   mple")

    global global_string_var
    global_string_var = tk.StringVar()
    
    # Step 2: Create an Entry widget and link it to the global StringVar
    entry = tk.Entry(root, textvariable=global_string_var)
    entry.pack(pady=10)

    # Create a button to trigger the update_variable function
    button = tk.Button(root, text="Print Variable", command=update_variable)
    button.pack(pady=10)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
