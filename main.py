import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import time
import threading
import os

class ValidatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Unified XML Data Validator (Portfolio Demo)")
        self.root.geometry("600x450")
        self.root.resizable(False, False)

        # --- Styles ---
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TButton", font=("Segoe UI", 10), padding=6)
        style.configure("TLabel", font=("Segoe UI", 10))
        style.configure("Header.TLabel", font=("Segoe UI", 12, "bold"), foreground="#2c3e50")

        # --- Header Section ---
        header_frame = tk.Frame(root, bg="white", pady=15)
        header_frame.pack(fill="x")
        
        lbl_title = tk.Label(header_frame, text="Unified XML/FNT Validator Tool", 
                             font=("Segoe UI", 14, "bold"), bg="white", fg="#2980b9")
        lbl_title.pack()
        
        lbl_subtitle = tk.Label(header_frame, text="Automated Quality Assurance & Error Reporting System", 
                                font=("Segoe UI", 9), bg="white", fg="#7f8c8d")
        lbl_subtitle.pack()

        # --- Control Panel ---
        control_frame = ttk.LabelFrame(root, text="Validation Controls", padding=15)
        control_frame.pack(padx=20, pady=15, fill="x")

        self.btn_load = ttk.Button(control_frame, text="📂 Select Source Folder", command=self.load_folder)
        self.btn_load.pack(side="left", padx=5)

        self.lbl_path = ttk.Label(control_frame, text="No folder selected", foreground="gray")
        self.lbl_path.pack(side="left", padx=10)

        # --- Progress Section ---
        progress_frame = tk.Frame(root, padx=20, pady=5)
        progress_frame.pack(fill="x")

        self.progress = ttk.Progressbar(progress_frame, orient="horizontal", length=100, mode='determinate')
        self.progress.pack(fill="x", pady=5)

        self.btn_run = ttk.Button(progress_frame, text="▶ Run Validation Sequence", command=self.start_validation_thread, state="disabled")
        self.btn_run.pack(fill="x", pady=5)

        # --- Log Console ---
        log_frame = ttk.LabelFrame(root, text="System Log", padding=10)
        log_frame.pack(padx=20, pady=5, fill="both", expand=True)

        self.log_text = tk.Text(log_frame, height=8, font=("Consolas", 9), state="disabled", bg="#f4f6f7")
        self.log_text.pack(fill="both", expand=True)

    def log(self, message):
        self.log_text.config(state="normal")
        self.log_text.insert(tk.END, f">> {message}\n")
        self.log_text.see(tk.END)
        self.log_text.config(state="disabled")

    def load_folder(self):
        # In a real app, this would open a dialog. For demo, we simulate a selection.
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.lbl_path.config(text=f".../{folder_selected.split('/')[-1]}")
            self.log(f"Source loaded: {folder_selected}")
            self.log("Ready to validate. 142 files detected.")
            self.btn_run.config(state="normal")

    def start_validation_thread(self):
        # Run logic in a thread so GUI doesn't freeze
        t = threading.Thread(target=self.run_dummy_logic)
        t.start()

    def run_dummy_logic(self):
        self.btn_run.config(state="disabled")
        self.btn_load.config(state="disabled")
        self.log("Initializing validation engine...")
        time.sleep(1)
        
        steps = [
            "Parsing XML Schema definition...",
            "Checking syntax integrity...",
            "Validating node hierarchy...",
            "Cross-referencing FNT tags...",
            "Detecting orphan elements...",
            "Generating error report (CSV)..."
        ]

        self.progress['maximum'] = len(steps) * 20
        
        for i, step in enumerate(steps):
            time.sleep(0.6) # Fake processing time
            self.log(step)
            self.progress['value'] += 20
            self.root.update_idletasks()

        self.log("✅ Validation Complete. 0 Critical Errors found.")
        self.log("Report saved to /output/validation_report_2024.csv")
        messagebox.showinfo("Success", "Validation Process Completed Successfully!\nTime elapsed: 3.42s")
        
        self.btn_run.config(state="normal")
        self.btn_load.config(state="normal")
        self.progress['value'] = 0

if __name__ == "__main__":
    # Check if we are in a headless environment (like a server)
    if os.environ.get('DISPLAY', '') == '':
        print("⚠️  HEADLESS ENVIRONMENT DETECTED ⚠️")
        print("This is a GUI Application. It cannot run in this cloud terminal because there is no screen.")
        print("ACTION: Copy this code to your local computer (VS Code / PyCharm) and run it there to see the window.")
    else:
        try:
            root = tk.Tk()
            app = ValidatorApp(root)
            root.mainloop()
        except tk.TclError:
            print("Error: Could not open display. Run this locally.")
