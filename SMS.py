from tkinter import *
from tkinter import ttk

def add():
    root = Tk()
    root.title("Update Student Data")
    root.geometry("680x670")

    title = Label(root, text="Student Management System", font=("times new roman", 40, "bold"), bd=8, relief=GROOVE, bg="yellow", fg="red")
    title.pack(side=TOP, fill=X)

    Manage_Frame = Frame(root, bd=4, relief=RIDGE, bg="crimson")
    Manage_Frame.pack(side=TOP, )

    m_title = Label(Manage_Frame, text="Manage Student", font=("times new roman", 30, "bold"), fg="white", bg="crimson")
    m_title.grid(row=0, columnspan=2, pady=20, padx=130)

    lbl_prn = Label(Manage_Frame, text="PRN No.", font=("times new roman", 20, "bold"), fg="white", bg="crimson")
    lbl_prn.grid(row=1, column=0, pady=10, padx=25, sticky="w")

    txt_prn = Entry(Manage_Frame, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
    txt_prn.grid(row=1, column=1, pady=10, padx=25, sticky="w")

    lbl_name = Label(Manage_Frame, text="Name", font=("times new roman", 20, "bold"), fg="white", bg="crimson")
    lbl_name.grid(row=2, column=0, pady=10, padx=25, sticky="w")

    txt_name = Entry(Manage_Frame, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
    txt_name.grid(row=2, column=1, pady=10, padx=25, sticky="w")

    lbl_email = Label(Manage_Frame, text="Email", font=("times new roman", 20, "bold"), fg="white", bg="crimson")
    lbl_email.grid(row=3, column=0, pady=10, padx=25, sticky="w")

    txt_email = Entry(Manage_Frame, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
    txt_email.grid(row=3, column=1, pady=10, padx=25, sticky="w")

    lbl_gender = Label(Manage_Frame, text="Gender", font=("times new roman", 20, "bold"), fg="white", bg="crimson")
    lbl_gender.grid(row=4, column=0, pady=10, padx=25, sticky="w")

    combo_gender = ttk.Combobox(Manage_Frame, font=("times new roman", 13, "bold"))
    combo_gender['values'] = ("male", "female", "other")
    combo_gender.grid(row=4, column=1, pady=10, padx=25, sticky="w")

    lbl_contact = Label(Manage_Frame, text="Contact No.", font=("times new roman", 20, "bold"), fg="white", bg="crimson")
    lbl_contact.grid(row=5, column=0, pady=10, padx=25, sticky="w")

    txt_contact = Entry(Manage_Frame, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
    txt_contact.grid(row=5, column=1, pady=10, padx=25, sticky="w")

    lbl_dob = Label(Manage_Frame, text="D.O.B", font=("times new roman", 20, "bold"), fg="white", bg="crimson")
    lbl_dob.grid(row=6, column=0, pady=10, padx=25, sticky="w")

    txt_dob = Entry(Manage_Frame, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
    txt_dob.grid(row=6, column=1, pady=10, padx=25, sticky="w")

    lbl_address = Label(Manage_Frame, text="Address", font=("times new roman", 20, "bold"), fg="white", bg="crimson")
    lbl_address.grid(row=7, column=0, pady=10, padx=25, sticky="w")

    txt_address = Text(Manage_Frame, font=("times new roman", 15, "bold"), height=5, width=20, wrap=WORD, bd=5, relief=GROOVE)
    txt_address.grid(row=7, column=1, pady=10, padx=25, sticky="w")

    print = Button(root, text=' Add ', fg='black', bg='red', height=3, width=7)
    print.pack()


def update():
    pass


def delete():
    pass


def exit():
    pass


def print():
    pass



class Student:
    def __init__(self, root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1585x860+0+0")

        title = Label(self.root, text="Student Management System", font=("times new roman", 40, "bold"), bd=8, relief=GROOVE, bg="yellow", fg="red")
        title.pack(side=TOP, fill=X)

        #--------------------------Manage Frame--------------------------
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Manage_Frame.place(x=30, y=106, width=500, height=725)

        add_btn = Button(Manage_Frame, text=' Add ', font=("times new roman", 40, "bold"), fg='black', bg='red', command=add, width=10)
        add_btn.grid(row=1, column=0, pady=17, padx=80, sticky="w")

        update_btn = Button(Manage_Frame, text=' Update ', font=("times new roman", 40, "bold"), fg='black', bg='red', command=update, width=10)
        update_btn.grid(row=2, column=0, pady=17, padx=80, sticky="w")

        delete_btn = Button(Manage_Frame, text=' Delete ', font=("times new roman", 40, "bold"), fg='black', bg='red', command=delete, width=10)
        delete_btn.grid(row=3, column=0, pady=17, padx=80, sticky="w")

        exit_btn = Button(Manage_Frame, text=' Exit ', font=("times new roman", 40, "bold"), fg='black', bg='red', command=exit, width=10)
        exit_btn.grid(row=4, column=0, pady=17, padx=80, sticky="w")

        print_btn = Button(Manage_Frame, text=' Print ', font=("times new roman", 40, "bold"), fg='black', bg='red', command=print, width=10)
        print_btn.grid(row=5, column=0, pady=17, padx=80, sticky="w")



        # --------------------------Detail Frame--------------------------
        Display_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Display_Frame.place(x=565, y=106, width=993, height=725)





root = Tk()
s = Student(root)
root.mainloop()