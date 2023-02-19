from tkinter import *

from tkinter import filedialog

def browserFiles():
    filename = filedialog.askopenfile(initialdir= "/",
    title = "Selecione um Arquivo",
    filetypes= (("Text Files", 
    "*.txt*"),
    ("all files",
    "*.*")))
    
    label_file_explorer.configure(text="File Opened: " + filename)

window = Tk()

window.title("File Explorer")

window.geometry("640x480")

window.config(background= "white")

label_file_explorer = Label(window,
text = "Explorador de Arquivos",
width= 100, height= 4,
fg= "dark blue")

button_explore = Button(window, text = "Explorar Arquivos", bd=1, 
command = browserFiles)


button_exit = Button(window, 
text = "Sair", bd=1,
command= exit)

label_file_explorer.grid(column=1, row=1)

button_explore.grid(column = 1, row=2)

button_exit.grid(column=1, row=3)

window.mainloop()