from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
class employeeClass:
    def __init__ (self,root):
        self.root=root
        self.root.geometry("1073x523+200+123")
        self.root.title("Shopping Managment System  | Developed by Team 3")
        self.root.config(bg='white')
        self.root.focus_force()


        #===searhFrame===#
        SearchFrame=LabelFrame(self.root,text="Search Employee",font=('goudy old style',12,'bold'),bg='white')
        SearchFrame.place(x=250,y=20,width=600,height=70)


if __name__=='__main__':
    root=Tk()
    obj=employeeClass(root)
    root.mainloop()
