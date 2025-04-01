# ui.py

import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
import csv

def launch_ui(jobs):
    root = tk.Tk()
    root.title("DevApply Agent – Job Scanner")
    root.geometry("1000x500")

    # Treeview
    columns = ("title", "company", "location", "posted", "easy_apply", "url")
    tree = ttk.Treeview(root, columns=columns, show='headings', height=20)

    for col in columns:
        tree.heading(col, text=col.capitalize())
        tree.column(col, width=160 if col != "url" else 250)

    for job in jobs:
        tree.insert("", "end", values=(
            job.get("title", "N/A"),
            job.get("company", "N/A"),
            job.get("location", "N/A"),
            job.get("posted", "N/A"),
            str(job.get("easy_apply", False)),
            job.get("url", "")
        ))

    tree.pack(fill=tk.BOTH, expand=True)

    # Open link on double click
    def on_row_double_click(event):
        selected = tree.selection()
        if selected:
            job = tree.item(selected[0], 'values')
            job_url = job[-1]
            if job_url.startswith("http"):
                webbrowser.open_new_tab(job_url)

    tree.bind("<Double-1>", on_row_double_click)

    # Export to CSV
    def export_to_csv():
        if not jobs:
            messagebox.showinfo("Export", "No jobs to export.")
            return

        with open("jobs_export.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=columns)
            writer.writeheader()
            for job in jobs:
                writer.writerow(job)

        messagebox.showinfo("Export", "Jobs exported to jobs_export.csv")

    export_button = tk.Button(root, text="📤 Export to CSV", command=export_to_csv)
    export_button.pack(pady=10)

    root.mainloop()

