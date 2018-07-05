from tkinter import *
import os
import sqlite3

os.chdir(r'C:\Users\nikhi\Desktop\c')
root = Tk()
ab = int
c = StringVar()
btn = StringVar()
option = StringVar()
v= StringVar()
l = []
entry1 = Entry()
entry2 = Entry()
la2 = Entry()
la4 = Entry()
h = StringVar()
r = StringVar()
m = 0
n = 0
o = 0
f = IntVar()
s1 = StringVar()


def print1():
    global s1
    s1 = (e1.get())
    db = sqlite3.connect(r"" + s1 + ".db")
    f1 = Frame(root, width=30, height=100)
    f1.pack()
    b1 = Button(f1, text=s1,width=20, height=3)
    b1.pack()


def selop():
    root7 = Tk()
    root7.title("SELECT YOUR OPTION")
    fr1 = Frame(root7, width=100, height=30)
    fr1.pack()
    fr1 = Frame(root7, width=100, height=100)
    fr1.pack()
    l = Label(fr1, text="What do you wish to do? ")
    l.pack()
    l.configure(font=("Ariel", 10))
    b1 = Button(fr1, text="Insert", command=entry, width=10)
    b1.pack(fill="none", expand=True)
    b2 = Button(fr1, text="Update", command=update_table, width=10)
    b2.pack(fill="none", expand=True)
    b3 = Button(fr1, text="Delete", command=delete, width=10)
    b3.pack(fill="none", expand=True)
    b4 = Button(fr1, text="View", command=view, width=10)
    b4.pack(fill="none", expand=True)
    fr2 = Frame(root7, width=30, height=60)
    fr2.pack(fill="none", expand=True)


def btn_name(event):
    global c
    c = event.widget['text']


def update_table():

    def switch1():

        def reason_update():
            global c, v, r
            r = str(entry2.get())
            con = sqlite3.connect(r"" + c + ".db")
            d = con.cursor()
            d.execute("UPDATE " + c + " SET Reason = ? WHERE Srno = " + v, (r, ))
            con.commit()

        def amount_update():
            global c, v, h
            h = str(entry2.get())
            con = sqlite3.connect(r"" + c + ".db")
            d = con.cursor()
            d.execute("UPDATE  " + c + "  SET Amount =" + h + " WHERE Srno = " + v)
            con.commit()
        global c, option, entry2, h
        option = str(entry1.get())
        root9 = Tk()
        update_frame = Frame(root9, width=30, height=30)
        update_frame.pack()
        if option.lower() == "amount":
            lab4 = Label(update_frame, text="Enter the Amount you wish to update")
            lab4.pack()
            lab4.config(font=("Ariel", 10))
            entry2 = Entry(update_frame, text="", width=15)
            entry2.pack()
            button4 = Button(update_frame, text="Submit", command=amount_update)
            button4.pack()
            button4.config(font=("Ariel", 10))
        elif option.lower() == "reason":
            lab4 = Label(update_frame, text="Enter the Reason you wish to update")
            lab4.pack()
            lab4.config(font=("Ariel", 10))
            entry2 = Entry(update_frame, text="", width=15)
            entry2.pack()
            button4 = Button(update_frame, text="Submit", command=reason_update)
            button4.pack()
            button4.config(font=("Ariel", 10))
        else:
            lab5 = Label(update_frame, text="Please enter a valid option!!")
            lab5.pack()
        root9.mainloop()

    def update():
        global v, g, entry1
        global c
        root8 = Tk()
        v = str(v2.get())
        lab1 = Label(root8, text="What do you wish to update? ")
        lab1.pack()
        lab2 = Label(root8, text="1. Amount ")
        lab2.pack()
        lab3 = Label(root8, text="2. Reason ")
        lab3.pack()
        entry1 = Entry(root8, text="")
        entry1.pack()
        button3 = Button(root8, text="Submit", command=switch1)
        button3.pack()
        root8.mainloop()
    global c
    root5 = Tk()
    ser = Label(root5, text="Enter the serial no of the record")
    ser.pack()
    v2 = Entry(root5, text="")
    v2.pack()
    sub = Button(root5, text="Update", command=update)
    sub.pack()
    root5.mainloop()


def delete():
    def delet():
        global c
        serial_num = num.get()
        con = sqlite3.connect(r"" + c + ".db")
        d = con.cursor()
        d.execute("DELETE FROM    " + c + " WHERE Srno =" + serial_num)
        con.commit()
    root6 = Tk()
    ser = Label(root6, text="Enter the serial number of the tuple to be deleted")
    ser.pack()
    num = Entry(root6, text="")
    num.pack()
    but = Button(root6, text="Delete", command=delet)
    but.pack()
    root6.mainloop()


def view():
    global c
    os.startfile(r"" + c + ".db")


def walk(a):
    for name in os.listdir(a):
        global c
        if name.endswith(".db"):
            c, b = name.split('.')
            z = c.capitalize()
            l.append(z)
            f3 = Frame(root, width=30, height=100)
            f3.pack()
            btn1 = Button(f3, text=z, command=selop, width=20, height=3, font=("Ariel", 14))
            btn1.bind("<Button-1>", btn_name)
            btn1.pack()


def entry():
    def open_database():
        global f
        global ab
        global btn, m, n, o
        amt = int(la2.get())
        reason = str(la4.get())
        radio = str(la7.get())
        if radio.lower() == "credit":
            n += amt
            m += n
        elif radio.lower() == "debit":
            if m < amt:
                o = "Insufficient balance"
            else:
                o += amt
                m -= o

        con = sqlite3.connect(r"" + c + ".db")
        d = con.cursor()
        try:
            d.execute(
                "CREATE TABLE IF NOT EXISTS " + c + " (Srno INTEGER,Amount INTEGER, Reason TEXT,CD GPType,Total_Credit INTEGER,Total_Debit INTEGER,Balance INTEGER)")
            x = d.execute("SELECT MAX(Srno) FROM "+c)
            ab = (d.fetchone()[0])
            if ab is None:
                f = 1
                d.execute("INSERT INTO " + c + "(Srno, Amount, Reason, CD,Total_Credit,Total_Debit,Balance)VALUES(?, ?, ?, ?, ?, ?, ?)",
                          (f, amt, reason, radio, n, o, m))
                con.commit()
            else:
                #ab = int(d.fetchone()[0])
                d.execute(
                    "INSERT INTO " + c + "(Srno, Amount, Reason, CD,Total_Credit,Total_Debit,Balance)VALUES(?, ?, ?, ?, ?, ?, ?)",
                    (ab+1, amt, reason, radio, n, o, m))
                con.commit()
        except sqlite3.ProgrammingError as e:
            print(e)
    global ab
    root2 = Tk()
    root2.title("Insert A Record")
    f1 = Frame(root2)
    f1.pack()
    la1 = Label(f1, text="Enter the amount: ")
    la1.pack(side=LEFT)
    la2 = Entry(f1, text="")
    la2.pack(side=RIGHT)
    f2 = Frame(root2)
    f2.pack()
    la3 = Label(f2, text="Enter the reason: ")
    la3.pack(side=LEFT)
    la4 = Entry(f2, text="")
    la4.pack(side=RIGHT)
    f3 = Frame(root2)
    f3.pack()
    la6 = Label(f3, text="CREDIT/DEBIT")
    la6.pack()
    la7 = Entry(f3, text="")
    la7.pack(side=LEFT)
    f4 = Frame(root2)
    f4.pack()
    '''d.execute("SELECT SUM(Amount) FROM " + c)
    ab = d.fetchone()[0]'''
    f5 = Frame(root2)
    f5.pack()
    l11 = Button(f5, text="Submit", command=open_database)
    l11.pack()
    root2.mainloop()


def button():
    root1 = Tk()
    global e1
    root1.title("NEW DATABASE")
    l1 = Label(root1, text="Please enter the name of the database to be created")
    l1.pack()
    e1 = Entry(root1, text="")
    e1.pack()
    b1 = Button(root1, text="Submit", command=print1)
    b1.pack()
    root1.mainloop()


root.title("Account Manager")
frame1 = Frame(root).pack()
l1 = Label(frame1, text='WELCOME TO ACCOUNT MANAGEMENT SYSTEM')
label = Label(root, text="  ACCOUNT MANAGER ")
label.pack()
label.config(font=("Courier", 44))
f2 = Frame(root, width=30, height=50)
f2.pack()
walk(r'C:\Users\nikhi\Desktop\c')
b1 = Button(frame1, text="+", command=button, width=5, height=2)
b1.pack(side=RIGHT)
b1.configure(font=("Courier", 20))
root.mainloop()
