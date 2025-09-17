import tkinter as tk
from tkinter import ttk, scrolledtext, simpledialog, messagebox
import threading
import sys
import io
from contextlib import redirect_stdout, redirect_stderr
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

class PurpleTeamGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Purple Team Toolkit")
        self.root.geometry("900x600")
        self.root.minsize(700, 500)
        
        # Configure grid weights for responsive design
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(3, weight=1)
        
        self.toolkit_var = tk.StringVar()
        self.tool_var = tk.StringVar()
        self.is_running = False
        
        self.create_widgets()
        self.setup_initial_state()
        
    def create_widgets(self):
        # Title
        title_frame = ttk.Frame(self.root)
        title_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=(10, 5))
        
        title_label = ttk.Label(title_frame, text="Purple Team Toolkit", 
                               font=("Arial", 16, "bold"))
        title_label.pack()
        
        # Toolkit selection frame
        toolkit_frame = ttk.LabelFrame(self.root, text="Toolkit Selection", padding=10)
        toolkit_frame.grid(row=1, column=0, sticky="ew", padx=10, pady=5)
        toolkit_frame.columnconfigure(1, weight=1)
        
        ttk.Label(toolkit_frame, text="Select Toolkit:").grid(row=0, column=0, sticky="w", padx=(0, 10))
        self.toolkit_menu = ttk.Combobox(toolkit_frame, textvariable=self.toolkit_var, 
                                        values=list(TOOLKIT_TOOLS.keys()), 
                                        state="readonly", width=20)
        self.toolkit_menu.grid(row=0, column=1, sticky="ew")
        
        ttk.Label(toolkit_frame, text="Select Tool:").grid(row=1, column=0, sticky="w", padx=(0, 10), pady=(10, 0))
        self.tool_menu = ttk.Combobox(toolkit_frame, textvariable=self.tool_var, 
                                     state="readonly", width=20)
        self.tool_menu.grid(row=1, column=1, sticky="ew", pady=(10, 0))
        
        # Control buttons frame
        button_frame = ttk.Frame(self.root)
        button_frame.grid(row=2, column=0, sticky="ew", padx=10, pady=10)
        
        self.run_button = ttk.Button(button_frame, text="Run Tool", 
                                    command=self.run_selected_tool)
        self.run_button.pack(side="left", padx=(0, 10))
        
        self.clear_button = ttk.Button(button_frame, text="Clear Output", 
                                      command=self.clear_output)
        self.clear_button.pack(side="left", padx=(0, 10))
        
        self.stop_button = ttk.Button(button_frame, text="Stop", 
                                     command=self.stop_tool, state="disabled")
        self.stop_button.pack(side="left")
        
        # Progress bar
        self.progress_bar = ttk.Progressbar(button_frame, mode='indeterminate')
        self.progress_bar.pack(side="right", padx=(10, 0))
        
        # Output console frame
        console_frame = ttk.LabelFrame(self.root, text="Output Console", padding=5)
        console_frame.grid(row=3, column=0, sticky="nsew", padx=10, pady=(0, 10))
        console_frame.columnconfigure(0, weight=1)
        console_frame.rowconfigure(0, weight=1)
        
        self.output_console = scrolledtext.ScrolledText(console_frame, wrap=tk.WORD, 
                                                       width=80, height=20, 
                                                       bg="black", fg="green", 
                                                       insertbackground="green",
                                                       font=("Consolas", 10))
        self.output_console.grid(row=0, column=0, sticky="nsew")
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = ttk.Label(self.root, textvariable=self.status_var, 
                              relief=tk.SUNKEN, anchor=tk.W)
        status_bar.grid(row=4, column=0, sticky="ew", padx=5, pady=(0, 5))
        
    def setup_initial_state(self):
        self.toolkit_var.set("Cyber Hygiene")
        self.update_tool_options()
        self.toolkit_menu.bind("<<ComboboxSelected>>", self.update_tool_options)
        
        # Add welcome message
        welcome_msg = """
╔═══════════════════════════════════════════════════════════════╗
║                    Purple Team Toolkit                        ║
║                                                               ║
║  Cyber Hygiene: Tools for personal security assessment       ║
║  Ethical Hacker: Advanced penetration testing tools          ║
║                                                               ║
║  Select a toolkit and tool above, then click 'Run Tool'      ║
╚═══════════════════════════════════════════════════════════════╝

"""
        self.output_console.insert(tk.END, welcome_msg)
        
    def update_tool_options(self, event=None):
        selected_toolkit = self.toolkit_var.get()
        if selected_toolkit in TOOLKIT_TOOLS:
            tools = list(TOOLKIT_TOOLS[selected_toolkit].keys())
            self.tool_menu['values'] = tools
            if tools:
                self.tool_menu.current(0)
                
    def clear_output(self):
        self.output_console.delete(1.0, tk.END)
        self.status_var.set("Output cleared")
        
    def stop_tool(self):
        self.is_running = False
        self.status_var.set("Stopping tool...")
        
    def append_output(self, text):
        """Thread-safe method to append text to output console"""
        self.root.after(0, lambda: self._append_output_safe(text))
        
    def _append_output_safe(self, text):
        self.output_console.insert(tk.END, text)
        self.output_console.see(tk.END)
        self.root.update_idletasks()
        
    def set_running_state(self, running):
        """Update UI state based on whether a tool is running"""
        self.is_running = running
        if running:
            self.run_button.config(state="disabled")
            self.stop_button.config(state="normal")
            self.progress_bar.start(10)
            self.status_var.set("Tool running...")
        else:
            self.run_button.config(state="normal")
            self.stop_button.config(state="disabled")
            self.progress_bar.stop()
            self.status_var.set("Ready")
            
    def get_user_input(self, tool_name):
        """Get appropriate input for each tool type"""
        if tool_name == "Password Checker":
            return simpledialog.askstring("Password Input", 
                                        "Enter password to check:", 
                                        parent=self.root, show='*')
        elif tool_name in ["Hacker Port Scan", "Network Scan", "Vulnerability Scanner"]:
            default_msg = "Enter IP address (e.g., 192.168.1.1) or CIDR range (e.g., 192.168.1.0/24):"
            return simpledialog.askstring("Target Input", default_msg, parent=self.root)
        elif tool_name in ["Port Scan", "Packet Sniffer"]:
            return "default"  # These tools don't need user input
        else:
            return None
            
    def run_tool_thread(self, func, user_input, tool_name):
        """Run tool in separate thread to prevent GUI freezing"""
        try:
            # Capture stdout and stderr
            output_buffer = io.StringIO()
            error_buffer = io.StringIO()
            
            with redirect_stdout(output_buffer), redirect_stderr(error_buffer):
                if user_input == "default":
                    result = func()
                elif user_input:
                    result = func(user_input)
                else:
                    result = "No input provided."
                    
            # Get any captured print statements
            stdout_content = output_buffer.getvalue()
            stderr_content = error_buffer.getvalue()
            
            # Combine all output
            full_output = ""
            if stdout_content:
                full_output += stdout_content
            if stderr_content:
                full_output += f"Warnings/Errors:\n{stderr_content}\n"
            if result:
                full_output += str(result)
                
            self.append_output(full_output + "\n\n")
            
        except Exception as e:
            error_msg = f"Error running {tool_name}: {str(e)}\n\n"
            self.append_output(error_msg)
        finally:
            self.root.after(0, lambda: self.set_running_state(False))
            
    def run_selected_tool(self):
        if self.is_running:
            messagebox.showwarning("Tool Running", "A tool is already running. Please wait or stop it first.")
            return
            
        toolkit = self.toolkit_var.get()
        tool = self.tool_var.get()
        
        if not toolkit or not tool:
            messagebox.showerror("Selection Error", "Please select both a toolkit and a tool.")
            return
            
        func = TOOLKIT_TOOLS.get(toolkit, {}).get(tool)
        if not func:
            messagebox.showerror("Tool Error", "Selected tool is not implemented or does not exist.")
            return
            
        # Get user input if needed
        user_input = self.get_user_input(tool)
        
        # For tools that require input, check if user cancelled
        if tool == "Password Checker" and user_input is None:
            return
        elif tool in ["Hacker Port Scan", "Network Scan", "Vulnerability Scanner"] and user_input is None:
            return
            
        # Add header to output
        header = f"\n{'='*60}\n> Running {tool} from {toolkit} toolkit...\n{'='*60}\n"
        self.append_output(header)
        
        # Set running state
        self.set_running_state(True)
        
        # Run tool in separate thread
        tool_thread = threading.Thread(target=self.run_tool_thread, 
                                      args=(func, user_input, tool))
        tool_thread.daemon = True
        tool_thread.start()
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = PurpleTeamGUI()
    app.run()