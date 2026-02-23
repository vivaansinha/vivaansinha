from tkinter import *
from tkinter import messagebox
import os
import subprocess
def commit():
    commit_message = commit_entry.get()
    if not commit_message:
        messagebox.showerror("Error", "Please enter a commit message.")
        return
    try:
        # Stage all changes
        subprocess.run(["git", "add", "."], check=True)
        # Commit with the provided message
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        messagebox.showinfo("Success", "Changes committed successfully!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
# Create the main application window
root = Tk()
root.title("Git Commit")
root.geometry("400x200")
# Create and place the commit message label and entry
commit_label = Label(root, text="Commit Message:")
commit_label.pack(pady=10)
commit_entry = Entry(root, width=50)
commit_entry.pack(pady=5)
# Create and place the commit button
commit_button = Button(root, text="Commit", command=commit)
commit_button.pack(pady=20)
# Start the main event loop
root.mainloop()
class Commit:
    def __init__(self, message):
        self.message = message
        self.hash = None
        self.author = None
        self.date = None
        self.files_changed = []
    def set_hash(self, hash):
        self.hash = hash
    def set_author(self, author):
        self.author = author
    def set_date(self, date):
        self.date = date
    def add_file_changed(self, file):
        self.files_changed.append(file)
    def __str__(self):
        return f"Commit: {self.hash}\nAuthor: {self.author}\nDate: {self.date}\nMessage: {self.message}\nFiles Changed: {', '.join(self.files_changed)}"
