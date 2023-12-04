from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
class BillClass:
    def __init__ (self,root):
        self.root=root
        self.root.geometry=("1350*700+0+0")
        self.root.title("Shopping Managment System  | Developed by Team 3")
        self.root.config(bg='white')
        #===Title===#
        self.icon_title=PhotoImage(file="images/logo1.png")
        title=Label(self.root,text="Shopping Managment System",image=self.icon_title,compound=LEFT,font=('times new roman',40,"bold"),bg="#010c48",fg='white').place(x=0,y=0,relwidth=1,height=70)

        #===btnLogout===#
        btn_logout=Button(self.root,text="Logout",font=("times new roman",15,'bold'),bg="yellow",cursor='hand2').place(x=1350,y=10,height=30,width=150)
        #===clock===#
        self.lbl_clock=Label(self.root,text="Welcome to Shopping Managment System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=('times new roman',15),bg="#4d636d",fg='white')
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
 


       #=====Product======#
        self.var_search=StringVar()
        ProductFrame1=Frame(self.root,bd=4,relief=RIDGE,bg='white')
        ProductFrame1.place(x=6,y=110,width=410,height=550)

        pTitle=Label(ProductFrame1,text="All Products",font=("goudy old style",20,"bold"),bg='#262626',fg="white").pack(side=TOP,fill=X)

        ProductFrame2=Frame(ProductFrame1,bd=4,relief=RIDGE,bg='white')
        ProductFrame2.place(x=2,y=42,width=398,height=90)

        lbl_search=Label(ProductFrame2,text="Search Product | By Name ",font=("times new roman",15,'bold'),bg='white',fg='green').place(x=2,y=5)

        lbl_search=Label(ProductFrame2,text='Product Name',font=("times new roman",15,'bold'),bg='white').place(x=5,y=45)
        txt_search=Entry(ProductFrame2,textvariable=self.var_search,font=("times new roman",15),bg='lightyellow').place(x=128,y=47,width=150,height=22)
        btn_search=Button(ProductFrame2,text='Search',font=("goudy old style",15),bg="#2196f3",fg='white',cursor="hand2").place(x=285,y=45,width=100,height=25)
        btn_show_all=Button(ProductFrame2,text='Show All',font=("goudy old style",15),bg="#083531",fg='white',cursor="hand2").place(x=285,y=10,width=100,height=25)

        ProductFrame3=Frame(ProductFrame1,bd=3,relief=RIDGE)
        ProductFrame3.place(x=2,y=140,width=398,height=375)

        scrolly=Scrollbar(ProductFrame3,orient=VERTICAL)
        scrollx=Scrollbar(ProductFrame3,orient=HORIZONTAL)

        self.productTable=ttk.Treeview(ProductFrame3,columns=("pid","name","price","qty",'status'),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        self.productTable.heading("pid",text="PID")
        self.productTable.heading("name", text="Name")
        self.productTable.heading("price", text="Price")
        self.productTable.heading("qty", text="QTY")
        self.productTable.heading("status", text="Status")
        self.productTable["show"]="headings"
        
        self.productTable.column("pid",width=90)
        self.productTable.column("name",width=100)
        self.productTable.column("price",width=100)
        self.productTable.column("qty",width=100)
        self.productTable.column("status",width=100)
        self.productTable.pack(fill=BOTH,expand=1)
        #self.productTable.bind('<ButtonRelease-1>',self.get_data)
        lbl_not=Label(ProductFrame3,text="Note:'Enter 0 Quantity to remove product from the Cart' ",font=("goudy old style",12),anchor='w',bg="white",fg='red').pack(side=BOTTOM,fill=X)
         
       
#==========================================================================================================================#
    






if __name__=='__main__':
    root=Tk()
    obj=BillClass(root)
    root.mainloop()
        
         

