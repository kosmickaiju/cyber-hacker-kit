import tkinter as tk
from tkinter import ttk, scrolledtext, simpledialog, messagebox
from scanners import password_checker

def run_selected_tool():
    toolkit = toolkit_var.get()
    tool = tool_var.get()
    output_console.insert(tk.END, f"> Running {tool} from {toolkit} toolkit...\n")

    if toolkit == "Cyber Hygiene" and tool == "Password Checker":
        password = simpledialog.askstring("Password Input", "Enter password to check:", parent=root)
        if password:
            result = password_checker.run(password)
            output_console.insert(tk.END, result + '\n\n')
        else:
            output_console.insert(tk.END, "⚠️ No password entered.\n\n")

root = tk.Tk()
root.title("Cybersecurity Toolkit")
root.geometry("600x400")

# Variables
toolkit_var = tk.StringVar(value="Cyber Hygiene")
tool_var = tk.StringVar(value="Password Checker")

# Dropdowns
ttk.Label(root, text="Select Toolkit").pack()
toolkit_menu = ttk.Combobox(root, textvariable=toolkit_var, values=["Cyber Hygiene"], state="readonly")
toolkit_menu.pack()

ttk.Label(root, text="Select Tool").pack()
tool_menu = ttk.Combobox(root, textvariable=tool_var, values=["Password Checker"], state="readonly")
tool_menu.pack()

# Buttons
ttk.Button(root, text="Run Tool", command=run_selected_tool).pack(pady=5)

# Output Console
output_console = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=15)
output_console.pack(padx=10, pady=10)

root.mainloop()