from tkinter import*
import sqlite3
from tkinter import messagebox
from PIL import Image,ImageTk
from course import CourseClass
from course import CourseClass
from student import StudentClass
from result import ResultClass
from report import ReportClass
class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #logo
        self.logo_dash=ImageTk.PhotoImage(file="images/im.1.png")
#title
        title=Label(self.root,text="Student Result Management System",padx=10,compound=LEFT,image=self.logo_dash,font=("goudy old style",20,"bold"),bg="#033295",fg="white").place(x=0,y=0,relwidth=1,height=50)
#menu
        M_Frame=LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white")
        M_Frame.place(x=10,y=70,width=350,height=600)

        btn_course=Button(M_Frame,text="Course",font=("goudy old style",15,"bold"),bg="#0b5399",fg="white",cursor="hand2",command=self.add_course).place(x=80,y=50,width=200,height=40)
        btn_course=Button(M_Frame,text="Student",font=("goudy old style",15,"bold"),bg="#0b5399",fg="white",cursor="hand2",command=self.add_student).place(x=80,y=190,width=200,height=40)
        btn_course=Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5399",fg="white",cursor="hand2",command=self.add_result).place(x=80,y=330,width=200,height=40)
        btn_course=Button(M_Frame,text="View Result",font=("goudy old style",15,"bold"),bg="#0b5399",fg="white",cursor="hand2",command=self.add_report).place(x=80,y=470,width=200,height=40)
        #content_window
        self.bg_img=Image.open("images/im.3.png")
        self.bg_img=self.bg_img.resize((1120,400))#,Image.ANTIALIAS
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=400,y=180,width=1120,height=400)

        self.lbl_course=Label(self.root,text="Totle Course [0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#2196f3",fg="white",cursor="hand2")
        self.lbl_course.place(x=400,y=80,width=300,height=70)

        self.lbl_students=Label(self.root,text="Totle Students [0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#4caf50",fg="white",cursor="hand2")
        self.lbl_students.place(x=810,y=75,width=300,height=70)

        self.lbl_result=Label(self.root,text="Totle Result [0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#607d8b",fg="white",cursor="hand2")
        self.lbl_result.place(x=1220,y=75,width=300,height=70)

        #footer
        footer=Label(self.root,text="SRMS-Student Result Management System\ncontect us for any Technical Issue : 99******11\n Created by: Gaurav & Vishal Sharma",font=("goudy old style",12),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)
        self.upd_detail()


    

    
    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)

    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=StudentClass(self.new_win)

    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=ResultClass(self.new_win)

    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=ReportClass(self.new_win)

    def upd_detail(self):
        con=sqlite3.connect(database="rms.db")

        cur=con.cursor()
        try:
            cur.execute("select * from course")
            cr=cur.fetchall()
            self.lbl_course.config(text=f"Total Course[{str(len(cr))}]")

            cur.execute("select * from student")
            cr=cur.fetchall()
            self.lbl_students.config(text=f"Totle Students[{str(len(cr))}]")

            cur.execute("select * from result")
            cr=cur.fetchall()
            self.lbl_result.config(text=f"Total Result[{str(len(cr))}]")


            self.lbl_course.after(200,self.upd_detail)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")



if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()