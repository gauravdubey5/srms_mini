from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class ResultClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+300+150")
        self.root.config(bg="white")
        self.root.focus_force()
#====Title=====
        title=Label(self.root,text="Add Student Result",font=("goudy old style",20,"bold"),bg="orange",fg="#262626").place(x=10,y=15,width=1180,height=50)

        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_mark=StringVar()
        self.var_fullmark=StringVar()
        self.roll_list=[]
        self.fetch_roll()



#===============lebal=========
        lbl_select=Label(self.root,text="Select Student:",font=("goudy old style",20,"bold"),bg="white")
        lbl_select.place(x=50,y=100)
        lbl_name=Label(self.root,text="Name :",font=("goudy old style",20,"bold"),bg="white")
        lbl_name.place(x=50,y=150)
        lbl_course=Label(self.root,text="Course :",font=("goudy old style",20,"bold"),bg="white")
        lbl_course.place(x=50,y=200)
        lbl_mark=Label(self.root,text="Mark Obtain :",font=("goudy old style",20,"bold"),bg="white")
        lbl_mark.place(x=50,y=250)
        lbl_fullmarks=Label(self.root,text="Total Marks :",font=("goudy old style",20,"bold"),bg="white")
        lbl_fullmarks.place(x=50,y=300)

# ==============Entry============

        self.txt_roll=ttk.Combobox(self.root,textvariable=self.var_roll,values=self.roll_list,font=("goudy old style",20,"bold"),state='readonly',justify=CENTER)
        self.txt_roll.place(x=280,y=100,width=140)
        self.txt_roll.set("Select")

        self.txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",20,"bold"),bg="lightyellow",state='readonly').place(x=280,y=150,width=300)
        self.txt_course=Entry(self.root,textvariable=self.var_course,font=("goudy old style",20,"bold"),bg="lightyellow",state='readonly').place(x=280,y=200,width=300)
        self.txt_mark=Entry(self.root,textvariable=self.var_mark,font=("goudy old style",20,"bold"),bg="lightyellow")
        self.txt_mark.place(x=280,y=250,width=300)
        self.txt_fullmarks=Entry(self.root,textvariable=self.var_fullmark,font=("goudy old style",20,"bold"),bg="lightyellow")
        self.txt_fullmarks.place(x=280,y=300,width=300)


        self.btn_search=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.search)
        self.btn_search.place(x=440,y=100,width=140)
        self.btn_submit=Button(self.root,text="Submit",font=("goudy old style",15,"bold"),bg="green",fg="white",cursor="hand2",command=self.add)
        self.btn_submit.place(x=320,y=350,width=100,height=35)
        self.btn_clear=Button(self.root,text="Clear",font=("goudy old style",15,"bold"),bg="#607d8b",fg="white",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=450,y=350,width=100,height=35)

        self.bg_img=Image.open("image/im.8.jpg")
        self.bg_img=self.bg_img.resize((500,300))
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=630,y=100)

#=============================================================================

    def fetch_roll(self):
            con=sqlite3.connect(database="rms.db")

            cur=con.cursor()
            try:
                    cur.execute("select roll from student")
                    rows=cur.fetchall()
                    if len(rows)>0:
                            for row in rows:
                                    self.roll_list.append(row[0])       

            except Exception as ex:
                    messagebox.showerror("Error",f"Error due to {str(ex)}")

    def search(self):
         con=sqlite3.connect(database="rms.db")

         cur=con.cursor()
         try:
            cur.execute("select name,course from student where roll=?",(self.var_roll.get(),))
            row=cur.fetchone()
            if row!=None:
                  self.var_name.set(row[0])
                  self.var_course.set(row[1])

            else:
                messagebox.showerror("Error","No Record Found",parent=self.root)

         except Exception as ex:
             messagebox.showerror("Error",f"Error due to {str(ex)}")
   
    def add(self):
         con=sqlite3.connect(database="rms.db")
         cur=con.cursor()
         try:
             if  self.var_name.get()=="":
                 messagebox.showerror("Error","Please first search student record",parent=self.root)
             else:
                 cur.execute("select * from result where roll=? and course=?",(self.var_roll.get(),self.var_course.get(),))
                 row=cur.fetchone()
                 
                 if row!=None:
                     messagebox.showerror("Error","Result already present",parent=self.root)
                 else:
                     per=(int(self.var_mark.get())*100)/int(self.var_fullmark.get())
                     cur.execute("insert into result (roll,name,course,mark,fullmark,per) values(?,?,?,?,?,?)",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_mark.get(),
                        self.var_fullmark.get(),
                        str(per)
                     ))
                     con.commit()
                     messagebox.showinfo("Success","Result Added Successfully",parent=self.root)
         
         except Exception as ex:
             messagebox.showerror("Error",f"Error due to {str(ex)}")

    def clear(self):
         self.var_roll.set("Select")
         self.var_name.set("")
         self.var_course.set("")
         self.var_mark.set("")
         self.var_fullmark.set("")
                      

             


if __name__=="__main__":
    root=Tk()
    obj=ResultClass(root)
    root.mainloop()