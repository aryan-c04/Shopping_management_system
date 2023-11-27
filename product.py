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

        #===column 1
        lbl_category=Label(self.root,text="Category",font=("goudy old style",18),bg="white").place(x=30,y=60)
        lbl_supplier=Label(self.root,text="Supplier",font=("goudy old style",18),bg="white").place(x=30,y=110)
        lbl_product_name=Label(self.root,text="Name",font=("goudy old style",18),bg="white").place(x=30,y=160)
        lbl_price=Label(self.root,text="Price",font=("goudy old style",18),bg="white").place(x=30,y=210)
        lbl_quantity=Label(self.root,text="Quantity",font=("goudy old style",18),bg="white").place(x=30,y=260)
        lbl_status=Label(self.root,text="Status",font=("goudy old style",18),bg="white").place(x=30,y=310)


        #===column 2
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
        
 







if __name__=='__main__':
    root=Tk()
    obj=productClass(root)
    root.mainloop()
