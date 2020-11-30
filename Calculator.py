from tkinter import *
print("Pravin Kumar Mahato, 25")

def click(num):
    global scvalue
    text = num.widget.cget("text")
    print(text)

    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(scvalue.get())

        scvalue.set(value)
        entry_field.update()

    elif text == "C":
        scvalue.set("")
        entry_field.update()

    else:
        scvalue.set(scvalue.get() + text)
        entry_field.update()

root = Tk()
root.geometry("332x447")
root.title("Calculator")

scvalue = StringVar()
entry_field = Entry(root, textvariable=scvalue, font="lucida 17 bold",)
entry_field.pack(fill=X, ipadx=10, ipady=10, padx=10, pady=10)
scvalue.set("")

b11 = Button(root, text="1", height=2, width=5, font="lucida 15 bold")
b11.place(x=10, y=70)
b11.bind("<Button>",click)

b12 = Button(root, text="2", height=2, width=5, font="lucida 15 bold")
b12.place(x=90, y=70)
b12.bind("<Button>",click)

b13 = Button(root, text="3", height=2, width=5, font="lucida 15 bold")
b13.place(x=170, y=70)
b13.bind("<Button>",click)

b14 = Button(root, text="+", height=2, width=5, font="lucida 15 bold")
b14.place(x=250, y=70)
b14.bind("<Button>",click)

b21 = Button(root, text="4", height=2, width=5, font="lucida 15 bold")
b21.place(x=10, y=145)
b21.bind("<Button>",click)

b22 = Button(root, text="5", height=2, width=5, font="lucida 15 bold")
b22.place(x=90, y=145)
b22.bind("<Button>",click)

b23 = Button(root, text="6", height=2, width=5, font="lucida 15 bold")
b23.place(x=170, y=145)
b23.bind("<Button>",click)

b24 = Button(root, text="-", height=2, width=5, font="lucida 15 bold")
b24.place(x=250, y=145)
b24.bind("<Button>",click)

b31 = Button(root, text="7", height=2, width=5, font="lucida 15 bold")
b31.place(x=10, y=220)
b31.bind("<Button>",click)

b32 = Button(root, text="8", height=2, width=5, font="lucida 15 bold")
b32.place(x=90, y=220)
b32.bind("<Button>",click)

b33 = Button(root, text="9", height=2, width=5, font="lucida 15 bold")
b33.place(x=170, y=220)
b33.bind("<Button>",click)

b34 = Button(root, text="*", height=2, width=5, font="lucida 15 bold")
b34.place(x=250, y=220)
b34.bind("<Button>",click)

b41 = Button(root, text="C", height=2, width=5, font="lucida 15 bold")
b41.place(x=10, y=295)
b41.bind("<Button>",click)

b42 = Button(root, text="0", height=2, width=5, font="lucida 15 bold")
b42.place(x=90, y=295)
b42.bind("<Button>",click)

b43 = Button(root, text=".", height=2, width=5, font="lucida 15 bold")
b43.place(x=170, y=295)
b43.bind("<Button>",click)

b44 = Button(root, text="/", height=2, width=5, font="lucida 15 bold")
b44.place(x=250, y=295)
b44.bind("<Button>",click)

b52 = Button(root, text="=", height=2, width=12, font="lucida 15 bold")
b52.place(x=87, y=370)
b52.bind("<Button>",click)

root=mainloop()