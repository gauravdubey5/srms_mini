from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class StudentClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+300+150")
        self.root.config(bg="white")
        self.root.focus_force()
#====Title=====
        title=Label(self.root,text="Manage Student Details",font=("goudy old style",20,"bold"),bg="#0b5399",fg="white").place(x=10,y=15,width=1180,height=35)
#====variable===
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_contact=StringVar()
        self.var_date=StringVar()  
        self.var_course=StringVar()
        self.var_state=StringVar()
        self.var_city=StringVar()
        self.var_pin=StringVar()
#============column1=======
        lbl_roll=Label(self.root,text="Roll No",font=("goudy old style",15,"bold"),bg="white")
        lbl_roll.place(x=10,y=60)
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15,"bold"),bg="white")
        lbl_name.place(x=10,y=100)
        lbl_email=Label(self.root,text="Email",font=("goudy old style",15,"bold"),bg="white")
        lbl_email.place(x=10,y=140)
        lbl_gender=Label(self.root,text="Gender",font=("goudy old style",15,"bold"),bg="white")
        lbl_gender.place(x=10,y=180)
        lbl_state=Label(self.root,text="State",font=("goudy old style",15,"bold"),bg="white")
        lbl_state.place(x=10,y=220)
        lbl_city=Label(self.root,text="City",font=("goudy old style",15,"bold"),bg="white").place(x=260,y=220)
        lbl_pin=Label(self.root,text="Pin",font=("goudy old style",15,"bold"),bg="white").place(x=500,y=220)

        lbl_address=Label(self.root,text="Address",font=("goudy old style",15,"bold"),bg="white")
        lbl_address.place(x=10,y=260)


#===Entry Fields1======
        self.txt_roll=Entry(self.root,textvariable=self.var_roll,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_roll.place(x=110,y=60,width=200)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=110,y=100,width=200)
        txt_email=Entry(self.root,textvariable=self.var_email,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=110,y=140,width=200)
        txt_state=Entry(self.root,textvariable=self.var_state,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=110,y=220,width=120)
        txt_city=Entry(self.root,textvariable=self.var_city,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=330,y=220,width=120)
        txt_pin=Entry(self.root,textvariable=self.var_pin,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=580,y=220,width=90)

        self.txt_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Other"),font=("goudy old style",15,"bold"),state='readonly',justify=CENTER)
        self.txt_gender.place(x=110,y=180,width=200)
        self.txt_gender.current(0)
        
        #=====text fields=============
        self.txt_address=Text(self.root,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_address.place(x=110,y=260,width=500,height=110)


        #=========collumn2===========

        lbl_dob=Label(self.root,text="D.O.B",font=("goudy old style",15,"bold"),bg="white")
        lbl_dob.place(x=420,y=60)
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15,"bold"),bg="white")
        lbl_contact.place(x=420,y=100)
        lbl_date=Label(self.root,text="Date",font=("goudy old style",15,"bold"),bg="white")
        lbl_date.place(x=420,y=140)
        lbl_course=Label(self.root,text="Course",font=("goudy old style",15,"bold"),bg="white")
        lbl_course.place(x=420,y=180)

#===Entry Fields2======
        self.course_list=[]
        #========call to update the list==========
        self.fetch_course()

        self.txt_dob=Entry(self.root,textvariable=self.var_dob,font=("goudy old style",20,"bold"),bg="lightyellow")
        self.txt_dob.place(x=520,y=60,width=150)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",20,"bold"),bg="lightyellow").place(x=520,y=100,width=150)
        txt_date=Entry(self.root,textvariable=self.var_date,font=("goudy old style",20,"bold"),bg="lightyellow").place(x=520,y=140,width=150)
        self.txt_course=ttk.Combobox(self.root,textvariable=self.var_course,values=self.course_list,font=("goudy old style",15,"bold"),state='readonly',justify=CENTER)
        self.txt_course.place(x=520,y=180,width=150)
        self.txt_course.set("Select")

#===buttons ====
        self.btn_add=Button(self.root,text="Save",font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.add)
        self.btn_add.place(x=150,y=400,width=110,height=40)
        self.btn_update=Button(self.root,text="Update",font=("goudy old style",15,"bold"),bg="#4caf50",fg="white",cursor="hand2",command=self.update)
        self.btn_update.place(x=270,y=400,width=110,height=40)
        self.btn_delete=Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="#f44336",fg="white",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=390,y=400,width=110,height=40)
        self.btn_clear=Button(self.root,text="Clear",font=("goudy old style",15,"bold"),bg="#607d8b",fg="white",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=510,y=400,width=110,height=40)
#search panal====
        self.var_search=StringVar()
        lbl_search_roll=Label(self.root,text="Student Name",font=("goudy old style",20,"bold"),bg="white")
        lbl_search_roll.place(x=715,y=60)
        txt_search_roll=Entry(self.root,textvariable=self.var_search,font=("goudy old style",20,"bold"),bg="lightyellow")
        txt_search_roll.place(x=890,y=60,width=170)
        btn_search=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.search)
        btn_search.place(x=1080,y=60,width=110,height=33)
        #===content===
        self.S_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.S_Frame.place(x=720,y=100,width=470,height=340)

        scrolly=Scrollbar(self.S_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.S_Frame,orient=HORIZONTAL)

        self.StudentTable=ttk.Treeview(self.S_Frame,columns=("roll","name","email","gender","dob","contact","date","course","city","state","pin","address"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.StudentTable.xview)
        scrolly.config(command=self.StudentTable.yview)


        self.StudentTable.heading("roll",text="Roll No")
        self.StudentTable.heading("name",text="Name")
        self.StudentTable.heading("email",text="Email")
        self.StudentTable.heading("gender",text="Gender")
        self.StudentTable.heading("dob",text="D.O.B")
        self.StudentTable.heading("contact",text="Contact")
        self.StudentTable.heading("course",text="Course")
        self.StudentTable.heading("date",text="Date")
        self.StudentTable.heading("address",text="Address")
        self.StudentTable.heading("city",text="City")
        self.StudentTable.heading("state",text="State")
        self.StudentTable.heading("pin",text="Pin")
        self.StudentTable.heading("address",text="Address")
        self.StudentTable["show"]='headings'
        self.StudentTable.column("roll",width=100)
        self.StudentTable.column("name",width=100)
        self.StudentTable.column("email",width=100)
        self.StudentTable.column("gender",width=100)
        self.StudentTable.column("dob",width=100)
        self.StudentTable.column("contact",width=100)
        self.StudentTable.column("course",width=100)
        self.StudentTable.column("date",width=100)
        self.StudentTable.column("address",width=200)
        self.StudentTable.column("city",width=100)
        self.StudentTable.column("state",width=100)
        self.StudentTable.column("pin",width=100)
        self.StudentTable.column("address",width=200)
        self.StudentTable.pack(fill=BOTH,expand=1)
        self.StudentTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        

#========================calling================
    
    
    
    def clear(self):
        self.show()
        self.var_roll.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_dob.set("")
        self.var_contact.set("")
        self.var_date.set("")
        self.var_course.set("Select")
        self.var_state.set("")
        self.var_city.set("")
        self.var_pin.set("")
        self.txt_address.delete("1.0",END)
        self.txt_roll.config(state=NORMAL)
        self.var_search.set("")


    def delete(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if  self.var_roll.get()=="":
                 messagebox.showerror("Error","Roll number should be required",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                 
                if row==None:
                    messagebox.showerror("Error","Please select student from the list first",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete",parent=self.root)
                    if op==True:
                        cur.execute("delete from student where roll=?",(self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Student delete successfully",parent=self.root)
                        self.clear()


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def get_data(self,ev):
        self.txt_roll.config(state='readonly')
        self.txt_roll
        r=self.StudentTable.focus()
        content=self.StudentTable.item(r)
        row=content["values"]
        self.var_roll.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_dob.set(row[4])
        self.var_contact.set(row[5])
        self.var_date.set(row[6])
        self.var_course.set(row[7])
        self.var_state.set(row[8])
        self.var_city.set(row[9])
        self.var_pin.set(row[10])
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[11])
             



    def add(self):
         con=sqlite3.connect(database="rms.db")
         cur=con.cursor()
         try:
             if  self.var_roll.get()=="":
                 messagebox.showerror("Error","Roll Number should be required",parent=self.root)
             else:
                 cur.execute("select * from student where roll=?",(self.var_roll.get(),))
                 row=cur.fetchone()
                 
                 if row!=None:
                     messagebox.showerror("Error","Roll Number already present",parent=self.root)
                 else:
                     cur.execute("INSERT INTO student (roll,name,email,gender,dob,contact,date,course,city,state,pin,address) values(?,?,?,?,?,?,?,?,?,?,?,?)",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_date.get(),
                        self.var_course.get(),
                        self.var_city.get(),
                        self.var_state.get(),

                        self.var_pin.get(),

                        self.txt_address.get("1.0",END)
                     ))
                     con.commit()
                     messagebox.showinfo("Success","Student Added Successfully",parent=self.root)

                     self.show()

         except Exception as ex:
             messagebox.showerror("Error",f"Error due to {str(ex)}")
        

    def update(self):
         con=sqlite3.connect(database="rms.db")
         cur=con.cursor()
         try:
             if  self.var_roll.get()=="":
                 messagebox.showerror("Error","Roll number should be required",parent=self.root)
             else:
                 cur.execute("select * from student where roll=?",(self.var_roll.get(),))
                 row=cur.fetchone()
                 
                 if row==None:
                     messagebox.showerror("Error","Select student From List",parent=self.root)
                 else:
                     cur.execute("update student set name=?,email=?,gender=?,dob=?,contact=?,date=?,course=?,city=?,state=?,pin=?,address=? where roll=?",(
                        
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),

                        self.txt_address.get("1.0",END),
                        self.var_roll.get(),

                     ))
                     con.commit()
                     messagebox.showinfo("Success","Student Update Successfully",parent=self.root)

                     self.show()

         except Exception as ex:
             messagebox.showerror("Error",f"Error due to {str(ex)}")


    def show(self):
         con=sqlite3.connect(database="rms.db")

         cur=con.cursor()
         try:
             cur.execute("select * from student")
             rows=cur.fetchall()
             self.StudentTable.delete(*self.StudentTable.get_children())
             for row in rows:
                 self.StudentTable.insert('',END,values=row)

         except Exception as ex:
             messagebox.showerror("Error",f"Error due to {str(ex)}")

    def fetch_course(self):
         con=sqlite3.connect(database="rms.db")

         cur=con.cursor()
         try:
             cur.execute("select name from course")
             rows=cur.fetchall()
             
             if len(rows)>0:
                 for row in rows:
                     self.course_list.append(row[0])
            # print(v)


         except Exception as ex:
             messagebox.showerror("Error",f"Error due to {str(ex)}")

             

    def search(self):
         con=sqlite3.connect(database="rms.db")

         cur=con.cursor()
         try:
            cur.execute("select * from student where roll=?",(self.var_search.get(),))
            row=cur.fetchone()
            if row!=None:
                self.StudentTable.delete(*self.StudentTable.get_children())
                self.StudentTable.insert('',END,values=row)
            else:
                messagebox.showerror("Error","No Record Found",parent=self.root)

         except Exception as ex:
             messagebox.showerror("Error",f"Error due to {str(ex)}")

if __name__=="__main__":
    root=Tk()
    obj=StudentClass(root)
    root.mainloop()