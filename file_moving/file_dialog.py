import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(initialdir=os.getcwd())
directory_path = filedialog.askdirectory(initialdir=os.getcwd())

print(file_path)
print(directory_path)

input("press any key to exit")

