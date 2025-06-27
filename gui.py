import tkinter as tk
from tkinter import ttk, scrolledtext, simpledialog, messagebox
from scanners import password_checker

def run_selected_tool():
    toolkit = toolkit_var.get()
    tool = tool_var.get()
    output_console.insert(tk.END, f"> Running {tool} from {toolkit} toolkit...\n")

    if toolkit == "Cyber Hygiene" and tool == "Password Checker":
        # Ask for the password
        password = simpledialog.askstring("Password Input", "Enter password to check:", parent=root)
        if password:
            result = password_checker.run(password)
            output_console.insert(tk.END, result + '\n\n')
        else:
            output_console.insert(tk.END, "⚠️ No password entered.\n\n")

# ----- MAIN GUI SETUP -----

root = tk.Tk()
root.title("Cybersecurity Toolkit")
root.geometry("600x400")

# Dropdown Variables
toolkit_var = tk.StringVar()
tool_var = tk.StringVar()

# Toolkit Selector
ttk.Label(root, text="Select Toolkit").pack(pady=(10, 0))
toolkit_menu = ttk.Combobox(root, textvariable=toolkit_var, values=["Cyber Hygiene"], state="readonly")
toolkit_menu.current(0)
toolkit_menu.pack()

# Tool Selector
ttk.Label(root, text="Select Tool").pack(pady=(10, 0))
tool_menu = ttk.Combobox(root, textvariable=tool_var, values=["Password Checker"], state="readonly")
tool_menu.current(0)
tool_menu.pack()

# Run Button
ttk.Button(root, text="Run Tool", command=run_selected_tool).pack(pady=10)

# Output Text Area
output_console = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=15)
output_console.pack(padx=10, pady=10)

# Start GUI Loop
root.mainloop()