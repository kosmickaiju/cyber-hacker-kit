import tkinter as tk
from tkinter import ttk, scrolledtext, simpledialog
from scanners import password_checker, hygiene_port_scan, hacker_port_scan, network_scan, packet_sniffer, vuln_scanner

TOOLKIT_TOOLS = {
    "Cyber Hygiene": {
        "Password Checker": password_checker.run,
        "Port Scan": hygiene_port_scan.run,
    },
    "Ethical Hacker": {
        "Hacker Port Scan": hacker_port_scan.run,
        "Network Scan": network_scan.run,
        "Packet Sniffer": packet_sniffer.run,
        "Vulnerability Scanner": vuln_scanner.run
    }
}

root = tk.Tk()
root.title("Purple Team Toolkit")
root.geometry("700x450")
root.state("zoomed")

toolkit_var = tk.StringVar()
tool_var = tk.StringVar()

# toolkit dropdown
ttk.Label(root, text="Select Toolkit").pack(pady=(10, 0))
toolkit_menu = ttk.Combobox(root, textvariable=toolkit_var, values=list(TOOLKIT_TOOLS.keys()), state="readonly")
toolkit_menu.pack()

# tool dropdown
ttk.Label(root, text="Select Tool").pack(pady=(10, 0))
tool_menu = ttk.Combobox(root, textvariable=tool_var, state="readonly")
tool_menu.pack()

# output console
output_console = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=15)
output_console.pack(padx=10, pady=10)

# tool launcher
def run_selected_tool():
    toolkit = toolkit_var.get()
    tool = tool_var.get()
    func = TOOLKIT_TOOLS[toolkit].get(tool)

    output_console.insert(tk.END, f"> Running {tool} from {toolkit} toolkit...\n")

    if not func:
        output_console.insert(tk.END, "Tool not implemented yet or does not exist.\n\n")
        return
    if tool == "Password Checker":
        user_input = simpledialog.askstring("Input", "Enter password to check:", parent=root)
    elif tool in ["Hacker Port Scan", "Network Scan"]:
        user_input = simpledialog.askstring("Input", "Enter IP address or CIDR range:", parent=root)
    elif tool == "Hygiene Port Scan":
        user_input = "default" 
    elif tool == "Packet Sniffer":
        user_input = "default"
    else:
        user_input = None

    # ---------- TOOL EXECUTION ----------
    try:
        if user_input == "default":
            result = func()
        elif user_input:
            result = func(user_input)
        else:
            output_console.insert(tk.END, "Oops! No input provided.\n\n")
            return

        output_console.insert(tk.END, result + '\n\n')

    except Exception as e:
        output_console.insert(tk.END, f"Error: {e}\n\n")

# ---------- TOOL DROPDOWN UPDATER ----------
def update_tool_options(event=None):
    selected_toolkit = toolkit_var.get()
    tools = list(TOOLKIT_TOOLS[selected_toolkit].keys())
    tool_menu['values'] = tools
    if tools:
        tool_menu.current(0)

# ---------- RUN BUTTON ----------
ttk.Button(root, text="Run Tool", command=run_selected_tool).pack(pady=10)

# ---------- INITIAL SETUP ----------
toolkit_var.set("Cyber Hygiene")
update_tool_options()
toolkit_menu.bind("<<ComboboxSelected>>", update_tool_options)

# ---------- MAIN LOOP ----------
root.mainloop()