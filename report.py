from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class ReportClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+300+150")
        self.root.config(bg="white")
        self.root.focus_force()
#====Title=====
        title=Label(self.root,text="View Student Result",font=("goudy old style",20,"bold"),bg="orange",fg="#262626").place(x=10,y=15,width=1180,height=50)
#=================================

        self.var_search=StringVar()
        self.var_id=""

        
        lbl_search=Label(self.root,text="Search By Roll No:",font=("goudy old style",20,"bold"),bg="white")
        lbl_search.place(x=280,y=100)
        txt_search=Entry(self.root,textvariable=self.var_search,font=("goudy old style",20),bg="lightyellow")
        txt_search.place(x=520,y=100,width=150)

        self.btn_search=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.search)
        self.btn_search.place(x=680,y=100,width=140,height=35)
        self.btn_clear=Button(self.root,text="Clear",font=("goudy old style",15,"bold"),bg="#607d8b",fg="white",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=830,y=100,width=100,height=35)

        lbl_roll=Label(self.root,text="Roll No",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        lbl_roll.place(x=150,y=230,width=150,height=50)
        lbl_name=Label(self.root,text="Name ",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        lbl_name.place(x=300,y=230,width=150,height=50)
        lbl_course=Label(self.root,text="Course ",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        lbl_course.place(x=450,y=230,width=150,height=50)
        lbl_mark=Label(self.root,text="Mark Obtained ",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        lbl_mark.place(x=600,y=230,width=150,height=50)
        lbl_fullmarks=Label(self.root,text="Total Marks ",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        lbl_fullmarks.place(x=750,y=230,width=150,height=50)
        lbl_per=Label(self.root,text="Percentage",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        lbl_per.place(x=900,y=230,width=150,height=50)

        self.roll=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.roll.place(x=150,y=280,width=150,height=50)
        self.name=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.name.place(x=300,y=280,width=150,height=50)
        self.course=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.course.place(x=450,y=280,width=150,height=50)
        self.mark=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.mark.place(x=600,y=280,width=150,height=50)
        self.fullmarks=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.fullmarks.place(x=750,y=280,width=150,height=50)
        self.per=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.per.place(x=900,y=280,width=150,height=50)

        self.btn_delete=Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="red",fg="white",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=500,y=350,width=150,height=35)

#================================
    def search(self):
         con=sqlite3.connect(database="rms.db")

         cur=con.cursor()
         try:
            if self.var_search.get()=="":
                messagebox.showerror("Error","Roll no should be required",parent=self.root)
            else:
                cur.execute("select * from result where roll=?",(self.var_search.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.var_id=row[0]
                    self.roll.config(text=row[1])
                    self.name.config(text=row[2])
                    self.course.config(text=row[3])
                    self.mark.config(text=row[4])
                    self.fullmarks.config(text=row[5])
                    self.per.config(text=row[6])

                else:
                    messagebox.showerror("Error","No Record Found",parent=self.root)

         except Exception as ex:
             messagebox.showerror("Error",f"Error due to {str(ex)}")
 
    def clear(self):
        self.var_id=""
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.mark.config(text="")
        self.fullmarks.config(text="")
        self.per.config(text="")
        self.var_search.set("")

    def delete(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if  self.var_id=="":
                 messagebox.showerror("Error","Search Student Result First ",parent=self.root)
            else:
                cur.execute("select * from result where cid=?",(self.var_id,))
                row=cur.fetchone()
                 
                if row==None:
                    messagebox.showerror("Error","Invalid student Result",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete",parent=self.root)
                    if op==True:
                        cur.execute("delete from result where cid=?",(self.var_id,))
                        con.commit()
                        messagebox.showinfo("Delete","Result delete successfully",parent=self.root)
                        self.clear()


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")



if __name__=="__main__":
    root=Tk()
    obj=ReportClass(root)
    root.mainloop()