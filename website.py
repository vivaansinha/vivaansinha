from tkinter import *
import pywhatkit
window= Tk()
window.title("Browseracsessories")
label = Label(window, text="Browser Accessories!", font=("Arial", 26), bg="blue", fg="palegreen")
label.pack(pady=20)
entry = Entry(window, width=30, font=("Arial", 36), bg="lightblue", fg="black", bd=0, highlightthickness=0)
entry.pack(pady=0)
window.geometry('1000x500')
window.config(bg="blue")
button = Button(window, text="Search", font=("Arial", 12), bg="lightblue", fg="black", command=lambda: pywhatkit.search(entry.get()))
button.pack(pady=20)
window.mainloop()