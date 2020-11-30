from tkinter import *
from tkinter import filedialog

root=Tk()
root.geometry("497x705")

def save_file():
    save_file=filedialog.asksaveasfile(mode='w',defaultextension=".txt")
    if save_file is not None:
        text=str(entry.get(1.0,END))
        save_file.write(text)
        save_file.close()

def open_file():
    entry.delete(1.0, END)
    open_file=filedialog.askopenfile(mode='r',filetype=[('text files','*.txt')])
    if open_file is not None:
        content=open_file.read()
    entry.insert(INSERT,content)

def clear():
    entry.delete(1.0,END)

b1=Button(root,text="Save", command=save_file)
b1.place(x=20,y=10)

b2=Button(root,text="Open", command=open_file)
b2.place(x=80,y=10)

b3=Button(root,text="Clear", command=clear)
b3.place(x=140,y=10)

entry=Text(root,height=40,width=59,wrap=WORD)
entry.place(x=10,y=50)

root.mainloop()