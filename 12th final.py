import tkinter.messagebox
from tkinter import *

import mysql.connector as sqlcon
import random as rd
import csv

# Connection to MySQL
con = sqlcon.connect(host="localhost", user="root",password='bgsps')
cur = con.cursor()
cur = con.cursor(buffered=True)

cur.execute("create database IF NOT EXISTS mydb")
cur.execute("use mydb")

if con:
    # Carry out normal procedure
    print("Connection successful")
else:
    print("Connection unsuccessful")

cur.execute("create database if not exists Hospital")
cur.execute("use Hospital")
cur.execute("create table if not exists appointment"
            "("
            "idno int primary key,"
            "name char(50),"
            "age char(3),"
            "gender char(1),"
            "phone varchar(10),"
            "bg varchar(3))")

cur.execute("create table if not exists appointment_details"
            "("
            "idno int primary key,"
            "doctor varchar(50),"
            "date varchar(20),"
            "time varchar(20),"
            "appointment_no varchar(10))")

def entry():
    global e1, e2, e3, e4, e5, e6
    p1 = e1.get()
    p2 = e2.get()
    p3 = e3.get()
    p4 = e4.get()
    p5 = e5.get()
    p6 = e6.get()
    query = 'insert into appointment values("{}", "{}", "{}", "{}", "{}", "{}")'.format(p1, p2, p3, p4, p5, p6)
    cur.execute(query)
    con.commit()
    lu = [p1, p2, p3, p4, p5, p6]

    with open("data.csv", "a", newline="\n") as T:
        k = csv.writer(T)
        k.writerow(lu)

    tkinter.messagebox.showinfo("DONE", "YOU HAVE BEEN REGISTERED")

def register():
    global e1, e2, e3, e4, e5, e6 
    root1 = Tk()
    label = Label(root1, text="REGISTER YOURSELF", font='arial 25 bold')
    label.pack()
    frame = Frame(root1, height=500, width=200)
    frame.pack()

    l1 = Label(root1, text="AADHAR CARD NO.")
    l1.place(x=10, y=130)
    e1 = tkinter.Entry(root1)
    e1.place(x=100, y=130)

    l2 = Label(root1, text="NAME")
    l2.place(x=10, y=170)
    e2 = tkinter.Entry(root1)
    e2.place(x=100, y=170)

    l3 = Label(root1, text="AGE")
    l3.place(x=10, y=210)
    e3 = tkinter.Entry(root1)
    e3.place(x=100, y=210)

    l4 = Label(root1, text="GENDER M\F")
    l4.place(x=10, y=250)
    e4 = tkinter.Entry(root1)
    e4.place(x=100, y=250)

    l5 = Label(root1, text="PHONE")
    l5.place(x=10, y=290)
    e5 = tkinter.Entry(root1)
    e5.place(x=100, y=290)

    l6 = Label(root1, text="BLOOD GROUP")
    l6.place(x=10, y=330)
    e6 = tkinter.Entry(root1)
    e6.place(x=100, y=330)

    b1 = Button(root1, text="SUBMIT", command=entry)
    b1.place(x=150, y=370)

    root.resizable(False, False)
    root1.mainloop()

# long code indented might go wrong from here

def get_apoint():
    global x1
    p1 = x1.get()
    cur.execute('select * from appointment where idno=(%s)', (p1,))
    dat = cur.fetchall()
    a = []

    for i in dat:
        a.append(i)

    if len(a) == 0:
        tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!!")
    else:
        root3 = Tk()
        label = Label(root3, text="APPOINTMENT", font='arial 25 bold')
        label.pack()
        frame = Frame(root3, height=500, width=300)
        frame.pack()

        # Displaying the retrieved data
        for i in a:
            label1 = Label(root3, text=f"ID: {i[0]}\nName: {i[1]}\nAge: {i[2]}\nGender: {i[3]}\nPhone: {i[4]}\nBlood Group: {i[5]}", font='arial 12')
            label1.pack()

        # Adding a dropdown menu to select a doctor
        doctor_label = Label(root3, text="Select Doctor:")
        doctor_label.pack()

        # List of available doctors
        doctors = ["Dr. Sharma", "Dr. Verma", "Dr. Kumar", "Dr. Khan", "Dr. Kohli", "Dr. Singh", "Dr. Sidharth", "Dr. Tendulkar",
                   "Dr. Virat", "Dr. Leo", 'Dr. Irfan', 'Dr. John', 'Dr. Sanjay', 'Dr. Shahid']

        doctor_var = StringVar(root3)
        doctor_var.set(doctors[0])  # default value

        doctor_menu = OptionMenu(root3, doctor_var, *doctors)
        doctor_menu.pack()

        # Button to submit the appointment with the selected doctor
        submit_button = Button(root3, text="Submit Appointment", command=lambda: appoint_doctor(p1, doctor_var.get()))
        submit_button.pack()

        root3.resizable(False, False)
        root3.mainloop()

# Function to handle the appointment with the selected doctor
def appoint_doctor(patient_id, selected_doctor):
    appointment_details = f"Your appointment is fixed with {selected_doctor}.\nAppointment No: {rd.choice([23, 34, 12, 67, 53, 72])}"
    
    # Insert appointment details into the database
    query = 'insert into appointment_details values("{}", "{}", "{}", "{}", "{}")'.format(patient_id, selected_doctor, '', '', '')
    cur.execute(query)
    con.commit()

    tkinter.messagebox.showinfo("APPOINTMENT DETAILS", appointment_details)



def apoint():
    global x1
    root2 = Tk()
    label = Label(root2, text="APPOINTMENT", font='arial 25 bold')
    label.pack()
    frame = Frame(root2, height=200, width=200)
    frame.pack()
    l1 = Label(root2, text="AADHAAR NO.")
    l1.place(x=10, y=130)
    x1 = tkinter.Entry(root2)
    x1.place(x=100, y=130)
    b1 = Button(root2, text='Submit', command=get_apoint)
    b1.place(x=100, y=160)
    root2.resizable(False, False)
    root2.mainloop()

# List of doctors

def lst_doc():
    root4 = Tk()

    l = ["Dr. Sharma", "Dr. Verma", "Dr. Kumar", "Dr. Khan", "Dr. Kohli", "Dr. Singh", "Dr. Sidharth", "Dr. Tendulkar",
         "Dr. Virat", "Dr. Leo", 'Dr. Irfan', 'Dr. John', 'Dr. Sanjay', 'Dr. Shahid']
    m = ["Orthopaedic surgeon", "Orthopaedic surgeon", "Nephrologist", "Nephrologist", "Gynaecologist", "Gynaecologist",
         "Physician", "Physician", "Neurologist", "Neurologist", 'X-ray', 'X-ray', 'X-ray', 'X-ray']
    n = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
    frame = Frame(root4, height=500, width=500)
    frame.pack()

    l1 = Label(root4, text='NAME OF DOCTORS')
    l1.place(x=20, y=10)
    count = 20
    for i in l:
        count += 20
        l = Label(root4, text=i)
        l.place(x=20, y=count)

    l2 = Label(root4, text='DEPARTMENT')
    l2.place(x=140, y=10)
    count1 = 20
    for i in m:
        count1 += 20
        l3 = Label(root4, text=i)
        l3.place(x=140, y=count1)

    l4 = Label(root4, text='ROOM NO')
    l4.place(x=260, y=10)
    count2 = 20
    for i in n:
        count2 += 20
        l5 = Label(root4, text=i)
        l5.place(x=260, y=count2)

    root.resizable(False, False)
    root4.mainloop()

def ser_avail():
    root5 = Tk()
    frame = Frame(root5, height=500, width=500)
    frame.pack()
    l1 = Label(root5, text='SERVICES AVAILABLE')
    l1.place(x=20, y=10)
    f = ["ULTRASOUND", "X-RAY", "CT Scan", "MRI", "BLOOD COLLECTION", "DIALYSIS", "ECG", "CHEMIST", "LAB"]
    count1 = 20
    for i in f:
        count1 += 20
        l3 = Label(root5, text=i)
        l3.place(x=20, y=count1)
    l2 = Label(root5, text='ROOM NO.')
    l2.place(x=140, y=10)
    g = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    count2 = 20
    for i in g:
        count2 += 20
        l4 = Label(root5, text=i)
        l4.place(x=140, y=count2)
    l5 = Label(root5, text='To avail any of these please contact on our no.:- 7042****55')
    l5.place(x=20, y=240)
    root5.resizable(False, False)
    root5.mainloop()


def modify():
    global x3, x4, choice, new, x5, root6
    p1 = x3.get()
    cur.execute('select * from appointment where idno=(%s)', (p1,))

    dat = cur.fetchall()
    a = []
    for i in dat:
        a.append(i)
    if len(a) == 0:
        tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!!")
    else:
        root6 = Tk()
        frame = Frame(root6, height=500, width=500)
        frame.pack()
        l1 = Label(root6, text='DATA MODIFICATION', font="arial 15 bold")
        l1.place(x=75, y=10)
        l2 = Label(root6, text='WHAT YOU WANT TO CHANGE')
        l2.place(x=50, y=200)
        l3 = Label(root6, text='1.NAME')
        l3.place(x=50, y=220)
        l4 = Label(root6, text='2.AGE')
        l4.place(x=50, y=240)
        l5 = Label(root6, text='3.GENDER')
        l5.place(x=50, y=260)
        l6 = Label(root6, text='4.PHONE')
        l6.place(x=50, y=280)
        l7 = Label(root6, text='5.BLOOD GROUP')
        l7.place(x=50, y=300)
        x2 = Label(root6, text='Enter')
        x2.place(x=50, y=330)
        x4 = tkinter.Entry(root6)
        choice = x4.get()
        x4.place(x=100, y=330)
        for i in dat:
            name = Label(root6, text='NAME:-')
            name.place(x=50, y=80)
            name1 = Label(root6, text=i[1])
            name1.place(x=150, y=80)
            age = Label(root6, text='AGE:-')
            age.place(x=50, y=100)
            age1 = Label(root6, text=i[2])
            age1.place(x=150, y=100)
            gen = Label(root6, text='GENDER:-')
            gen.place(x=50, y=120)
            gen1 = Label(root6, text=i[3])
            gen1.place(x=150, y=120)
            pho = Label(root6, text='PHONE:-')
            pho.place(x=50, y=140)
            pho1 = Label(root6, text=i[4])
            pho1.place(x=150, y=140)
            bg = Label(root6, text='BLOOD GROUP:-')
            bg.place(x=50, y=160)
            bg1 = Label(root6, text=i[5])
            bg1.place(x=150, y=160)
        b = Button(root6, text='Submit', command=do_modify)
        b.place(x=50, y=400)
        L1 = Label(root6, text='OLD DETAILS')
        L1.place(x=50, y=50)
        L2 = Label(root6, text='ENTER NEW DETAIL')
        L2.place(x=50, y=360)
        x5 = tkinter.Entry(root6)
        new = x5.get()
        x5.place(x=160, y=360)
        root6.resizable(False, False)
        root6.mainloop()


def do_modify():
    global ad, x3, x4, x5
    ad = x3.get()
    choice = x4.get()
    new = x5.get()
    if choice == '1':
        cur.execute('update appointment set name={} where idno={}'.format(new, ad))
    elif choice == '2':
        cur.execute('update appointment set age={} where idno={}'.format(new, ad))
    elif choice == '3':
        cur.execute('update appointment set gender={} where idno={}'.format(new, ad))
    elif choice == '4':
        cur.execute('update appointment set phone={} where idno={}'.format(new, ad))
    elif choice == '5':
        cur.execute('update appointment set bg={} where idno={}'.format(new, ad))
    else:
        pass
    root6.destroy()
    tkinter.messagebox.showinfo("DONE", "YOUR DATA HAS BEEN MODIFIED")


choice = None
new = None
ad = None


def mod_sub():
    global x3, ad
    root7 = Tk()
    label = Label(root7, text="MODIFICATION", font='arial 25 bold')
    label.pack()
    frame = Frame(root7, height=200, width=200)
    frame.pack()
    l1 = Label(root7, text="AADHAAR NO.")
    l1.place(x=10, y=130)
    x3 = tkinter.Entry(root7)
    x3.place(x=100, y=130)
    ad = x3.get()
    b1 = Button(root7, text='Submit', command=modify)
    b1.place(x=100, y=160)
    root7.resizable(False, False)
    root7.mainloop()


def search_data():
    global x3, ad
    root7 = Tk()
    label = Label(root7, text="SEARCH DATA", font='arial 25 bold')
    label.pack()
    frame = Frame(root7, height=200, width=200)
    frame.pack()
    l1 = Label(root7, text="AADHAAR NO.")
    l1.place(x=10, y=130)
    x3 = tkinter.Entry(root7)
    x3.place(x=100, y=130)
    ad = x3.get()
    b1 = Button(root7, text='Submit', command=view_data)
    b1.place(x=100, y=160)
    root7.resizable(False, False)
    root7.mainloop()


def view_data():
    global p1
    p1 = x3.get()
    cur.execute('select * from appointment where idno=(%s)', (p1,))

    dat = cur.fetchall()
    print(dat)
    a = []
    for i in dat:
        a.append(i)
    if len(a) == 0:
        tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!!")
    else:
        det = a
        tkinter.messagebox.showinfo("APPOINTMENT DETAILS", det)


root = Tk()
label = Label(root, text="KRISHNA HOSPITAL", font="arial 40 bold", bg='light blue')
b1 = Button(text="Registration", font="arial 20 bold", bg='red', command=register)
b2 = Button(text="Appointment", font="arial 20 bold", bg='red', command=apoint)
b3 = Button(text="List of Doctors", font="arial 20 bold", bg='red', command=lst_doc)
b4 = Button(text="Services available", font='arial 20 bold', bg='red', command=ser_avail)
b7 = Button(text="View data", font='arial 20 bold', bg='red', command=search_data)
b5 = Button(text="Modify existing data", font='arial 20 bold', bg='red', command=mod_sub)
b6 = Button(text="Exit", font='arial 20 bold', command=root.destroy, bg='green')
label.pack()
b1.pack(side=LEFT, padx=10)
b3.pack(side=LEFT, padx=10)
b4.pack(side=LEFT, padx=10)
b2.place(x=25, y=500)
b7.pack(side=LEFT, padx=10)
b5.place(x=350, y=500)
b6.place(x=800, y=500)
frame = Frame(root, height=600, width=50)
frame.pack()
root.resizable(False, False)
root.mainloop()
