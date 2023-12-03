from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
class productClass:
    def __init__ (self,root):
        self.root=root
        self.root.geometry("1073x523+200+123")
        self.root.title("Shopping Managment System  | Developed by Team 3")
        self.root.config(bg='white')
        self.root.focus_force()

        #=============================
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        
        self.var_cat=StringVar()
        self.var_sup=StringVar()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()

        
        
        product_Frame=Frame(product_Frame,bd=2,relief=RIDGE,bg="white")
        product_Frame.place(x=10,y=10,width=450,height=480)

        #============title==================
        
        
        title=Label(self.root,text="Manage Product Details",font=("goudy old style",18),bg="#0f4d7d",fg="white").pack(side=TOP,fill=X)

        #========column 1===========
        lbl_category=Label(self.root,text="Category",font=("goudy old style",18),bg="white").place(x=30,y=60)
        lbl_supplier=Label(self.root,text="Supplier",font=("goudy old style",18),bg="white").place(x=30,y=110)
        lbl_product_name=Label(self.root,text="Name",font=("goudy old style",18),bg="white").place(x=30,y=160)
        lbl_price=Label(self.root,text="Price",font=("goudy old style",18),bg="white").place(x=30,y=210)
        lbl_quantity=Label(self.root,text="Quantity",font=("goudy old style",18),bg="white").place(x=30,y=260)
        lbl_status=Label(self.root,text="Status",font=("goudy old style",18),bg="white").place(x=30,y=310)


        #========column 2==========
        cmd_cat=ttk.Combobox(product_Frame,textvariable=self.var_cat,values=("Select"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmd_cat.place(x=150,y=60,width=200)
        cmd_cat.current(0)
        
        
        cmd_sup=ttk.Combobox(product_Frame,textvariable=self.var_sup,values=("Select"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmd_sup.place(x=150,y=110,width=200)
        cmd_sup.current(0)
        
        
        txt_name=Entry(product_Frame,textvariable=self.var_name,font=("goudy old style",15),bg='lightyellow').place(x=150,y=160,width=200)
        txt_price=Entry(product_Frame,textvariable=self.var_price,font=("goudy old style",15),bg='lightyellow').place(x=150,y=210,width=200)
        txt_quantity=Entry(product_Frame,textvariable=self.var_qty,font=("goudy old style",15),bg='lightyellow').place(x=150,y=260,width=200)

        cmd_status=ttk.Combobox(product_Frame,textvariable=self.var_status,values=("Active","Inactive"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmd_status.place(x=150,y=310,width=200)
        cmd_status.current(0)
        
        #========Buttons==========
        
        btn_add=Button(product_Frame, text="Save", command=self.add, font=("goudy old style", 15),bg="#2196f3",fg="white", cursor="hand2").place(x=10, y=400, width=100,height=40)
        btn_update=Button(product_Frame, text="Update", command=self.update, font=("goudy old style", 15),bg="#4caf50",fg="white", cursor="hand2").place(x=120, y=400, width=100,height=40)
        btn_delete=Button(product_Frame, text="Delete", command=self.delete, font=("goudy old style",15),bg="#f44336",fg="white", cursor="hand2").place(x=230, y=400, width=100,height=40)
        btn_clear=Button(self.root,text="Clear",command=self.clear, font=("goudy old style",15),bg="#607d8b",fg="white", cursor="hand2").place(x=10, y=340, width=100,height=40)
        
        
        #===searhFrame===#
        SearchFrame=LabelFrame(self.root,text="Search Employee",font=('goudy old style',12,'bold'),bg='white')
        SearchFrame.place(x=480,y=10,width=600,height=80)
  

         #===options===#
        cmd_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Category","Supplier","Name"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmd_search.place(x=10,y=10,width=180)
        cmd_search.current(0)

        txt_search = Entry(SearchFrame,textvariable=self.var_searchtxt,font=('goudy old style', 15), bg='lightyellow').place(x=200,y=10)
        btn_search= Button(SearchFrame,text="Search",font=('goudy old style', 15), bg='#4caf50',fg="white",cursor="hand2").place(x=410,y=9,width=150,height=30)

 
#Copy the db from employee(Around 15-18 minustes from vid 6)


        #=============Product-Details==================
        p_frame=Frame(self.root,bd=3, relief=RIDGE)
        p_frame.place(x=480, y=100, width=600, height=390)
        scrolly=Scrollbar (p_frame, orient=VERTICAL)
        scrollx=Scrollbar(p_frame, orient=HORIZONTAL)
        self.product_table=ttk.Treeview(p_frame, columns=("pid","Category", "Supplier","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)
        
        self.product_table.heading ("pid", text="P ID")
        self.product_table.heading("Category", text="Category")
        self.product_table.heading ("Supplier", text="Supplier")
        self.product_table.heading("name", text="name")
        self.product_table.heading ("price", text="price")
        self.product_table.heading ("qty", text="Quantity")
        self.product_table.heading ("status", text="Status")
        
        self.product_table.column("pid",width=90)      
        self.product_table.column("Category",width=100)
        self.product_table.column("Supplier",width=100)
        self.product_table.column("name",width=100)
        self.product_table.column("price",width=100)
        self.product_table.column("qty",width=100)
        self.product_table.column("status",width=100)
        self.product_table.pack(fill=BOTH, expand=1)
        self.product_table.bind("<ButtonRelease-1>", self.get_data)
        
        self.show()
                
                
        
        
        






if __name__=='__main__':
    root=Tk()
    obj=productClass(root)
    root.mainloop()
