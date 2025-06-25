import tkinter as tk
from tkinter import ttk, scrolledtext

def run_selected_tool():
    toolkit = toolkit_var.get()
    tool = tool_var.get()
    output_console.insert(tk.END, f"> Running {tool} from {toolkit} toolkit...\n")

    if toolkit == "Cyber Hygiene":
        if tool == "Password Checker":
            from scanners import password_checker
            result = password_checker.run()
            output_console.insert(tk.END, result + '\n')
    # Add other tool mappings here...

root = tk.Tk()
root.title("Cybersecurity Toolkit")

toolkit_var = tk.StringVar(value="Cyber Hygiene")
tool_var = tk.StringVar(value="Password Checker")

ttk.Label(root, text="Select Toolkit").pack()
toolkit_menu = ttk.Combobox(root, textvariable=toolkit_var, values=["Cyber Hygiene", "Ethical Hacker"])
toolkit_menu.pack()

ttk.Label(root, text="Select Tool").pack()
tool_menu = ttk.Combobox(root, textvariable=tool_var, values=["Password Checker", "Port Scan", "Summary"])
tool_menu.pack()

ttk.Button(root, text="Run Tool", command=run_selected_tool).pack()

output_console = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=15)
output_console.pack(padx=10, pady=10)

root.mainloop()