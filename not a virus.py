from tkinter import messagebox
import pyautogui
while True:

    if messagebox.showerror("McAfee", "Your computer has been infected with a virus! Please click OK to remove it.") :
        pyautogui.dragTo(100, 100, duration=0.5)