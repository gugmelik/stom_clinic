import tkinter as tk
import mysql.connector
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

class RecView:
    def __init__(self,root,user):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="gug123",
            database="stom_clinic"
        )
        self.cur = self.db.cursor()
        self.root = root
        self.root.geometry('655x525+600+200')
        self.root.title('Doctor')
        self.rec=user

        toolbar = Frame(self.root)
        self.frame = LabelFrame(self.root)

        view_pat = Button(toolbar, text="Add Patient", command=self.add_patient)
        view_pat.pack(side=LEFT, padx=2, pady=2)
        view_rec = Button(toolbar, text="Token", command=self.token)
        view_rec.pack(side=LEFT, padx=2, pady=2)
        logout = Button(toolbar, text="Logout", command=self.logout)
        logout.pack(side=LEFT, padx=2, pady=2)




        toolbar.pack(side=TOP, fill=X)
        self.frame.pack()

    def add_patient(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.cur.execute("select max(id)+1 from patients")
        maxid = self.cur.fetchall()
        Label(self.frame, text= 'Add Patient').grid(row=0, column=1, columnspan=10)
        Label(self.frame, text = ' Patient ID ',font='Times 15').grid(row=1,column=1,pady=10)
        mystr = StringVar()
        mystr.set(maxid)
        self.frame.p_id = Entry(self.frame, textvariable=mystr, state=DISABLED)
        self.frame.p_id.grid(row=1,column=2,columnspan=10)

        Label(self.frame, text = ' Full Name ',font='Times 15').grid(row=2,column=1,pady=10)
        self.frame.p_name = Entry(self.frame)
        self.frame.p_name.grid(row=2,column=2,columnspan=10)

        Label(self.frame, text = ' Mobile ',font='Times 15').grid(row=4,column=1,pady=10)
        self.frame.mob = Entry(self.frame)
        self.frame.mob.grid(row=4,column=2,columnspan=10)

        Label(self.frame, text = ' Address ',font='Times 15').grid(row=5,column=1,pady=10)
        self.frame.addr = Entry(self.frame)
        self.frame.addr.grid(row=5,column=2,columnspan=10)


        Button(self.frame, text='Submit', command=self.add_pat_db).grid(row=6,column=2)

    def add_pat_db(self):
        formula = "insert into patients (id, full_name, address, mobile) values (%s, %s, %s, %s)"
        doc = (self.frame.p_id.get(), self.frame.p_name.get(), self.frame.addr, self.frame.mob.get())

        popup=Tk()
        def leave():
            popup.destroy()
            self.add_patient()

        popup.wm_title("!")
        try:
            self.cur.execute(formula,doc)
            self.db.commit()
            Label(popup, text="Patient successfully added!", font='Times 15').pack(side="top", fill=X, pady=10)
            Button(popup, text="Okay", command = leave).pack(side="bottom")
        except:
            Label(popup, text="Something went wrong!!!").pack(side="top", fill=X, pady=10)
            Button(popup, text="Okay", command = lambda: popup.destroy()).pack(side="bottom")
        popup.mainloop()


    def token(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.cur.execute("select max(id)+1 from tokens")
        maxid = self.cur.fetchall()
        Label(self.frame, text= 'Add Token').grid(row=0, column=1, columnspan=10)
        Label(self.frame, text = ' Token ID ',font='Times 15').grid(row=1,column=1,pady=10)
        mystr = StringVar()
        mystr.set(maxid)
        self.frame.t_id = Entry(self.frame, textvariable=mystr, state=DISABLED)
        self.frame.t_id.grid(row=1,column=2,columnspan=10)

        Label(self.frame, text = ' Patient ID ',font='Times 15').grid(row=2,column=1,pady=10)
        mystr = StringVar()
        mystr.set(maxid)
        self.frame.tp_id = Entry(self.frame, textvariable=mystr, state=DISABLED)
        self.frame.tp_id.grid(row=2,column=2,columnspan=10)

        Label(self.frame, text = ' Full Name ',font='Times 15').grid(row=3,column=1,pady=10)
        self.frame.tp_name = Entry(self.frame)
        self.frame.tp_name.grid(row=3,column=2,columnspan=10)

        Label(self.frame, text = ' Doctor ',font='Times 15').grid(row=4,column=1,pady=10)
        self.frame.td_id = Entry(self.frame)
        self.frame.td_id.grid(row=4,column=2,columnspan=10)


        Button(self.frame, text='Submit', command=self.add_token_db).grid(row=5,column=2)

    def add_token_db(self):
        formula = "insert into tokens (patients_id, doctors_id) values (%s, %s)"
        pat = (self.frame.tp_id.get(), self.frame.td_id.get())

        popup=Tk()
        def leave():
            popup.destroy()
            self.add_token()

        popup.wm_title("!")
        try:
            self.cur.execute(formula,pat)
            self.db.commit()
            Label(popup, text="Token successfully added!", font='Times 15').pack(side="top", fill=X, pady=10)
            Button(popup, text="Okay", command = leave).pack(side="bottom")
        except:
            Label(popup, text="Something went wrong!!!").pack(side="top", fill=X, pady=10)
            Button(popup, text="Okay", command = lambda: popup.destroy()).pack(side="bottom")
        popup.mainloop()


    def logout(self):
        self.root.destroy()
        rot = Tk()
        rot.geometry('425x225')

        application = MainWindow(rot)
        rot.mainloop()



class DocView:
    def __init__(self,root,user):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="gug123",
            database="stom_clinic"
        )
        self.cur = self.db.cursor()
        self.root = root
        self.root.geometry('655x525+600+200')
        self.root.title('Doctor')
        self.doc=user

        toolbar = Frame(self.root)
        self.frame = LabelFrame(self.root)

        view_pat = Button(toolbar, text="View Patients", command=self.view_patient)
        view_pat.pack(side=LEFT, padx=2, pady=2)
        view_rec = Button(toolbar, text="Add Prescription", command=self.add_pres)
        view_rec.pack(side=LEFT, padx=2, pady=2)
        logout = Button(toolbar, text="Logout", command=self.logout)
        logout.pack(side=LEFT, padx=2, pady=2)




        toolbar.pack(side=TOP, fill=X)
        self.frame.pack()

    def add_pres(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        Label(self.frame, text= 'Add Prescription').grid(row=0, column=1, columnspan=10)
        Label(self.frame, text = ' Patient ID ',font='Times 15').grid(row=1,column=1,pady=10)
        self.frame.p_id = Entry(self.frame)
        self.frame.p_id.grid(row=1,column=2,columnspan=10)

        Label(self.frame, text = ' Full Name ',font='Times 15').grid(row=2,column=1,pady=10)
        self.frame.p_name = Entry(self.frame)
        self.frame.p_name.grid(row=2,column=2,columnspan=10)

        Label(self.frame, text = ' Disease ',font='Times 15').grid(row=4,column=1,pady=10)
        self.frame.dis = Entry(self.frame)
        self.frame.dis.grid(row=4,column=2,columnspan=10)

        Label(self.frame, text = ' Prescription ',font='Times 15').grid(row=5,column=1,pady=10)
        self.frame.pre = Entry(self.frame)
        self.frame.pre.grid(row=5,column=2,columnspan=10)

        Button(self.frame, text='Submit', command=self.add_hist_db).grid(row=6,column=2)

    def add_hist_db(self):
        print(self.doc)
        formula = "insert into patients_history (Disease, Medicine, Date, patients_id, doctors_id) values (%s, %s, now(), %s, %s)"
        query = "select d.id from doctors as d, users u where u.id=d.users_id and u.username=%s"
        self.cur.execute(query,(self.doc, ))
        d_id=self.cur.fetchall()
        print(d_id)
        pres = (self.frame.dis.get(), self.frame.pre.get(), self.frame.p_id.get(), d_id[0][0])

        popup=Tk()
        def leave():
            popup.destroy()

        popup.wm_title("!")
        try:
            self.cur.execute(formula,pres)
            self.db.commit()
            Label(popup, text="Prescription successfully added!", font='Times 15').pack(side="top", fill=X, pady=10)
            Button(popup, text="Okay", command = leave).pack(side="bottom")
        except:
            Label(popup, text="Something went wrong!!!").pack(side="top", fill=X, pady=10)
            Button(popup, text="Okay", command = lambda: popup.destroy()).pack(side="bottom")
        popup.mainloop()


    def view_patient(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        Label(self.frame, text='View Patient', font='Helvetica 18 bold').grid(row=0,column=2)

        Label(self.frame, text = ' Patient ID ',font='Times 15').grid(row=1,column=1,pady=10)
        self.frame.v_id = Entry(self.frame)
        self.frame.v_id.grid(row=1,column=1,columnspan=10)
        Button(self.frame, text='Search', command=self.view_patient_history).grid(row=2,column=2)

        Label(self.frame, text='Patient Details').grid(row=3,column=0)
        self.tree = ttk.Treeview(self.frame, height=10, column=['', '', ''])
        self.tree.grid(row=3, column=0, columnspan=2)
        self.tree.heading('#0', text='ID')
        self.tree.column('#0', width=50)
        self.tree.heading('#1', text='Full Name')
        self.tree.column('#1', width=200)
        self.tree.heading('#2', text='Address')
        self.tree.column('#2', width=150)
        self.tree.heading('#3', text='Mobile')
        self.tree.column('#3', width=150, stretch=False)
        self.view_patients()

        Label(self.frame, text='Patient History').grid(row=3,column=3)
        self.history = ttk.Treeview(self.frame, height=10, column=['', '', '', '', ''])
        self.history.grid(row=3, column=3, columnspan=2)
        self.history.heading('#0', text='PID')
        self.history.column('#0', width=50)
        self.history.heading('#1', text='Full Name')
        self.history.column('#1', width=200)
        self.history.heading('#2', text='Disease')
        self.history.column('#2', width=150)
        self.history.heading('#3', text='Medicine')
        self.history.column('#3', width=150)
        self.history.heading('#4', text='Date')
        self.history.column('#4', width=150)
        self.history.heading('#5',text='Doctor')
        self.history.column('#5', width=150, stretch=False)

    def view_patient_history(self):
        records = self.history.get_children()
        for element in records:
            self.history.delete(element)
        query = 'SELECT ph.patients_id, p.full_name, ph.Disease, ph.Medicine, ph.Date, ph.doctors_id FROM patients_history as ph, patients as p where ph.patients_id= %s and p.id=ph.patients_id'
        id = self.frame.v_id.get()
        self.cur.execute(query, (id, ))
        db_table = self.cur.fetchall()
        for data in db_table:
            self.history.insert('', 1000, text=data[0], values=data[1:])



    def view_patients(self):
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        query = 'SELECT * FROM patients'
        self.cur.execute(query)
        db_table = self.cur.fetchall()
        for data in db_table:
            self.tree.insert('', 1000, text=data[0], values=data[1:])

    def logout(self):
        self.root.destroy()
        rot = Tk()
        rot.geometry('425x225')

        application = MainWindow(rot)
        rot.mainloop()




class AdminView:
    def __init__(self,root):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="gug123",
            database="stom_clinic"
        )
        self.cur = self.db.cursor()
        self.root = root
        self.root.geometry('655x525+600+200')
        self.root.title('Admin')

        toolbar = Frame(self.root)
        self.frame = LabelFrame(self.root)

        add_doc = Button(toolbar, text="Add Doctor", command=self.add_doctor)
        add_doc.pack(side=LEFT, padx=2, pady=2)
        add_rec = Button(toolbar, text="Add Receptionist", command=self.add_recep)
        add_rec.pack(side=LEFT, padx=2,pady=2)
        view_pat = Button(toolbar, text="View Patients", command=self.view_patient)
        view_pat.pack(side=LEFT, padx=2, pady=2)
        view_doc = Button(toolbar, text="View Doctors", command=self.view_doctor)
        view_doc.pack(side=LEFT, padx=2, pady=2)
        view_rec = Button(toolbar, text="View Receptionists", command=self.view_recep)
        view_rec.pack(side=LEFT, padx=2, pady=2)
        logout = Button(toolbar, text="Logout", command=self.logout)
        logout.pack(side=LEFT, padx=2, pady=2)




        toolbar.pack(side=TOP, fill=X)
        self.frame.pack()
        photo = ImageTk.PhotoImage(Image.open("toon.jpg"))
        canvas = Canvas(self.frame, width = 300, height = 300)
        canvas.pack()
        img = PhotoImage(file="toon.jpg")
        canvas.create_image(20,20, anchor=NW, image=img)


    def add_doctor(self):
        for widget in self.frame.winfo_children():
                widget.destroy()
        self.cur.execute("select max(id)+1 from doctors")
        maxid = self.cur.fetchall()
        Label(self.frame, text= 'Add Doctor').grid(row=0, column=1, columnspan=10)
        Label(self.frame, text = ' Doctor ID ',font='Times 15').grid(row=1,column=1,pady=10)
        mystr = StringVar()
        mystr.set(maxid)
        self.frame.d_id = Entry(self.frame, textvariable=mystr, state=DISABLED)
        self.frame.d_id.grid(row=1,column=2,columnspan=10)

        Label(self.frame, text = ' Full Name ',font='Times 15').grid(row=2,column=1,pady=10)
        self.frame.d_name = Entry(self.frame)
        self.frame.d_name.grid(row=2,column=2,columnspan=10)

        Label(self.frame, text = ' Speciality ',font='Times 15').grid(row=3,column=1,pady=10)
        self.frame.spec = Entry(self.frame)
        self.frame.spec.grid(row=3,column=2,columnspan=10)

        Label(self.frame, text = ' Mobile ',font='Times 15').grid(row=4,column=1,pady=10)
        self.frame.mob = Entry(self.frame)
        self.frame.mob.grid(row=4,column=2,columnspan=10)

        Label(self.frame, text = ' Username ',font='Times 15').grid(row=5,column=1,pady=10)
        self.frame.uname = Entry(self.frame)
        self.frame.uname.grid(row=5,column=2,columnspan=10)


        Label(self.frame, text = ' Password ',font='Times 15').grid(row=6,column=1,pady=10)
        self.frame.pas = Entry(self.frame)
        self.frame.pas.grid(row=6,column=2,columnspan=10)

        Button(self.frame, text='Submit', command=self.add_doc_db).grid(row=7,column=2)


    def add_recep(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.cur.execute("select max(id)+1 from receptionists")
        maxid = self.cur.fetchall()
        Label(self.frame, text= 'Add Receptionist').grid(row=0, column=1, columnspan=10)
        Label(self.frame, text = ' Receptionist ID ',font='Times 15').grid(row=1,column=1,pady=10)
        mystr = StringVar()
        mystr.set(maxid)
        self.frame.r_id = Entry(self.frame, textvariable=mystr, state=DISABLED)
        self.frame.r_id.grid(row=1,column=2,columnspan=10)

        Label(self.frame, text = ' Full Name ',font='Times 15').grid(row=2,column=1,pady=10)
        self.frame.r_name = Entry(self.frame)
        self.frame.r_name.grid(row=2,column=2,columnspan=10)

        Label(self.frame, text = ' Mobile ',font='Times 15').grid(row=4,column=1,pady=10)
        self.frame.mob = Entry(self.frame)
        self.frame.mob.grid(row=4,column=2,columnspan=10)

        Button(self.frame, text='Submit', command=self.add_rec_db).grid(row=5,column=2)

    def view_patient(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        Label(self.frame, text='View Patient', font='Helvetica 18 bold').grid(row=0,column=2)

        Label(self.frame, text = ' Patient ID ',font='Times 15').grid(row=1,column=1,pady=10)
        self.frame.v_id = Entry(self.frame)
        self.frame.v_id.grid(row=1,column=1,columnspan=10)
        Button(self.frame, text='Search', command=self.view_patient_history).grid(row=2,column=2)

        Label(self.frame, text='Patient Details').grid(row=3,column=0)
        self.tree = ttk.Treeview(self.frame, height=10, column=['', '', ''])
        self.tree.grid(row=3, column=0, columnspan=2)
        self.tree.heading('#0', text='ID')
        self.tree.column('#0', width=50)
        self.tree.heading('#1', text='Full Name')
        self.tree.column('#1', width=200)
        self.tree.heading('#2', text='Address')
        self.tree.column('#2', width=150)
        self.tree.heading('#3', text='Mobile')
        self.tree.column('#3', width=150, stretch=False)
        self.view_patients()

        Label(self.frame, text='Patient History').grid(row=3,column=3)
        self.history = ttk.Treeview(self.frame, height=10, column=['', '', '', '', ''])
        self.history.grid(row=3, column=3, columnspan=2)
        self.history.heading('#0', text='PID')
        self.history.column('#0', width=50)
        self.history.heading('#1', text='Full Name')
        self.history.column('#1', width=200)
        self.history.heading('#2', text='Disease')
        self.history.column('#2', width=150)
        self.history.heading('#3', text='Medicine')
        self.history.column('#3', width=150)
        self.history.heading('#4', text='Date')
        self.history.column('#4', width=150)
        self.history.heading('#5',text='Doctor')
        self.history.column('#5', width=150, stretch=False)

    def view_patient_history(self):
        records = self.history.get_children()
        for element in records:
            self.history.delete(element)
        query = 'SELECT ph.patients_id, p.full_name, ph.Disease, ph.Medicine, ph.Date, ph.doctors_id FROM patients_history as ph, patients as p where ph.patients_id= %s and p.id=ph.patients_id'
        id = self.frame.v_id.get()
        self.cur.execute(query, (id, ))
        db_table = self.cur.fetchall()
        for data in db_table:
            self.history.insert('', 1000, text=data[0], values=data[1:])



    def view_patients(self):
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        query = 'SELECT * FROM patients'
        self.cur.execute(query)
        db_table = self.cur.fetchall()
        for data in db_table:
            self.tree.insert('', 1000, text=data[0], values=data[1:])

    def view_doctor(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        Label(self.frame, text='View Doctor', font='Helvetica 18 bold').grid(row=0,column=1)

        Label(self.frame, text = ' Doctor ID ',font='Times 15').grid(row=1,column=0,pady=10)
        self.frame.vd_id = Entry(self.frame)
        self.frame.vd_id.grid(row=1,column=1,columnspan=10)
        Button(self.frame, text='Search', command=self.find_doctor).grid(row=2,column=1)

        self.doc = ttk.Treeview(self.frame, height=10, column=['', '', ''])
        self.doc.grid(row=3, column=0, columnspan=2)
        self.doc.heading('#0', text='ID')
        self.doc.column('#0', width=50)
        self.doc.heading('#1', text='Full Name')
        self.doc.column('#1', width=200)
        self.doc.heading('#2', text='Speciality')
        self.doc.column('#2', width=150)
        self.doc.heading('#3', text='Mobile')
        self.doc.column('#3', width=150, stretch=False)
        self.view_doctors()

    def view_doctors(self):
        records = self.doc.get_children()
        for element in records:
            self.doc.delete(element)
        query = 'SELECT * FROM doctors'
        self.cur.execute(query)
        db_table = self.cur.fetchall()
        for data in db_table:
            self.doc.insert('', 1000, text=data[0], values=data[1:])

    def find_doctor(self):
        records = self.doc.get_children()
        for element in records:
            self.doc.delete(element)
        query = 'SELECT * FROM doctors where id= %s'
        id = self.frame.vd_id.get()
        self.cur.execute(query, (id, ))
        db_table = self.cur.fetchall()
        for data in db_table:
            self.doc.insert('', 1000, text=data[0], values=data[1:])


    def view_recep(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        Label(self.frame, text='View Receptionist', font='Helvetica 18 bold').grid(row=0,column=1)

        Label(self.frame, text = ' Receptionist ID ',font='Times 15').grid(row=1,column=0,pady=10)
        self.frame.rd_id = Entry(self.frame)
        self.frame.rd_id.grid(row=1,column=1,columnspan=10)
        Button(self.frame, text='Search', command=self.find_recep).grid(row=2,column=1)

        self.rec = ttk.Treeview(self.frame, height=10, column=['', ''])
        self.rec.grid(row=3, column=0, columnspan=2)
        self.rec.heading('#0', text='ID')
        self.rec.column('#0', width=50)
        self.rec.heading('#1', text='Full Name')
        self.rec.column('#1', width=200)
        self.rec.heading('#2', text='Mobile')
        self.rec.column('#2', width=150, stretch=False)
        self.view_receps()

    def view_receps(self):
        records = self.rec.get_children()
        for element in records:
            self.rec.delete(element)
        query = 'SELECT * FROM receptionists'
        self.cur.execute(query)
        db_table = self.cur.fetchall()
        for data in db_table:
            self.rec.insert('', 1000, text=data[0], values=data[1:])

    def find_recep(self):
        records = self.rec.get_children()
        for element in records:
            self.rec.delete(element)
        query = 'SELECT * FROM receptionists where id= %s'
        id = self.frame.rd_id.get()
        self.cur.execute(query, (id, ))
        db_table = self.cur.fetchall()
        for data in db_table:
            self.rec.insert('', 1000, text=data[0], values=data[1:])

    def logout(self):
        self.root.destroy()
        rot = Tk()
        rot.geometry('425x225')

        application = MainWindow(rot)
        rot.mainloop()

    def add_rec_db(self):
        formula = "insert into receptionists (id, full_name, mobile) values (%s, %s, %s)"
        doc = (self.frame.r_id.get(), self.frame.r_name.get(), self.frame.mob.get())

        popup=Tk()
        def leave():
            popup.destroy()
            self.add_recep()

        popup.wm_title("!")
        try:
            self.cur.execute(formula,doc)
            self.db.commit()
            Label(popup, text="Receptionist successfully added!", font='Times 15').pack(side="top", fill=X, pady=10)
            Button(popup, text="Okay", command = leave).pack(side="bottom")
        except:
            Label(popup, text="Something went wrong!!!").pack(side="top", fill=X, pady=10)
            Button(popup, text="Okay", command = lambda: popup.destroy()).pack(side="bottom")
        popup.mainloop()


    def add_doc_db(self):
        self.cur.execute("select max(id)+1 from users")
        us_id = self.cur.fetchall()
        print(us_id[0][0])
        add = "insert into users (id, username, password, type) values (%s, %s, %s, %s)"
        user = (us_id[0][0], self.frame.uname.get(), self.frame.pas.get(), "Doctor")

        formula = "insert into doctors (id, full_name, speciality, mobile, users_id) values (%s, %s, %s, %s, %s)"
        doc = (self.frame.d_id.get(), self.frame.d_name.get(), self.frame.spec.get(), self.frame.mob.get(), us_id[0][0])

        popup=Tk()
        def leave():
            popup.destroy()
            self.add_doctor()


        popup.wm_title("!")
        #try:
        self.cur.execute(add, user)
        self.db.commit()
        self.cur.execute(formula,doc)
        self.db.commit()
        Label(popup, text="Doctor successfully added!", font='Times 15').pack(side="top", fill=X, pady=10)
        Button(popup, text="Okay", command = leave).pack(side="bottom")
        #except:
            #Label(popup, text="Something went wrong!!!").pack(side="top", fill=X, pady=10)
            #Button(popup, text="Okay", command = lambda: popup.destroy()).pack(side="bottom")
        popup.mainloop()



class MainWindow:
    def __init__(self,root):
        self.root = root
        self.root.title('Stomatologiacal Clinic ')

        Label(text = ' Username ',font='Times 15').grid(row=1,column=1,pady=20)
        self.username = Entry()
        self.username.grid(row=1,column=2,columnspan=10)

        Label(text = ' Password ',font='Times 15').grid(row=2,column=1,pady=10)
        self.password = Entry(show='*')
        self.password.grid(row=2,column=2,columnspan=10)

        Label(text = 'Type',font='Times 15').grid(row=3,column=1,pady=10)
        options = ["Admin",
                   "Doctor",
                   "Receptionist"]
        self.clicked = StringVar()
        self.clicked.set("Admin")
        typ = OptionMenu(root, self.clicked, "Admin", "Doctor", "Receptionist").grid(row=3, column=2 )

        tk.Button(text='LOGIN', command=self.login).grid(row=4,column=2)
        root.bind('<Return>', lambda event: self.login())

    def login(self):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="gug123",
            database="stom_clinic"
        )
        cur = db.cursor()

        while True:
            user = self.username.get()
            passwd = self.password.get()
            typ = self.clicked.get()


            logincheck = "select * from users where username = %s and password = %s and type = %s"
            cur.execute(logincheck,(user, passwd, typ))
            rud = cur.fetchall()

            if rud and typ == "Admin":
                self.root.destroy()
                print("Successfully logged as Admin!")

                newroot = Tk()
                newroot.attributes("-fullscreen", True)
                app = AdminView(newroot)
                newroot.mainloop()
            elif rud and typ == "Doctor":
                self.root.destroy()
                print("Successfully logged as Doctor!")

                newroot = Tk()
                newroot.attributes("-fullscreen", True)
                app = DocView(newroot,user)

                newroot.mainloop()
            elif rud and typ == "Receptionist":
                self.root.destroy()
                print("Successfully logged as Receptionist!")

                newroot = Tk()
                app = RecView(newroot,user)

                newroot.mainloop()
            else:
                print("wrong login or password")
                break

        cur.close()
        db.close()



if __name__ == '__main__':
    root = Tk()
    root.geometry('425x225')

    application = MainWindow(root)
    root.mainloop()
