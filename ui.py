# ui.py

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import csv
from core.job_search import find_jobs
from playwright.sync_api import sync_playwright
from core.session import load_cookies

class JobApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DevApply Agent – Job Scanner")

        # Search filters
        self.keyword_var = tk.StringVar(value="AWS Cloud Engineer")
        self.location_var = tk.StringVar(value="Remote")
        self.easy_apply_var = tk.BooleanVar(value=True)

        self.build_ui()

    def build_ui(self):
        # Top filters
        filter_frame = ttk.Frame(self.root)
        filter_frame.pack(pady=10)

        ttk.Label(filter_frame, text="Keyword:").grid(row=0, column=0, padx=5)
        ttk.Entry(filter_frame, textvariable=self.keyword_var, width=25).grid(row=0, column=1)

        ttk.Label(filter_frame, text="Location:").grid(row=0, column=2, padx=5)
        ttk.Entry(filter_frame, textvariable=self.location_var, width=20).grid(row=0, column=3)

        ttk.Checkbutton(filter_frame, text="Easy Apply Only", variable=self.easy_apply_var).grid(row=0, column=4, padx=5)

        ttk.Button(filter_frame, text="Find Jobs", command=self.find_jobs).grid(row=0, column=5, padx=10)

        # Table
        self.tree = ttk.Treeview(self.root, columns=("Title", "Company", "Location", "Posted", "Easy_apply", "Url"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150 if col != "Url" else 400)
        self.tree.pack(fill=tk.BOTH, expand=True)

        ttk.Button(self.root, text="📁 Export to CSV", command=self.export_csv).pack(pady=10)

    def find_jobs(self):
        keyword = self.keyword_var.get()
        location = self.location_var.get()
        easy_apply = self.easy_apply_var.get()

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            load_cookies(context)
            page = context.new_page()

            jobs = find_jobs(page, keyword, location, easy_apply)
            self.display_jobs(jobs)

            browser.close()

    def display_jobs(self, jobs):
        for row in self.tree.get_children():
            self.tree.delete(row)
        if not jobs:
            messagebox.showinfo("No Jobs Found", "Sorry, no jobs were found for your filters.")
        for job in jobs:
            self.tree.insert("", "end", values=(
                job.get("title", "N/A"),
                job.get("company", "N/A"),
                job.get("location", "N/A"),
                job.get("posted", "N/A"),
                str(job.get("easy_apply", False)),
                job.get("url", "#")
            ))

    def export_csv(self):
        file = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if not file:
            return
        with open(file, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Title", "Company", "Location", "Posted", "Easy Apply", "URL"])
            for row in self.tree.get_children():
                writer.writerow(self.tree.item(row)["values"])
        messagebox.showinfo("Export Complete", f"Jobs exported to {file}")

def launch_ui(_jobs=None):
    root = tk.Tk()
    app = JobApp(root)
    root.mainloop()

