import binary2strings
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

output_strings = ""
binary_file_path = ""
output_file_path  = ""



def read_strings():
    with open(binary_file_path, "rb") as file:
        binary_data = file.read()
    strings = binary2strings.extract_all_strings(binary_data)
    with open(output_file_path, "w", encoding="utf-8") as file:
        for string in strings:
            file.write(f"{string[0]}\n")
    messagebox.showinfo("Read Strings", "Strings read succesfully")
    
def select_binary_file():
    global binary_file_path
    binary_file_path = select_file()

def select_output_file():
    global output_file_path
    output_file_path = select_file()

def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        label.config(text=f"Selected File:\n{file_path}")
    return file_path

# Create the main window
root = tk.Tk()
root.title("String Reader")
root.geometry("500x300")

# Add a button to open the file dialog
select_binary_button = tk.Button(root, text="Select a Binary File", command=select_binary_file, padx=10, pady=5)
select_binary_button.pack(pady=20)

select_output_button = tk.Button(root, text="Select an Output File", command=select_output_file, padx=10, pady=5)
select_output_button.pack(pady=20)

read_strings_button = tk.Button(root, text="Read Strings", command=read_strings, padx=10, pady=5)
read_strings_button.pack(pady=20)

# Label to show the selected file path
label = tk.Label(root, text="No file selected", wraplength=350, justify="center")
label.pack(pady=10)

# Run the GUI loop
root.mainloop()
