from tkinter import*
from PIL import Image, ImageTk
class IMS:
    def __init__ (self,root):
        self.root=root
        self.root.geometry=("1350*700+0+0")
        self.root.title("Shopping Managment System  | Developed by Team 3")
        self.root.config(bg='white')
        #===Title===#
        self.icon_title=PhotoImage(file="images/logo1.png")
        title=Label(self.root,text="Shopping Managment System",image=self.icon_title,compound=LEFT,font=('times new roman',40,"bold"),bg="#010c48",fg='white').place(x=0,y=0,relwidth=1,height=70)

        #===btnLogout===#
        btn_logout=Button(self.root,text="Logout",font=("times new roman",15,'bold'),bg="yellow",cursor='hand2').place(x=1100,y=10,height=30,width=150)
        #===clock===#
        self.lbl_clock=Label(self.root,text="Welcome to Shopping Managment System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=('times new roman',15),bg="#4d636d",fg='white')
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        

        #===Left Menu===#
        
