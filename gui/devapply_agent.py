from tkinter import *
from tkinter import ttk

# Initialize the main window
root = Tk()
root.title("DevApply Agent v1 - LinkedIn Outreach")
root.geometry("520x400")
root.configure(bg="#1e1e2e")

# Fonts and styling
TITLE_FONT = ("Helvetica", 16, "bold")
LABEL_FONT = ("Helvetica", 10)
BUTTON_FONT = ("Helvetica", 10, "bold")

# Title label
title = Label(root, text="🚀 DevApply AGENT v1", font=TITLE_FONT, fg="white", bg="#1e1e2e")
title.pack(pady=10)

# Recruiter Bait Score
score_frame = Frame(root, bg="#1e1e2e")
score_frame.pack(pady=10)
score_label = Label(score_frame, text="Recruiter Bait Score:", font=LABEL_FONT, fg="white", bg="#1e1e2e")
score_label.pack(side=LEFT)

score_bar = ttk.Progressbar(score_frame, orient=HORIZONTAL, length=200, mode='determinate')
score_bar['value'] = 88  # Initial score
score_bar.pack(side=LEFT, padx=10)

score_percent = Label(score_frame, text="88%", font=LABEL_FONT, fg="lime", bg="#1e1e2e")
score_percent.pack(side=LEFT)

# Hashtag input
hashtag_label = Label(root, text="🔎 Enter Job Hashtag (e.g., #hiringcloudengineer):", font=LABEL_FONT, fg="white", bg="#1e1e2e")
hashtag_label.pack(pady=(20, 5))

hashtag_entry = Entry(root, width=40)
hashtag_entry.pack()

# Action Buttons Frame
button_frame = Frame(root, bg="#1e1e2e")
button_frame.pack(pady=30)

connect_btn = Button(button_frame, text="🤝 Auto Connect", font=BUTTON_FONT, width=18, bg="#00adb5", fg="white")
connect_btn.grid(row=0, column=0, padx=10)

comment_btn = Button(button_frame, text="💬 Auto Comment", font=BUTTON_FONT, width=18, bg="#ff5722", fg="white")
comment_btn.grid(row=0, column=1, padx=10)

dm_btn = Button(button_frame, text="✉️ Auto DM", font=BUTTON_FONT, width=18, bg="#9c27b0", fg="white")
dm_btn.grid(row=1, column=0, columnspan=2, pady=10)

# Footer
footer = Label(root, text="Built by Sudharsan ⚡ with Python + Playwright", font=("Helvetica", 8), fg="gray", bg="#1e1e2e")
footer.pack(side=BOTTOM, pady=10)

# Run the GUI
root.mainloop()

