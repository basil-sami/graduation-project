import datetime
import sqlite3
import tkinter
import ttkbootstrap
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import traceback
import Addtional_features
from Addtional_features import *
from tkinter import *
from tkcalendar import Calendar
from datetime import *
from datetime import datetime
# ADMIN MENU
class Admin:
    def __init__(self, mainw):
        self.mainw = mainw
        self.cond == 0
    # ADD ADMIN MAIN MENU TO WINDOW,ALL FRAMES AND ADD IMAGE BUTTONS
    def admin_mainmenu(self, a, b):

        self.limitlist = []
        self.sumlist=[]
        self.bfe = False

        self.failelines = []
        self.fai = []
        self.pointer = 0
        self.pointer2=0
        self.columns = ("ProductID", "Product_Name", "Product_Desc", "Product_Cat",
                        'Product_Price', 'Stocks')
        self.mainframe = ttkbootstrap.Frame(self.mainw, width=1200, height=145, bootstyle="secondary")
        self.mainframe.place(x=0, y=100)
        mi = PhotoImage(file="../pythonProject4/images/accounts.png")
        self.mi1 = PhotoImage(file="../pythonProject4/images/add.png")
        self.mi2 = PhotoImage(file="../pythonProject4/images/remove.png")
        self.mi1 = self.mi1.subsample(a, b)
        self.mi2 = self.mi2.subsample(a, b)
        mi = mi.subsample(a, b)
        self.accounts = Button(self.mainframe, text="Profiles", font="roboto 11 bold", bd=3, image=mi, compound=TOP,

relief='raised', command=self.buildusertable)
        self.accounts.image = mi
        self.accounts.place(x=420, y=27)
        mi = PhotoImage(file="../pythonProject4/images/inventory.png")
        mi = mi.subsample(a, b)
        self.locations = Button(self.mainframe, text="locations", font="roboto 11 bold", bd=5, image=mi, compound=TOP,
                                command=self.buildlocationtable)
        self.locations.image = mi
        self.locations.place(x=700, y=27)
        mi = PhotoImage(file="../pythonProject4/images/Door_Out-512.png")
        mi = mi.subsample(a, b)
        self.logout = ttkbootstrap.Button(self.mainframe, text="Quit", image=mi, compound=TOP, bootstyle="success")
        self.logout.image = mi
        self.logout.place(x=1080, y=27)
        mi = PhotoImage(file="../pythonProject4/images/change1.png")
        mi = mi.subsample(a, b)
        self.changeuser = Button(self.mainframe, text="Sign out", bd=5, font="roboto 11 bold", image=mi, compound=TOP)
        self.changeuser.image = mi
        self.changeuser.place(x=960, y=27)
        mi = PhotoImage(file="../pythonProject4/images/items.png")
        mi = mi.subsample(a, b)
        self.items = Button(self.mainframe, text="Items", bd=5, image=mi, font="roboto 11 bold", compound=TOP,
                            command=self.additems)
        self.items.image = mi
        self.items.place(x=140, y=27)
        mi = PhotoImage(file="../pythonProject4/images/items.png")
        mi = mi.subsample(a, b)
        self.schedule = Button(self.mainframe, text="schedule", bd=5, image=mi, font="roboto 11 bold", compound=TOP,
                            command=self.popschedulea)
        self.schedule.image = mi
        self.schedule.place(x=840, y=27)
        mi = PhotoImage(file="../pythonProject4/images/inventory.png")
        mi = mi.subsample(a, b)
        mi = PhotoImage(file="images/orders2.png")
        mi = mi.subsample(a, b)
        self.aitems = Button(self.mainframe, text="orders", bd=5, font="roboto 11 bold", image=mi,
                             compound=TOP, command=self.make_invoice2)
        self.aitems.image = mi
        self.aitems.place(x=0, y=27)
        self.stocks = Button(self.mainframe, text="Inventory", bd=5, image=mi, font="roboto 11 bold", compound=TOP,
                             command=self.buildprodtable)
        self.stocks.image = mi
        self.stocks.place(x=280, y=27)
        mi = PhotoImage(file="../pythonProject4/images/requests.png")
        mi = mi.subsample(a, b)
        self.sales = Button(self.mainframe, text="requests", bd=5, font="roboto 11 bold", image=mi, compound=TOP,
                            command=self.buildsalestable)
        self.sales.image = mi
        self.formframe2 = Frame(self.mainw, width=600, height=750, bg="#FFFFFF")
        self.formframe2.place(x=350, y=430)
        self.tableframe1 = Frame(self.mainw, width=150, height=400, bg="#FFFFFF")
        self.tableframe1.place(x=1130, y=270, anchor=NE)
        self.tableframe1info = self.tableframe1.place_info()
        self.tableframe4 = Frame(self.mainw, width=150, height=400, bg="#FFFFFF")
        self.tableframe4.place(x=330, y=330, anchor=NW)
        self.tableframe4info = self.tableframe4.place_info()
        self.tableframe = Frame(self.mainw, width=350, height=700, bg="#FFFFFF")
        self.tableframe.place(x=400, y=300, anchor=NE)
        self.sales.place(x=560, y=27)
        self.formframe = Frame(self.mainw, width=500, height=550, bg="#FFFFFF")
        self.formframe.place(x=350, y=315)
        self.formframeinfo = self.formframe.place_info()

        self.formframe2info = self.formframe2.place_info()
        self.tableframe3 = LabelFrame(self.mainw, width=450, height=700)
        self.tableframe3.place(x=1050, y=315, anchor=NE)
        self.tableframe3info = self.tableframe3.place_info()
        self.tableframe2 = LabelFrame(self.mainw, width=450, height=700)
        self.tableframe2.place(x=250, y=315, anchor=NW)
        self.tableframe2info = self.tableframe2.place_info()
        self.itemframe = Frame(self.mainw, bg="#FFFFFF", width=600, height=300)
        self.itemframe.place(x=320, y=280, anchor=NW)
        self.itemframeinfo = self.itemframe.place_info()
        self.formframe1 = Frame(self.mainw, width=500, height=445, bg="#FFFFFF")
        self.formframe1.place(x=0, y=275)
        self.formframe1info = self.formframe1.place_info()
        self.searchframe = Frame(self.mainw, width=600, height=70, bg="#FFFFFF")
        self.searchframe.place(x=250, y=260)

        self.searchframeinfo = self.searchframe.place_info()
        self.searchbut = Button(self.searchframe, text="Search Description", font="roboto 14", bg="#FFFFFF", bd=5,
                                command=self.searchprod)
        self.searchbut.place(x=0, y=20, height=40)

        self.searchbut3 = Button(self.searchframe, text="updatedp", font="roboto 14", bg="#FFFFFF", bd=5, )

        self.select = ()
        self.searchvar = StringVar()
        self.searchentry = myentry(self.searchframe, textvariable=self.searchvar, font="roboto 14", width=25,
                                   bg="#FFFFFF")
        self.searchvar2 = StringVar()

        self.searchs = mycombobox(self.searchframe, textvariable=self.searchvar2,text='search', font="roboto 14", width=10, )
        self.searchs['values'] = self.columns
        self.searchs['state'] = 'normal'
        self.searchentry.place(x=110, y=20, height=40)
        self.searchs.place(x=450, y=20, height=40)
        self.entryframe = Frame(self.mainw, width=800, height=350, bg="#FFFFFF")
        self.entryframe.place(x=710, y=460 + 20)
        self.entryframeinfo = self.entryframe.place_info()
        self.entryframe1 = Frame(self.mainw, width=500, height=350, bg="#FFFFFF")
        self.entryframe1.place(x=130, y=470 + 20)
        self.entryframe1info = self.entryframe1.place_info()
        self.cur.execute("select product_desc from products")
        li = self.cur.fetchall()
        a = []
        for i in range(0, len(li)):
            a.append(li[i][0])
        self.searchentry.set_completion_list(a)
        self.resetbut = Button(self.searchframe, text="Reset", font="roboto 14", bd=5, width=8, bg="#FFFFFF",
                               command=self.resetprodtabel)
        self.resetbut.place(x=510, y=18, height=40)

        self.cond = 0

        self.buildprodtable()

    # ADMIN MAIN MENU ENDS

    # BUILD PRODUCT TABLE AT INVENTORY
    def buildprodtable(self):
        self.tableframe3.place_forget()
        self.entryframe.place_forget()
        self.entryframe1.place_forget()
        self.tableframe1.place_forget()
        self.tableframe.place_forget()
        self.searchframe.place_forget()
        self.formframe.place_forget()
        self.tableframe2.place_forget()
        self.itemframe.place_forget()
        self.formframe1.place_forget()
        self.tableframe4.place_forget()
        self.formframe2.place_forget()


        self.tableframe2.place(self.tableframe2info)
        self.formframe.place(self.formframeinfo)

        self.itemeditv = StringVar()
        self.itemeditdescv = StringVar()
        self.itemeditcatv = StringVar()
        self.itemeditpricev = StringVar()
        self.itemeditstockv = StringVar()
        self.addstock = StringVar()

        if (self.cond == 1):
            self.tree.delete(*self.tree.get_children())
            self.tree.grid_remove()
            self.tree.destroy()
            self.cond == 0
        self.columns = ("ProductID", "Product_Name", "Product_Desc", "Product_Cat",
                        'Product_Price', 'Stocks')
        scrollbarx = ttkbootstrap.Scrollbar(self.tableframe2, orient=HORIZONTAL, bootstyle='secondary')
        scrollbary = ttkbootstrap.Scrollbar(self.tableframe2, orient=VERTICAL, bootstyle='secondary')
        self.tree = ttkbootstrap.Treeview(self.tableframe2, columns=(self.columns), selectmode="browse", height=18,
                                          yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set,
                                          bootstyle='info')
        self.cond == 1
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=100)
        self.tree.column('#2', stretch=NO, minwidth=0, width=100)
        self.tree.column('#3', stretch=NO, minwidth=0, width=150)
        self.tree.column('#4', stretch=NO, minwidth=0, width=150)
        self.tree.column('#5', stretch=NO, minwidth=0, width=100)
        self.tree.column('#6', stretch=NO, minwidth=0, width=100)
        self.tree.heading('ProductID', text="Product ID", anchor=W)
        self.tree.heading('Product_Name', text="Product Name", anchor=W)
        self.tree.heading('Product_Desc', text="Description", anchor=W)
        self.tree.heading('Product_Cat', text="Category", anchor=W)
        self.tree.heading('Product_Price', text="Price", anchor=W)
        self.tree.heading('Stocks', text="Stocks", anchor=W)
        self.tree.grid(row=1, column=0, sticky="W")
        scrollbary.config(command=self.tree.yview)
        scrollbarx.grid(row=2, column=0, sticky="we")
        scrollbarx.config(command=self.tree.xview)
        scrollbary.grid(row=1, column=1, sticky="ns", pady=30)
        for col in self.columns:
            self.tree.heading(col, command=lambda _col=col: \
                Addtional_features.treeview_sort_column(self.tree, _col, False))
        self.getproducts()
        self.tree.bind("<<TreeviewSelect>>", self.clickprodtable)
        self.formframe.focus_set()

        Button(self.formframe, text="Update", font="robot 11 bold", bg="#FFFFFF", bd=5, width=10, height=2,
               command=self.changeprodtable).place(x=105, y=361)
        Button(self.formframe, text="Remove", font="robot 11 bold", bg="#FFFFFF", bd=5, width=10, height=2,
               command=self.delproduct).place(x=205, y=361)
        Button(self.formframe, text="open", font="robot 11 bold", bg="#FFFFFF", bd=5, width=10, height=2,
               command=self.importexele).place(x=305, y=361)
        Button(self.formframe, text="save", font="robot 11 bold", bg="#FFFFFF", bd=5, width=10, height=2,
               command=self.exportexele).place(x=405, y=361)

        Button(self.formframe, text="ASSIGN ", font="robot 11 bold", bg="#FFFFFF", bd=5, width=10, height=2,
               command=self.assign).place(x=0, y=361)
        self.cond = 1
        self.mainsearch(1)


    def importexele(self):

        Addtional_features.importexele(self.tree, self.columns)

    def exportexele(self):
        print(self.tree.get_children())

        Addtional_features.exportexele(self.tree)

    # SEARCH FRAME FOR BOTH USER AND PRODUCT TABLE
    def mainsearch(self, f):
        self.searchvar.set('')
        self.bt1 = Button(self.searchframe, text="open", font="robot 11 bold", bg="#FFFFFF", bd=5, width=10,
                          height=2,
                          command=self.importexele)
        self.bt2 = Button(self.searchframe, text="save", font="robot 11 bold", bg="#FFFFFF", bd=5, width=10,
                          height=2,
                          command=self.exportexele)
        self.bt3 = Button(self.searchframe, text="updatedp", font="robot 11 bold", bg="#FFFFFF", bd=5, width=10,
                          height=2,
                          command=self.write2)
        if (f == 1):


            self.searchs['values'] = self.columns
            self.searchframe.config(width=820)
            self.searchframe.place(x=200, y=245)
            self.searchs.current(0)

            self.searchs.bind('<<ComboboxSelected>>', self.searchprod2)
            self.searchbut.config(text="Search" + self.searchs.get(), command=self.searchprod)
            self.select == self.columns
            self.searchbut3.config(text="updatedp", command=self.write)
            self.searchs.place(x=550, y=23, height=40)

            self.searchbut3.place(x=750, y=20, height=40)
            self.searchs.update()
            self.searchbut.place(x=0, y=23, height=37)
            self.searchentry.config(textvariable=self.searchvar, width=20)
            self.searchentry.place(x=210, y=25, height=35)
            self.cur.execute("select " + self.searchs.get() + " from products")
            li = self.cur.fetchall()
            a = []
            for i in range(0, len(li)):
                a.append(li[i][0])
            self.searchentry.set_completion_list(a)
            self.resetbut.config(command=self.resetprodtabel)
            self.resetbut.place(x=460, y=22, height=37)
        elif (f == 0):

            self.searchframe.place(x=661, y=245)
            self.searchframe.config(width=520)
            self.searchbut.config(command=self.searchuser)
            self.searchbut.config(text="Search Username")
            self.searchbut.place(x=0, y=23)

            self.searchentry.config(width=18, textvariable=self.searchvar)
            self.searchentry.place(x=195, y=25, height=35)
            self.resetbut.config(command=self.resetusertable)
            self.resetbut.place(x=415, y=23)
            self.cur.execute("select username from users")
            li = self.cur.fetchall()
            a = []
            for i in range(0, len(li)):
                a.append(li[i][0])
            self.searchentry.set_completion_list(a)
        elif (f == 2):
            self.searchs['values'] = self.columns
            self.searchs.current(0)

            self.searchframe.place(x=50, y=245)
            self.searchbut3.place_forget()


            self.searchs.place(x=550, y=23, height=40)
            self.searchs.bind('<<ComboboxSelected>>', self.searchsales2)

            self.searchframe.config(width=1100)

            self.bt1.place(x=900, y=23)
            self.bt3.place(x=1000, y=23)
            self.bt2.place(x=800, y=23)
            self.searchbut.config(command=self.searchinvoice)
            self.searchbut.config(text="Search invoice No.")
            self.searchbut.place(x=0, y=23)

            self.searchentry.config(width=18, textvariable=self.searchvar)

            self.searchentry.place(x=195, y=25, height=35)
            self.resetbut.config(command=self.buildsalestable)

            self.resetbut.place(x=415, y=23)
            self.cur.execute("select invoice from sales")
            li = self.cur.fetchall()
            a = []
            # print(li)
            for i in range(0, len(li)):
                if (a.count(str(li[i][0])) == 0):
                    a.append(str(li[i][0]))
            self.searchentry.set_completion_list(a)
        else:
            self.bt1.place_forget()
            self.bt1.place_forget()
            self.bt1.place_forget()


            self.searchs['values'] = self.columns
            self.searchframe.config(width=820)
            self.searchframe.place(x=240, y=245)
            self.searchs.current(0)
            self.resetbut.config(command=self.buildlocationtable)


            self.searchbut.config(text="Search" + self.searchs.get(), command=self.searchloc)
            self.select == self.columns
            self.searchbut3.config(text="updatedp", command=self.write3)
            self.searchs.place(x=550, y=23, height=40)
            self.searchs.bind('<<ComboboxSelected>>', self.searchloc2)

            self.searchbut3.place(x=750, y=20, height=40)
            self.searchs.update()
            self.searchbut.place(x=0, y=23, height=37)
            self.searchentry.config(textvariable=self.searchvar, width=20)
            self.searchentry.place(x=210, y=25, height=35)
            self.cur.execute("select " + self.searchs.get() + " from location")
            self.cur.execute("select location_id from location")
            li = self.cur.fetchall()
            a = []
            # print(li)
            for i in range(0, len(li)):
                if (a.count(str(li[i][0])) == 0):
                    a.append(str(li[i][0]))
            self.searchentry.set_completion_list(a)

    # FETCH PRODUCTS FROM PRODUCTS TABLE
    def getproducts(self, x=0):
        ans = ''
        self.cur.execute("select * from products ORDER BY product_desc ASC")
        productlist = self.cur.fetchall()
        for i in productlist:
            self.tree.insert('', 'end', values=(i))
            if (str(x) == i[0]):
                a = self.tree.get_children()
                ans = a[len(a) - 1]

        return ans

    # MODIFIES RECORD OF PRODUCT TABLE
    def changeprodtable(self):
        if not(self.tree.selection()):
                return
        self.formwin= ttkbootstrap.Toplevel()
        self.formwin.title('assign to location ')
        self.formwin.geometry('600x550+700+200')
        self.form=ttkbootstrap.Frame(self.formwin,width=500,height=500)
        Label(self.formwin,text='update product ',font="roboto 14 bold",).grid(column=0,row=0)
        self.form.grid(column=0,row=1)


        va = 5
        l1 = ['Product Name', 'Description', 'Category', 'Price', 'Current Stock', 'Add Stock']
        for i in range(0, 6):
            Label(self.form, text=l1[i], font="roboto 14 bold", bg="#FFFFFF").place(x=100, y=va)
            va += 60
        Entry(self.form, textvariable=self.itemeditv, font="roboto 14", bg="#FFFFFF", width=20).place(x=242, y=0,
                                                                                                           height=40)
        Entry(self.form, textvariable=self.itemeditdescv, font="roboto 14", bg="#FFFFFF", width=20).place(x=242,
                                                                                                               y=60,
                                                                                                               height=40)
        x = myentry(self.form, textvariable=self.itemeditcatv, font="roboto 14", bg="#FFFFFF", width=20)
        x.place(x=242, y=120, height=40)
        self.cur.execute("select product_cat from products")
        li = self.cur.fetchall()
        a = []
        self.desc_name = []
        for i in range(0, len(li)):
            if (a.count(li[i][0]) == 0):
                a.append(li[i][0])
        x.set_completion_list(a)
        Entry(self.form, textvariable=self.itemeditpricev, font="roboto 14", bg="#FFFFFF", width=20).place(x=242,
                                                                                                                y=180,
                                                                                                                height=40)
        Entry(self.form, textvariable=self.itemeditstockv, font="roboto 14", bg="#FFFFFF", width=20).place(x=242,
                                                                                                                y=240,
                                                                                                                height=40)
        Entry(self.form, textvariable=self.addstock, font="roboto 14", bg="#FFFFFF", width=20).place(x=242, y=300,
                                                                                                          height=40)
        Button(self.form, text='apply', command=self.aplaychng, width=20).place(x=242, y=360,
                                                                                                     height=40)
    def aplaychng(self):
        cur = self.tree.selection()
        cur = self.tree.item(cur)
        li = cur['values']
        self.itemeditv.set((self.itemeditv.get()).upper())
        self.itemeditcatv.set((self.itemeditcatv.get()).upper())
        self.itemeditdescv.set((self.itemeditdescv.get()).upper())
        if (len(li) == 7):
            if self.itemeditv.get() == '' or self.itemeditdescv.get() == '':
                messagebox.showerror("Error", "Please Fill All Fields")
                return
            elif self.itemeditcatv.get() == '' or self.itemeditstockv.get() == '' or self.itemeditpricev.get() == '':
                messagebox.showerror("Error", "Please Fill All Fields")
                return
            else:
                l = [self.itemeditpricev.get(), self.itemeditstockv.get()]
                for i in range(0, len(l)):
                    if (not l[i].isdigit()):
                        messagebox.showerror("Error", "Invalid Data Provided")
                        return
                    elif (int(l[i]) < 0):
                        messagebox.showerror("Error", "Invalid Data Provided")
                        return
            if (self.addstock.get() == ''):
                self.addstock.set('0')

            self.cur.execute(
                "update products set product_name=?,product_desc=?,product_cat=?,product_price = ?,stocks = ? where productid = ?;",
                (
                self.itemeditv.get(), self.itemeditdescv.get(), self.itemeditcatv.get(), int(self.itemeditpricev.get()),
                (int(self.itemeditstockv.get()) + int(self.addstock.get())), li[0]))
            self.base.commit()
            self.addstock.set('')
            self.tree.delete(*self.tree.get_children())
            cur = self.getproducts(li[0])
            self.tree.selection_set(cur)
            messagebox.showinfo('success','product updated')
            self.formwin.destroy()

    def delproduct(self):
        cur = self.tree.focus()
        cur = self.tree.item(cur)
        li = cur['values']
        if messagebox.askyesno('Alert!', 'Do you want to remove product from inventory?') == True and len(li) == 7:
            self.cur.execute("delete from products where productid = ?;", (li[0],))
            self.cur.execute("delete from sales where product_id = ?;", (li[0],))
            self.cur.execute("delete from allocation where product_id = ?;", (li[0],))
            self.base.commit()
            self.tree.delete(*self.tree.get_children())
            self.getproducts()
            self.itemeditv.set('')
            self.itemeditdescv.set('')
            self.itemeditcatv.set('')
            self.itemeditstockv.set('')
            self.itemeditpricev.set('')

    def searchsales2(self,event):


        self.searchbut.config(text="Search" + self.searchs.get())
        self.cur.execute("select * from sales")
        li = []
        saleslist = self.cur.fetchall()
        for i in range(0, len(saleslist)):
            saleslist[i] = list(saleslist[i])
            self.cur.execute("select product_desc,product_price from products where productid=?",
                             (int(saleslist[i][2]),))
            l = self.cur.fetchall()
            s = (str(saleslist[i][4])).split('-')

            saleslist[i][4] = s[2] + " - " + s[1] + " - " + s[0]
            saleslist[i] = [saleslist[i][0], saleslist[i][1], saleslist[i][2], l[0][0], saleslist[i][3],
                            int(l[0][1]) * (int(saleslist[i][3])), saleslist[i][6], saleslist[i][7],
                            saleslist[i][4], saleslist[i][5]]
            li.append(saleslist[i])
            li
        a = []
        for i in range(0, len(li)):
            if (a.count(str(li[i][self.searchs.current()])) == 0):
                a.append(str(li[i][self.searchs.current()]))
        self.searchentry.set_completion_list(a)

    def searchprod2(self,event):
        print(self.searchvar2.get())

        self.searchbut.config(text="Search" + self.searchs.get())
        self.cur.execute("select " + self.searchs.get() + " from products")
        li = self.cur.fetchall()
        a = []
        for i in range(0, len(li)):
            a.append(li[i][0])
        self.searchentry.set_completion_list(a)

    def searchloc2(self,event):
        self.searchvar.set('')
        self.tree.delete(*self.tree.get_children())
        self.getlocation()
        self.searchbut.config(text="Search" + self.searchs.get())
        self.cur.execute("select " + self.searchs.get() + " from location")
        li = self.cur.fetchall()
        a = []
        for i in range(0, len(li)):
            a.append(str(li[i][0]))
        self.searchentry.set_completion_list(a)

    def searchprod(self):
        if (self.searchvar.get() == ''):
            return
        self.tree.delete(*self.tree.get_children())
        self.cur.execute("select * from products")
        li = self.cur.fetchall()
        for i in li:
            if (i[self.searchs.current()] == self.searchvar.get()):
                self.tree.insert('', 'end', values=(i))

    def searchloc(self):
        if (self.searchvar.get() == ''):
            return
        self.tree.delete(*self.tree.get_children())
        self.cur.execute("select * from location")
        li = self.cur.fetchall()
        for i in li:
            if (str(i[self.searchs.current()]) == str(self.searchvar.get())):
                self.tree.insert('', 'end', values=(i))

    def resetprodtabel(self):
        self.searchvar.set('')
        self.tree.delete(*self.tree.get_children())
        self.getproducts()

    def resetsales(self):
        self.searchvar.set('')
        self.tree.delete(*self.tree.get_children())
        self.getsales()

    # ONCLICK EVENT FOR PRODUCT TABLE
    def resetdashboard(self,f):
        if (self.bfe):
         if(self.buttonframe.winfo_children()):




          for widgets in self.buttonframe.winfo_children():
            widgets.destroy()
            self.bfe = False

        date = datetime(year=self.a2.SelectedYear.get(),
                        month=self.a2.Month_Names.index(self.a2.SelectedMonthName.get()),
                        day=self.a2.SelectedDay.get())
        self.date_time_obj = date
        if f==0:
         self.cur.execute(
            'select sum(quantity) from allocation where product_id=' + str(self.li[0]) + ' and date=("' + str(
                self.date_time_obj) + '")')
        else:
            self.cur.execute(
            'select sum(quantity) from allocation where location_id=' + str(self.li[0]) + ' and date=("' + str(
                self.date_time_obj) + '")')
        print(self.li[0])



        g = self.cur.fetchall()
        if f==0:
         self.limit = self.li[5]
        self.current = g[0][0]


        if (self.current):
            if f==0:

             self.pb1 = ttkbootstrap.Meter(self.threshold_box, arcrange=360, bootstyle="info", amounttotal=self.li[5],
                                          textleft='usage', textright='/' + str(self.li[5]))
            else :
                self.pb1 = ttkbootstrap.Meter(self.threshold_box, arcrange=360, bootstyle="info",
                                              amounttotal=g[0][0],
                                              textleft='usage')

            self.pb1['amountused'] = self.current
            self.pb1.grid(column=0, row=5, columnspan=3)
            if f==0 :
             self.lel = ttkbootstrap.Label(self.threshold_box, text='locations assigned to :', font="robot 10 bold",
                                          bootstyle="inverse-info", ).grid(row=6, column=0,
                                                                           pady=5, columnspan=2,
                                                                           padx=10, ipady=3)
            else :
                self.lel = ttkbootstrap.Label(self.threshold_box, text='products assigned to :', font="robot 10 bold",
                                              bootstyle="inverse-info", ).grid(row=6, column=0,
                                                                               pady=5, columnspan=2,
                                                                               padx=10, ipady=3)
            if f==0:
             self.cur.execute(
                'select locationname,quantity from allocation where product_id=' + str(
                    self.li[0]) + ' and date=("' + str(
                    date) + '")')
            else:
                self.cur.execute(
                    'select productname,quantity,product_id from allocation where location_id=' + str(
                        self.li[0]) + ' and date=("' + str(
                        date) + '")')

            self.d = self.cur.fetchall()

            i = 0
            self.list = []
            for values in self.d:
                self.list.append(values[1])
            self.change = False

            self.buildbuttonframe()
        else:
            if f==0:
             self.lel = ttkbootstrap.Label(self.threshold_box, text='not assigned to any location this date :',
                                          font="robot 10 bold",
                                          bootstyle="inverse-info", ).grid(row=6, column=0,
                                                                           pady=5, columnspan=2,
                                                                           padx=10, ipady=3)
            else :
                self.lel = ttkbootstrap.Label(self.threshold_box, text='nothing assigned to  location this date :',
                                              font="robot 10 bold",
                                              bootstyle="inverse-info", ).grid(row=6, column=0,
                                                                               pady=5, columnspan=2,
                                                                               padx=10, ipady=3)
    def clrdash(self):
        for widgets in self.threshold_box.winfo_children():
            widgets.destroy()

    def clickprodtable(self, event):
        self.fr=0
        cur = self.tree.selection()
        cur = self.tree.item(cur)
        for widgets in self.threshold_box.winfo_children():
            widgets.destroy()
        self.change = False
        self.pointer2=1

        li = cur['values']
        self.li = li

        print(li[0])
        if (len(li) == 7):
            self.itemeditv.set((li[1]))
            self.itemeditdescv.set((li[2]))
            self.itemeditcatv.set((li[3]))
            self.itemeditpricev.set(str(li[4]))
            self.itemeditstockv.set(str(li[5]))
            self.addstock.set('')

            self.cur.execute('select * from products where productid = ?', (int(li[0]),))
            ttkbootstrap.Label(self.threshold_box, text='product name :', font="robot 10 bold",
                               bootstyle="inverse-info", ).grid(row=0, column=0)
            ttkbootstrap.Label(self.threshold_box, text=li[1], font="robot 10 bold", bootstyle="inverse-info", ).grid(
                row=0, column=1, )
            ttkbootstrap.Label(self.threshold_box, text='product desc :', font="robot 10 bold",
                               bootstyle="inverse-info", ).grid(row=1, column=0,)
            ttkbootstrap.Label(self.threshold_box, text=li[2
            ], font="robot 10 bold", bootstyle="inverse-info", ).grid(row=1, column=1)
            ttkbootstrap.Label(self.threshold_box, text='product cat :', font="robot 10 bold",
                               bootstyle="inverse-info", ).grid(row=2, column=0)
            ttkbootstrap.Label(self.threshold_box, text=li[3], font="robot 10 bold", bootstyle="inverse-info", ).grid(
                row=2, column=1)
            ttkbootstrap.Button(self.threshold_box, text='schedule', command=self.popschedule).grid(column=0, row=3)
            ttkbootstrap.Label(self.threshold_box, text='chose date:', font="robot 10 bold",
                               bootstyle="inverse-info", ).grid(row=4, column=0, pady=5,
                                                                padx=10, ipady=3)
            self.a2 = spin()
            frame1 = Frame(self.threshold_box)
            self.a2.spinframe(frame1)
            frame1.grid(row=5, column=0, columnspan=2)
            ttkbootstrap.Button(self.threshold_box, text='set', command=lambda :self.resetdashboard(0)).grid(column=2,row=5)
            date = datetime(year=self.a2.SelectedYear.get(),
                            month=self.a2.Month_Names.index(self.a2.SelectedMonthName.get()),
                            day=self.a2.SelectedDay.get())
            self.date_time_obj = date
            self.cur.execute(
                'select sum(quantity) from allocation where product_id=' + str(li[0]) + ' and date=("' + str(
                    self.date_time_obj) + '")')
            g = self.cur.fetchall()
            self.limit = li[5]
            self.current = g[0][0]
            self.buttonframe = ttkbootstrap.Frame(self.threshold_box, bootstyle="info")
            self.buttonframe.grid(row=6, column=0, columnspan=3)
            if (self.current):
                self.pb1 = ttkbootstrap.Meter(self.threshold_box, arcrange=360, bootstyle="info", amounttotal=li[5],
                                              textleft='usage', textright='/' + str(li[5]))
                self.pb1['amountused'] = self.current
                self.pb1.grid(column=0, row=6, columnspan=3)

                self.lel = ttkbootstrap.Label(self.threshold_box, text='locations assigned to :', font="robot 10 bold",
                                              bootstyle="inverse-info", ).grid(row=6, column=0,
                                                                               pady=5, columnspan=2,
                                                                               padx=10, ipady=3)
                self.cur.execute('select locationname,quantity from allocation where product_id=' + str(
                    li[0]) + ' and date=("' + str(date) + '")')
                self.d = self.cur.fetchall()

                i = 0
                self.list = []
                self.listt = []

                for values in self.d:
                    self.list.append(values[1])

                    self.listt.append(values[1])
                self.buildbuttonframe()
            else:
                self.lel = ttkbootstrap.Label(self.threshold_box, text='not assigned to any location this date :',
                                              font="robot 10 bold",
                                              bootstyle="inverse-info", ).grid(row=6, column=0,
                                                                               pady=5, columnspan=2,
                                                                               padx=10, ipady=3)

    def add(self, i):
        if self.fr==0:
         if self.current + 1 <= self.limit:
            self.list[i] += 1
            print(self.list)
            self.change = True
            for widgets in self.buttonframe.winfo_children():
                widgets.destroy()
            self.buildbuttonframe()
            self.current += 1
            self.pb1['amountused'] = self.current



         else:
            messagebox.showerror('error', 'over stock limit for that day')
        else:
            print (self.limitlist)
            if self.current+self.sumlist[i][0][0] + 1 <= int(self.limitlist[i][0][0]):
                self.list[i] += 1
                print(self.list)
                self.change = True
                for widgets in self.buttonframe.winfo_children():
                    widgets.destroy()
                self.buildbuttonframe()
                self.current += 1
                self.pb1['amountused'] = self.current



            else:
                messagebox.showerror('error', 'over stock limit for that day')

    def remove(self, i):
        if self.list[i] >= 1:

            self.list[i] -= 1
            self.current -= 1
            self.pb1['amountused'] = self.current
            self.change = True

            for widgets in self.buttonframe.winfo_children():
                widgets.destroy()
            self.buildbuttonframe()

    def buildbuttonframe(self):
        self.bfe=True

        i = 0

        for values in self.d:
            ttkbootstrap.Label(self.buttonframe, text=values[0], font="robot 10 bold", bootstyle="inverse-info", ).grid(
                row=i,
                column=0,
                pady=6,
                padx=10,
                ipady=3,
                sticky=W)


            ttkbootstrap.Label(self.buttonframe, text=str(self.list[i]) + ' units', font="robot 10 bold",
                               bootstyle="inverse-info", ).grid(row=i,
                                                                column=1,
                                                                pady=6,
                                                                padx=10,
                                                                ipady=3,
                                                                sticky=W)

            ttkbootstrap.Button(self.buttonframe, text='+', bootstyle="success",
                                command=(lambda x=i: self.add(x))).grid(row=i, column=2, )
            ttkbootstrap.Button(self.buttonframe, text='-', bootstyle="danger",
                                command=(lambda x=i: self.remove(x))).grid(row=i, column=3)
            print(self.fr)

            if self.fr==1 :

               self.cur.execute("select stocks from products where productid =?",(int(values[2]),))
               g = self.cur.fetchall()
               self.cur.execute(
                   'select sum(quantity) from allocation where product_id=' + str(values[2]) + ' and date=("' + str(
                       self.date_time_obj) + '")')
               print(self.date_time_obj)
               c = self.cur.fetchall()

               print(c)
               self.limitlist.append(g)
               self.sumlist.append(c)

            i += 1

        ttkbootstrap.Button(self.buttonframe, text='apply', bootstyle="info",
                            command=(self.apply)).grid(row=i, column=0, columnspan=3)
        if i > 5:
            scrollbary = ttkbootstrap.Scrollbar(self.box, orient=VERTICAL, bootstyle='secondary')
            self.box.config(yscrollcommand=scrollbary.set)
            scrollbary.grid(row=1, column=1, sticky="ns", pady=30)

    def apply(self):
        i = 0
        print(self.change)

        if self.change == True:
            print('buh')
            if (messagebox.askyesno("Alert!", "update the value?") == True):
                for values in self.d:


                    if self.list[i] == 0:
                        print(values[0])
                        if self.fr==0:
                         self.cur.execute(
                            'delete  from allocation where locationname ="' + values[0] + '" and product_id=' + str(
                                self.li[0]) + ' and date=("' + str(self.date_time_obj) + '")')
                        else :
                            self.cur.execute(
                                'delete  from allocation where productname ="' + values[0] + '" and location_id=' + str(
                                    self.li[0]) + ' and date=("' + str(self.date_time_obj) + '")')
                        listx = list(self.d)
                        listx.remove(values)
                        self.d = tuple(listx)
                        self.list.remove(self.list[i])
                        i -= 1
                    else:
                        if self.fr==0:
                         self.cur.execute(
                            'update  allocation  set quantity=' + str(self.list[i]) + ' where locationname ="' + values[
                                0] + '" and product_id=' + str(
                                self.li[0]) + ' and date=("' + str(self.date_time_obj) + '")')
                        else:
                            self.cur.execute(
                                'update  allocation  set quantity=' + str(self.list[i]) + ' where productname ="' +
                                values[
                                    0] + '" and location_id=' + str(
                                    self.li[0]) + ' and date=("' + str(self.date_time_obj) + '")')


                    i += 1
        self.base.commit()

        for widgets in self.buttonframe.winfo_children():
            widgets.destroy()

        self.buildbuttonframe()

    def clickloctable(self, event):
        cur = self.tree.selection()
        cur = self.tree.item(cur)
        self.fr = 1
        self.clrdash()
        li = cur['values']
        print(li)
        self.pointer2=2



        self.li = li
        if (len(li) == 5):
            self.itemeditv2.set((li[1]))
            self.itemeditdescv2.set((li[2]))
            self.itemeditcatv2.set((li[3]))
            self.itemeditpricev2.set(str(li[4]))

        self.cur.execute('select * from location where location_id = ?', (int(li[0]),))
        ttkbootstrap.Label(self.threshold_box, text='location name :', font="robot 10 bold",
                           bootstyle="inverse-info", ).grid(row=0, column=0, pady=5, padx=10, ipady=3, sticky=W)
        ttkbootstrap.Label(self.threshold_box, text=li[1], font="robot 10 bold", bootstyle="inverse-info", ).grid(row=0,
                                                                                                                  column=1,
                                                                                                                  pady=5,
                                                                                                                  padx=10,
                                                                                                                  ipady=3)
        ttkbootstrap.Label(self.threshold_box, text='location cat :', font="robot 10 bold",
                           bootstyle="inverse-info", ).grid(row=1, column=0,
                                                            pady=5, padx=10,
                                                            ipady=3, sticky=(
                N, S, E, W))
        ttkbootstrap.Label(self.threshold_box, text=li[3
        ], font="robot 10 bold", bootstyle="inverse-info", ).grid(row=1, column=1, pady=5,
                                                                  padx=10, ipady=3,
                                                                  sticky=(N, S, E, W))
        ttkbootstrap.Label(self.threshold_box, text='product fac :', font="robot 10 bold",
                           bootstyle="inverse-info", ).grid(row=2, column=0,
                                                            pady=5, padx=10,
                                                            ipady=3, sticky=W)
        ttkbootstrap.Label(self.threshold_box, text=li[4], font="robot 10 bold", bootstyle="inverse-info", ).grid(row=2,
                                                                                                                  column=1,
                                                                                                                  pady=5,
                                                                                                                  padx=10,
                                                                                                                  ipady=3)
        ttkbootstrap.Label(self.threshold_box, text='chose date:', font="robot 10 bold",
                           bootstyle="inverse-info", ).grid(row=3, column=0, pady=5,
                                                            padx=10, ipady=3)

        ttkbootstrap.Button(self.threshold_box, text='schedule',command=self.popschedule).grid(column=1,row=4)
        self.a2 = spin()
        frame1 = Frame(self.threshold_box)
        self.a2.spinframe(frame1)
        frame1.grid(row=5, column=0, columnspan=2)
        ttkbootstrap.Button(self.threshold_box, text='set', command=lambda :self.resetdashboard(1)).grid(column=2, row=5)
        date = datetime(year=self.a2.SelectedYear.get(),
                        month=self.a2.Month_Names.index(self.a2.SelectedMonthName.get()),
                        day=self.a2.SelectedDay.get())
        self.date_time_obj = date
        self.cur.execute(
            'select sum(quantity) from allocation where location_id=' + str(li[0]) + ' and date=("' + str(
                self.date_time_obj) + '")')
        g = self.cur.fetchall()

        self.current = g[0][0]
        print(self.current)
        self.buttonframe = ttkbootstrap.Frame(self.threshold_box, bootstyle="info")
        self.buttonframe.grid(row=8, column=0, columnspan=3)
        if (self.current):
            self.pb1 = ttkbootstrap.Meter(self.threshold_box, arcrange=360, bootstyle="info", amounttotal=g[0][0],
                                          )
            self.pb1['amountused'] = self.current
            self.pb1.grid(column=0, row=6, columnspan=3)

            self.lel = ttkbootstrap.Label(self.threshold_box, text='products assigned to :', font="robot 10 bold",
                                          bootstyle="inverse-info", ).grid(row=7, column=0,
                                                                           pady=5, columnspan=2,
                                                                           padx=10, ipady=3)
            self.cur.execute(
                'select productname,quantity,product_id from allocation where location_id=' + str(li[0]) + ' and date=("' + str(
                    date) + '")')
            self.d = self.cur.fetchall()

            i = 0
            self.list = []


            for values in self.d:
                self.list.append(values[1])


            self.buildbuttonframe()
        else:
            self.lel = ttkbootstrap.Label(self.threshold_box, text='not assigned to any location this date :',
                                          font="robot 10 bold",
                                          bootstyle="inverse-info", ).grid(row=6, column=0,
                                                                           pady=5, columnspan=2,
                                                                           padx=10, ipady=3)

    # FUNCTION FOR ITEM BUTTON
    def additems(self):
        self.tableframe3.place_forget()
        self.entryframe.place_forget()
        self.entryframe1.place_forget()
        self.tableframe1.place_forget()
        self.tableframe.place_forget()
        self.searchframe.place_forget()
        self.formframe.place_forget()
        self.tableframe2.place_forget()
        self.itemframe.place_forget()
        self.formframe1.place_forget()
        self.tableframe4.place_forget()
        self.formframe2.place_forget()

        self.itemframe.place(self.itemframeinfo)

        self.newitem = StringVar()
        self.newitemdesc = StringVar()
        self.newitemcode = StringVar()
        self.newitemcat = StringVar()
        self.newitemprice = StringVar()
        self.newitemstock = StringVar()

        l = ['Product Id', "Product Name", "Description", "Category", "Price", "Stock"]
        for i in range(0, len(l)):
            Label(self.itemframe, text=l[i], font="Roboto 14 bold", bg="#ffffff").grid(row=i, column=0, pady=15,
                                                                                       sticky="w")
        Entry(self.itemframe, width=40, textvariable=self.newitemcode, font="roboto 11", bg="#ffffff").grid(row=0,
                                                                                                            column=1,
                                                                                                            pady=15,
                                                                                                            padx=10,
                                                                                                            ipady=3)
        Entry(self.itemframe, width=40, textvariable=self.newitem, font="roboto 11", bg="#ffffff").grid(row=1, column=1,
                                                                                                        pady=15,
                                                                                                        padx=10,
                                                                                                        ipady=3)
        Entry(self.itemframe, width=40, textvariable=self.newitemdesc, font="roboto 11", bg="#ffffff").grid(row=2,
                                                                                                            column=1,
                                                                                                            pady=15,
                                                                                                            padx=8,
                                                                                                            ipady=3)
        cat = myentry(self.itemframe, width=40, textvariable=self.newitemcat, font="roboto 11", bg="#ffffff")
        cat.grid(row=3, column=1, pady=15, padx=10, ipady=3)
        Entry(self.itemframe, width=40, textvariable=self.newitemprice, font="roboto 11", bg="#ffffff").grid(row=4,
                                                                                                             column=1,
                                                                                                             pady=15,
                                                                                                             padx=10,
                                                                                                             ipady=3)
        Entry(self.itemframe, width=40, textvariable=self.newitemstock, font="roboto 11", bg="#ffffff").grid(row=5,
                                                                                                             column=1,
                                                                                                             pady=15,
                                                                                                             padx=10,
                                                                                                             ipady=3)
        self.cur.execute("select product_cat,product_name,product_desc from products")
        li = self.cur.fetchall()
        a = []
        self.desc_name = []
        for i in range(0, len(li)):
            if (a.count(li[i][0]) == 0):
                a.append(li[i][0])
            self.desc_name.append(li[i][2])
        cat.set_completion_list(a)
        Button(self.itemframe, text="Add item", height=3, bd=6, command=self.insertitem, bg="#FFFFFF").grid(row=6,
                                                                                                            column=1,
                                                                                                            pady=10,
                                                                                                            padx=12,
                                                                                                            sticky="w",
                                                                                                            ipadx=10)
        Button(self.itemframe, text="Back", height=3, width=8, bd=6, command=self.buildprodtable, bg="#FFFFFF").grid(
            row=6, column=1, padx=16, pady=10, sticky="e", ipadx=10)

    # PERFOMS CHECK AND ADD'S ITEMS
    def insertitem(self):
        self.newitem.set((self.newitem.get()).upper())
        self.newitemdesc.set((self.newitemdesc.get()).upper())
        self.newitemcat.set((self.newitemcat.get()).upper())
        if self.newitemcode.get() == '' or self.newitem.get() == '' or self.newitemdesc.get() == '':
            messagebox.showerror("Error", "Please Fill All Fields")
            return
        elif self.newitemcat.get() == '' or self.newitemprice.get() == '' or self.newitemstock.get() == '':
            messagebox.showerror("Error", "Please Fill All Fields")
            return
        else:
            l = [self.newitemcode.get(), self.newitemprice.get(), self.newitemstock.get()]
            for i in range(0, len(l)):
                if (not l[i].isdigit()):
                    if (i == 0):
                        messagebox.showerror("Error", "Product ID should be in numeral")
                    else:
                        messagebox.showerror("Error", "Invalid Data Provided")
                    return
                elif (int(l[i]) < 0):
                    messagebox.showerror("Error", "Invalid Data Provided")
                    return
        self.cur.execute('select * from products where productid = ?', (int(self.newitemcode.get()),))
        l = self.cur.fetchall()
        if (len(l) > 0):
            messagebox.showerror("Error", "Product ID Should Be Unique")
            return
        if (self.desc_name.count(self.newitemdesc.get()) != 0):
            messagebox.showerror('Error', 'Product with same description exsits!')
            return
        x = int(self.newitemcode.get())
        y = int(self.newitemprice.get())
        z = int(self.newitemstock.get())
        self.cur.execute("insert into products values(?,?,?,?,?,?,?)", (x, self.newitem.get(), self.newitemdesc.get(),
                                                                      self.newitemcat.get(), y, z,z))
        self.newitem.set('')
        self.newitemstock.set('')
        self.newitemprice.set('')
        self.newitemdesc.set('')
        self.newitemcode.set('')
        self.newitemcat.set('')
        messagebox.showinfo('Success', 'Item Added Successfully')
        self.base.commit()

    # BUILD USER TABLE
    def buildusertable(self):
        self.tableframe3.place_forget()
        self.entryframe.place_forget()
        self.entryframe1.place_forget()
        self.tableframe1.place_forget()
        self.tableframe.place_forget()
        self.searchframe.place_forget()
        self.formframe.place_forget()
        self.tableframe2.place_forget()
        self.itemframe.place_forget()
        self.formframe1.place_forget()
        self.tableframe4.place_forget()
        self.formframe2.place_forget()
        self.clrdash()

        self.formframe1.place(self.formframe1info)
        self.tableframe3.place(self.tableframe3info)
        if (self.cond == 1):
            self.tree.delete(*self.tree.get_children())
            self.tree.grid_remove()
            self.tree.destroy()
            self.cond == 0
        self.columns = ("Username", "Password", "Account Type")

        scrollbarx = ttkbootstrap.Scrollbar(self.tableframe3, orient=HORIZONTAL, bootstyle='secondary')
        scrollbary = ttkbootstrap.Scrollbar(self.tableframe3, orient=VERTICAL, bootstyle='secondary')
        self.tree = ttkbootstrap.Treeview(self.tableframe3, bootstyle='info',
                                          columns=("Username", "Password", "Account Type",),
                                          selectmode="browse", height=17, yscrollcommand=scrollbary.set,
                                          xscrollcommand=scrollbarx.set)
        self.cond == 1
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=170)
        self.tree.column('#2', stretch=NO, minwidth=0, width=170)
        self.tree.column('#3', stretch=NO, minwidth=0, width=170)
        self.tree.heading('Username', text="Username", anchor=W)
        self.tree.heading('Password', text="Password", anchor=W)
        self.tree.heading('Account Type', text="Account Type", anchor=W)
        self.tree.grid(row=1, column=0, sticky=E)
        scrollbary.config(command=self.tree.yview)
        scrollbarx.grid(row=2, column=0, sticky="we")
        scrollbarx.config(command=self.tree.xview)
        scrollbary.grid(row=1, column=1, sticky="ns", pady=30)
        for col in self.columns:
            self.tree.heading(col,  command=lambda _col=col: \
                Addtional_features.treeview_sort_column(self.tree, _col, False))
        self.getusers()
        self.tree.bind("<<TreeviewSelect>>", self.clickusertable)
        self.formframe1.focus_set()
        self.usernamedit = StringVar()
        self.passwordedit = StringVar()
        self.accedit = StringVar()
        va = 110
        l1 = ['Username', 'Password', 'Profile Type']
        for i in range(0, 3):
            Label(self.formframe1, text=l1[i], font="roboto 14 bold", bg="#FFFFFF").place(x=0, y=va)
            va += 70
        Entry(self.formframe1, textvariable=self.usernamedit, font="roboto 14", bg="#FFFFFF", width=25,
              state='readonly').place(x=162, y=105, height=40)
        Entry(self.formframe1, textvariable=self.passwordedit, font="roboto 14", bg="#FFFFFF", width=25).place(x=162,
                                                                                                               y=175,
                                                                                                               height=40)
        profiles = mycombobox(self.formframe1, font="robot 14", width=23, textvariable=self.accedit)
        profiles.place(x=162, y=245, height=40)
        profiles.set_completion_list(['ADMIN', 'USER'])
        Button(self.formframe1, text="Create a User", font="robot 12 bold", bg="#FFFFFF", bd=5, width=12, height=2,
               command=self.adduser).place(x=0, y=10)
        Button(self.formframe1, text="Update", font="robot 12 bold", bg="#FFFFFF", bd=5, width=10, height=2,
               command=self.changeusertable).place(x=145, y=381)
        Button(self.formframe1, text="Remove", font="robot 12 bold", bg="#FFFFFF", bd=5, width=10, height=2,
               command=self.deluser).place(x=345, y=381)

        self.mainsearch(0)

    # FETCH USERS FROM USERS TABLE
    def getusers(self, x=0):
        ans = ''
        self.cur.execute("select * from users")
        userslist = self.cur.fetchall()
        for i in userslist:
            self.tree.insert('', 'end', values=(i))
            if (str(x) == i[0]):
                a = self.tree.get_children()
                ans = a[len(a) - 1]

        return ans

    def changeusertable(self):
        cur = self.tree.selection()
        cur = self.tree.item(cur)
        li = cur['values']
        self.usernamedit.set((self.usernamedit.get()).upper())
        self.passwordedit.set((self.passwordedit.get()).upper())
        self.accedit.set((self.accedit.get()).upper())
        if (len(li) == 3):
            if self.usernamedit.get() == '' or self.accedit.get() == '':
                messagebox.showerror("Error", "Please Fill All Fields")
                return
            if (self.accedit.get() != 'ADMIN' and self.accedit.get() != 'USER'):
                messagebox.showerror("Error", "Unknown account type!")
                return
            self.cur.execute(
                "update users set password = ?,account_type = ? where username = ?;", (
                    self.passwordedit.get(), self.accedit.get(), self.usernamedit.get()))
            self.base.commit()
            self.tree.delete(*self.tree.get_children())
            cur = self.getusers(li[0])
            self.tree.selection_set(cur)

    def deluser(self):
        cur = self.tree.focus()
        cur = self.tree.item(cur)
        li = cur['values']
        fa = 0
        if (self.username.get() == li[0]):
            if (messagebox.askyesno("Alert!", "Remove Current User?") == True):
                fa = 1
            else:
                return
        if messagebox.askyesno('Alert!', 'Do you want to remove this profile?') == True and len(li) == 3:
            self.cur.execute("delete from users where username = ?;", (li[0],))
            self.base.commit()
            self.tree.delete(*self.tree.get_children())
            self.getusers()
            self.usernamedit.set('')
            self.passwordedit.set('')
            self.accedit.set('')
        if (fa == 1):
            self.change_user()

    def adduser(self):
        self.loginw.title("Login")
        width = 500
        height = 600
        self.loginw.protocol('WM_DELETE_WINDOW', self.revert2)

        self.toplabel.config(text="Register")
        self.toplabel.grid(column=0, row=0)
        self.username.set("Choose your username")
        self.password.set("Create a password")
        self.signin.config(text="Ok", command=self.insert)
        # ADD
        self.register.grid(column=0, row=4)
        self.register.config(text="Back", command=self.revert2)
        self.signin.config()
        self.signin.grid(column=1, row=4)
        self.pa.grid(column=0, row=2)
        self.us.grid(column=0, row=1)
        self.pa2.grid(column=0, row=3)
        self.pa.config(show='')
        self.loginw.focus()
        self.loginw.bind('<Return>', self.insert)
        self.loginw.title('Register')
        self.loginw.state('normal')  # LOGIN WINDOW ENTERS

    def searchuser(self):
        if (self.searchvar.get() == ''):
            return
        self.tree.delete(*self.tree.get_children())
        self.cur.execute("select * from users")
        li = self.cur.fetchall()
        for i in li:
            if (i[0] == self.searchvar.get()):
                self.tree.insert('', 'end', values=(i))

    def resetusertable(self):
        self.searchvar.set('')
        self.tree.delete(*self.tree.get_children())
        self.getusers()

    def clickusertable(self, event):
        cur = self.tree.selection()
        cur = self.tree.item(cur)
        li = cur['values']
        if (len(li) == 3):
            self.usernamedit.set((li[0]))
            self.passwordedit.set((li[1]))
            self.accedit.set((li[2]))

    # BUILD sales TABLE
    def make_invoice_a(self):
        self.tableframe3.place_forget()
        self.entryframe.place_forget()
        self.entryframe1.place_forget()
        self.tableframe1.place_forget()
        self.tableframe.place_forget()
        self.searchframe.place_forget()
        self.formframe.place_forget()
        self.tableframe2.place_forget()
        self.itemframe.place_forget()
        self.formframe1.place_forget()
        self.tableframe4.place_forget()
        self.formframe2.place_forget()

        self.entryframe.place(self.entryframeinfo)
        self.entryframe1.place(self.entryframe1info)
        self.tableframe3.place(self.tableframe3info)
        if (self.cond == 1):
            self.tree.delete(*self.tree.get_children())
            self.tree.grid_remove()
            self.tree.destroy()
            self.cond == 0
        scrollbarx = ttkbootstrap.Scrollbar(self.tableframe3, orient=HORIZONTAL, bootstyle='secondary')
        scrollbary = ttkbootstrap.Scrollbar(self.tableframe3, orient=VERTICAL, bootstyle='secondary')
        self.tree = ttkbootstrap.Treeview(self.tableframe3, bootstyle='info',
                                          columns=("Transaction ID", "Product ID", "Product Name",
                                                   'Quantity', 'Price', 'Date', 'Time'), selectmode="browse",
                                          height=6, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        self.cond == 1
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=100)
        self.tree.column('#2', stretch=NO, minwidth=0, width=110)
        self.tree.column('#3', stretch=NO, minwidth=0, width=130)
        self.tree.column('#4', stretch=NO, minwidth=0, width=100)
        self.tree.column('#5', stretch=NO, minwidth=0, width=100)
        self.tree.column('#6', stretch=NO, minwidth=0, width=100)
        self.tree.column('#7', stretch=NO, minwidth=0, width=100)
        self.tree.heading('Transaction ID', text="Transaction ID", anchor=W)
        self.tree.heading('Product ID', text="Product ID", anchor=W)
        self.tree.heading('Product Name', text="Product Name", anchor=W)
        self.tree.heading('Quantity', text="Quantity", anchor=W)
        self.tree.heading('Price', text="Price", anchor=W)
        self.tree.heading('Date', text="Date", anchor=W)
        self.tree.heading('Time', text="Time", anchor=W)
        self.tree.grid(row=1, column=1, sticky="We")
        scrollbary.config(command=self.tree.yview)
        scrollbarx.grid(row=2, column=0, sticky="we")
        scrollbarx.config(command=self.tree.xview)
        scrollbary.grid(row=1, column=1, sticky="ns", pady=30)
        self.tree.bind("<<TreeviewSelect>>", self.clicktranstable)
        self.user_input()

    def buildsalestable(self):
        self.entryframe.place_forget()
        self.entryframe1.place_forget()
        self.tableframe1.place_forget()
        self.tableframe.place_forget()
        self.searchframe.place_forget()
        self.formframe.place_forget()
        self.tableframe2.place_forget()
        self.itemframe.place_forget()
        self.formframe1.place_forget()
        self.tableframe4.place_forget()
        self.formframe2.place_forget()
        self.clrdash()

        self.tableframe3.place(x=50, y=315, anchor=NW)
        self.tableframe3.config(width=600)
        if (self.cond == 1):
            self.tree.delete(*self.tree.get_children())
            self.tree.grid_remove()
            self.tree.destroy()
            self.cond == 0
            self.columns = ("Transaction ID", "invoice No.", "Product ID", "Description",
                            'Quantity', 'Total Price', 'user', 'priority', 'Date', 'Time')
        scrollbarx = ttkbootstrap.Scrollbar(self.tableframe3, orient=HORIZONTAL, bootstyle='secondary')
        scrollbary = ttkbootstrap.Scrollbar(self.tableframe3, orient=VERTICAL, bootstyle='secondary')
        self.tree = ttkbootstrap.Treeview(self.tableframe3, bootstyle='info', columns=self.columns, selectmode="browse",
                                          height=16,
                                          yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        self.cond == 1
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=100)
        self.tree.column('#2', stretch=NO, minwidth=0, width=100)
        self.tree.column('#3', stretch=NO, minwidth=0, width=120)
        self.tree.column('#4', stretch=NO, minwidth=0, width=150)
        self.tree.column('#5', stretch=NO, minwidth=0, width=100)
        self.tree.column('#6', stretch=NO, minwidth=0, width=100)
        self.tree.column('#7', stretch=NO, minwidth=0, width=100)
        self.tree.column('#8', stretch=NO, minwidth=0, width=90)
        self.tree.column('#9', stretch=NO, minwidth=0, width=90)
        self.tree.heading('Transaction ID', text="Transaction ID", anchor=W)
        self.tree.heading('invoice No.', text="invoice No.", anchor=W)
        self.tree.heading('Product ID', text="Product ID", anchor=W)
        self.tree.heading('Description', text="Description", anchor=W)
        self.tree.heading('Quantity', text="Quantity", anchor=W)
        self.tree.heading('Total Price', text="Total Price", anchor=W)
        self.tree.heading('user', text="user", anchor=W)
        self.tree.heading('priority', text="priority", anchor=W)
        self.tree.heading('Date', text="Date", anchor=W)
        self.tree.heading('Time', text="Time", anchor=W)
        self.tree.grid(row=1, column=0, sticky="W")
        scrollbary.config(command=self.tree.yview)
        scrollbarx.grid(row=2, column=0, sticky="we")
        scrollbarx.config(command=self.tree.xview)
        scrollbary.grid(row=1, column=1, sticky="ns", pady=30)
        for col in self.columns:
            self.tree.heading(col,  command=lambda _col=col: \
                Addtional_features.treeview_sort_column(self.tree, _col, False))
        self.getsales()
        self.mainsearch(2)
        self.totalsales = Label(self.tableframe3, text="Total sales", font="roboto 14 bold").place(x=0, y=400)

    def getsales(self):
        self.cur.execute("select * from sales")
        saleslist = self.cur.fetchall()
        for i in range(0, len(saleslist)):
            saleslist[i] = list(saleslist[i])
            self.cur.execute("select product_desc,product_price from products where productid=?",
                             (int(saleslist[i][2]),))
            l = self.cur.fetchall()
            s = (str(saleslist[i][4])).split('-')
            #  print(saleslist[i])
            saleslist[i][4] = s[2] + " - " + s[1] + " - " + s[0]
            saleslist[i] = [saleslist[i][0], saleslist[i][1], saleslist[i][2], l[0][0], saleslist[i][3],
                            int(l[0][1]) * (int(saleslist[i][3])), saleslist[i][6], saleslist[i][7],
                            saleslist[i][4], saleslist[i][5]]
        for i in saleslist:
            self.tree.insert('', 'end', values=(i))

    def searchinvoice(self):
        if (self.searchvar.get() == ''):
            return
        li = []
        self.tree.delete(*self.tree.get_children())
        self.cur.execute("select * from sales")
        saleslist = self.cur.fetchall()
        for i in range(0, len(saleslist)):
            saleslist[i] = list(saleslist[i])
            self.cur.execute("select product_desc,product_price from products where productid=?",
                             (int(saleslist[i][2]),))
            l = self.cur.fetchall()
            s = (str(saleslist[i][4])).split('-')
            saleslist[i][4] = s[2] + " - " + s[1] + " - " + s[0]
            saleslist[i] = [saleslist[i][0], saleslist[i][1], saleslist[i][2], l[0][0], saleslist[i][3],
                            int(l[0][1]) * (int(saleslist[i][3])), saleslist[i][6], saleslist[i][7],
                            saleslist[i][4], saleslist[i][5]]

            saleslist[i] = tuple(saleslist[i])
            li.append(saleslist[i])

        for i in range(0, len(li)):
            if (str(li[i][self.searchs.current()]) == str(self.searchvar.get())):
                self.tree.insert('', 'end', values=(li[i]))

    def revert2(self):
        if messagebox.askyesno("withdraw", " stop creating account?") == True:
            self.loginw.state('withdraw')

    def make_invoice2(self):
        self.tableframe3.place_forget()
        self.entryframe.place_forget()
        self.entryframe1.place_forget()
        self.tableframe1.place_forget()
        self.tableframe.place_forget()
        self.searchframe.place_forget()
        self.formframe.place_forget()
        self.tableframe2.place_forget()
        self.itemframe.place_forget()
        self.formframe1.place_forget()
        self.tableframe4.place_forget()
        self.formframe2.place_forget()

        self.make_invoice()
        self.cond == 1

    def write(self):
        ids = self.tree.get_children()
        dict = defaultdict(list)
        b = self.tree['column']
        errors = 0
        dup = 0
        self.failelines = []

        for id in ids:

            q = self.tree.item(id)["values"]
            print(q)
            print(b)

            try:
                self.cur.execute(
                    " insert into products (" + b[0] + "," + b[1] + "," + b[2] + "," + b[3] + "," + b[4] + "," + b[
                        5] + ") values (?,?,?,?,?,?)",
                    (int(q[0]), str(q[1]), str(q[2]), str(q[3]), str(q[4]), int(q[5])))
            except sqlite3.Error as er:

                errors = errors + 1

                s = ('SQLite error: %s' % (' '.join(er.args)))
                print('SQLite error: %s/n' % (' '.join(er.args)))
                print("Exception class is: ", er.__class__)
                print('SQLite traceback: ')
                exc_type, exc_value, exc_tb = sys.exc_info()
                print(traceback.format_exception(exc_type, exc_value, exc_tb))
                if ''.join(er.args) == 'UNIQUE constraint failed: products.productid':
                    dup = dup + 1

                    self.cur.execute('select * from products where productid =' + str(q[0]))
                    l = self.cur.fetchall()
                    self.fai.append(l)

                    l = (int(q[0]), str(q[1]), str(q[2]), str(q[3]), str(q[4]), int(q[5]))
                    self.failelines.append(l)

        self.base.commit()

        if errors > 0:
            messagebox.showinfo("error:" + str(errors) + 'duplicates' + str(dup), s)
            self.pointer = 1

            self.updatedppro()
        self.base.commit()

    def write2(self):
        ids = self.tree.get_children()
        dict = defaultdict(list)

        b = ('Trans_id', 'invoice', 'Product_id', 'Quantity', 'Date', 'Time', 'users', 'priority')
        errors = 0
        self.failelines = []

        for id in ids:
            q = self.tree.item(id)["values"]
            print(q)
            print(b)
            try:

                self.cur.execute(
                    " insert into sales (" + b[0] + "," + b[1] + "," + b[2] + "," + b[3] + "," + b[4] + "," + b[
                        5] + "," + b[6] + "," + b[7] + ") values (?,?,?,?,?,?,?,?)",
                    (int(q[0]), int(q[1]), str(q[2]), int(q[4]), str(q[8]), str(q[9]), str(q[6]), str(q[7])))
                # tansid invoice id quant date time use pio 0 1 2 4 8 9 6 7
            except sqlite3.Error as er:

                errors = errors + 1

                s = ('SQLite error: %s' % (' '.join(er.args)))
                print('SQLite error: %s/n' % (' '.join(er.args)))
                print("Exception class is: ", er.__class__)
                print('SQLite traceback: ')
                exc_type, exc_value, exc_tb = sys.exc_info()
                print(traceback.format_exception(exc_type, exc_value, exc_tb))
                if ''.join(er.args) == 'UNIQUE constraint failed: sales.Trans_id':
                    errors = errors + 1
                    self.cur.execute('select * from sales where Trans_id =' + str(q[0]))
                    l = self.cur.fetchall()
                    self.fai.append(l)
                    l = (
                    (int(q[0]), int(q[1]), str(q[2]), int(q[4]), str(q[8]), str(q[9]), str(q[6]), str(q[7]), str(q[3])))
                    self.failelines.append(l)
                    print(self.failelines)

        self.base.commit()

        if errors > 0:
            messagebox.showinfo("error:" + str(errors), s)
            self.pointer = 2

            self.updatedppro()

    def write3(self):
        ids = self.tree.get_children()
        dict = defaultdict(list)
        b = self.tree['column']
        errors = 0
        dup = 0
        self.failelines = []

        for id in ids:

            q = self.tree.item(id)["values"]
            print(q)
            print(b)

            try:
                self.cur.execute(
                    " insert into location (" + b[0] + "," + b[1] + "," + b[2] + "," + b[3] + "," + b[
                        4] + ") values (?,?,?,?,?)",
                    (int(q[0]), str(q[1]), str(q[2]), str(q[3]), str(q[4])))
            except sqlite3.Error as er:

                errors = errors + 1

                s = ('SQLite error: %s' % (' '.join(er.args)))
                print('SQLite error: %s/n' % (' '.join(er.args)))
                print("Exception class is: ", er.__class__)
                print('SQLite traceback: ')
                exc_type, exc_value, exc_tb = sys.exc_info()
                print(traceback.format_exception(exc_type, exc_value, exc_tb))
                if ''.join(er.args) == 'UNIQUE constraint failed: location.location_ID':
                    dup = dup + 1
                    self.cur.execute('select * from location where location_id =' + str(q[0]))
                    l = self.cur.fetchall()
                    self.fai.append(l)

                    l = (int(q[0]), str(q[1]), str(q[2]), str(q[3]), str(q[4]))
                    self.failelines.append(l)

        self.base.commit()

        if errors > 0:
            messagebox.showinfo("error:" + str(errors) + 'duplicates' + str(dup), s)
            self.pointer = 3

            self.updatedppro()
        self.base.commit()

    def buildlocationtable(self):
        self.clrdash()
        self.tableframe3.place_forget()
        self.entryframe.place_forget()
        self.entryframe1.place_forget()
        self.tableframe1.place_forget()
        self.tableframe.place_forget()
        self.searchframe.place_forget()
        self.formframe.place_forget()
        self.tableframe2.place_forget()
        self.itemframe.place_forget()
        self.formframe1.place_forget()
        self.formframe2.place(self.formframe2info)
        self.tableframe4.place(self.tableframe4info)
        self
        if (self.cond == 1):
            self.tree.delete(*self.tree.get_children())
            self.tree.grid_remove()
            self.tree.destroy()
            self.cond == 0
        self.columns = ("location_ID", "location_name", "location_Desc", "location_Cat",
                        'location_faculty')
        scrollbarx = ttkbootstrap.Scrollbar(self.tableframe4, orient=HORIZONTAL, bootstyle='secondary')
        scrollbary = ttkbootstrap.Scrollbar(self.tableframe4, orient=VERTICAL, bootstyle='secondary')
        self.tree = ttkbootstrap.Treeview(self.tableframe4, columns=(self.columns), selectmode="browse", height=18,
                                          yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set,
                                          bootstyle='info')
        self.cond == 1
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=100)
        self.tree.column('#2', stretch=NO, minwidth=0, width=100)
        self.tree.column('#3', stretch=NO, minwidth=0, width=150)
        self.tree.column('#4', stretch=NO, minwidth=0, width=150)
        self.tree.column('#5', stretch=NO, minwidth=0, width=100)

        self.tree.heading('location_ID', text="location ID", anchor=W)
        self.tree.heading('location_name', text="location Name", anchor=W)
        self.tree.heading('location_Desc', text="Description", anchor=W)
        self.tree.heading('location_Cat', text="Category", anchor=W)
        self.tree.heading('location_faculty', text="faculty", anchor=W)

        self.tree.grid(row=1, column=0, sticky="W")
        scrollbary.config(command=self.tree.yview)
        scrollbarx.grid(row=2, column=0, sticky="we")
        scrollbarx.config(command=self.tree.xview)
        scrollbary.grid(row=1, column=1, sticky="ns", pady=30)
        for col in self.columns:
            self.tree.heading(col,  command=lambda _col=col: \
                Addtional_features.treeview_sort_column(self.tree, _col, False))
        self.getlocation()
        self.tree.bind("<<TreeviewSelect>>", self.clickloctable)
        self.formframe2.focus_set()
        self.itemeditv2 = StringVar()
        self.itemeditdescv2 = StringVar()
        self.itemeditcatv2 = StringVar()
        self.itemeditpricev2 = StringVar()


        Button(self.formframe2, text="add", font="robot 11 bold", bg="#FFFFFF", bd=5, width=10, height=2,
               command=self.addloctable).place(x=5, y=261)
        Button(self.formframe2, text="Update", font="robot 11 bold", bg="#FFFFFF", bd=5, width=10, height=2,
               command=self.changeloctable).place(x=105, y=261)
        Button(self.formframe2, text="Remove", font="robot 11 bold", bg="#FFFFFF", bd=5, width=10, height=2,
               command=self.delloc).place(x=205, y=261)
        Button(self.formframe2, text="open", font="robot 11 bold", bg="#FFFFFF", bd=5, width=10, height=2,
               command=self.importexele).place(x=305, y=261)
        Button(self.formframe2, text="save", font="robot 11 bold", bg="#FFFFFF", bd=5, width=10, height=2,
               command=self.exportexele).place(x=405, y=261)

        Button(self.formframe2, text=" assign items", font="robot 11 bold", bg="#FFFFFF", bd=5, width=10, height=2,
               command=self.assign).place(x=505, y=261)

        self.mainsearch(3)



    def getlocation(self, x=0):
        ans = ''
        self.cur.execute("select * from location")
        productlist = self.cur.fetchall()
        for i in productlist:
            self.tree.insert('', 'end', values=(i))
            if (str(x) == str(i[0])):
                a = self.tree.get_children()
                ans = a[len(a) - 1]
        return ans


    def changeloctable(self):
        if not (self.tree.selection()):

            return
        self.buildlocform()

        Button(self.form2, text='apply', command=self.aplaychng2, width=20).place(x=242, y=360,
                                                                                height=40)
    def buildlocform(self):
        self.formwin2 = ttkbootstrap.Toplevel()
        self.formwin2.title('assign to location ')
        self.formwin2.geometry('600x550+700+200')
        self.form2 = ttkbootstrap.Frame(self.formwin2, width=500, height=500)
        Label(self.formwin2, text='update product ', font="roboto 14 bold", ).grid(column=0, row=0)
        self.form2.grid(column=0, row=1)

        va = 5
        l1 = ['location_name', 'location_Desc', 'location_Cat', 'location_faculty']
        for i in range(0, len(l1)):
            Label(self.form2, text=l1[i], font="roboto 14 bold", bg="#FFFFFF").place(x=100, y=va)
            va += 60
        Entry(self.form2, textvariable=self.itemeditv2, font="roboto 14", bg="#FFFFFF", width=20).place(x=242, y=0,
                                                                                                        height=40)
        Entry(self.form2, textvariable=self.itemeditdescv2, font="roboto 14", bg="#FFFFFF", width=20).place(x=242,
                                                                                                            y=60,
                                                                                                            height=40)
        self.cur.execute("select location_cat from location")
        li = self.cur.fetchall()
        a = []
        self.desc_name = []
        x = myentry(self.form2, textvariable=self.itemeditcatv2, font="roboto 14", bg="#FFFFFF", width=20)
        x2 = myentry(self.form2, textvariable=self.itemeditpricev2, font="roboto 14", bg="#FFFFFF", width=20)
        for i in range(0, len(li)):
            if (a.count(li[i][0]) == 0):
                a.append(li[i][0])
        x.set_completion_list(a)
        self.cur.execute("select location_faculty from location")
        li = self.cur.fetchall()
        a = []
        self.desc_name = []
        for i in range(0, len(li)):
            if (a.count(li[i][0]) == 0):
                a.append(li[i][0])
        x2.set_completion_list(a)

        x.place(x=242, y=120, height=40)

        x2.place(x=242, y=180, height=40)
    def aplaychng2(self):

        cur = self.tree.selection()
        cur = self.tree.item(cur)
        li = cur['values']
        self.itemeditv2.set((self.itemeditv2.get()).upper())
        self.itemeditcatv2.set((self.itemeditcatv2.get()).upper())
        self.itemeditdescv2.set((self.itemeditdescv2.get()).upper())
        self.itemeditpricev2.set((self.itemeditpricev2.get()).upper())
        if (len(li) == 5):
            if self.itemeditv2.get() == '' or self.itemeditdescv2.get() == '':
                messagebox.showerror("Error", "Please Fill All Fields")
                return
            elif self.itemeditcatv2.get() == '':
                messagebox.showerror("Error", "Please Fill All Fields")
                return

            self.cur.execute(
                "update location set location_name=?,location_Desc=?,location_Cat=?,location_faculty = ? where location_id = ?;",
                (self.itemeditv2.get(), self.itemeditdescv2.get(), self.itemeditcatv2.get(), self.itemeditpricev2.get(),
                 li[0]))
            self.tree.delete(*self.tree.get_children())
            print(li)
            cur = self.getlocation(li[0])
            print(cur)


            self.tree.selection_set(cur)

            messagebox.showinfo('success', 'product updated')
            self.formwin2.destroy()
            self.base.commit()


    def delloc(self):
        cur = self.tree.focus()
        cur = self.tree.item(cur)
        li = cur['values']
        if messagebox.askyesno('Alert!', 'Do you want to remove location from dp?') == True and len(li) == 5:
            self.cur.execute("delete from location where location_id = ?;", (li[0],))
            self.base.commit()
            self.tree.delete(*self.tree.get_children())
            self.getlocation()
            self.itemeditv2.set('')
            self.itemeditdescv2.set('')
            self.itemeditcatv2.set('')

            self.itemeditpricev2.set('')

    def addloctable(self):
        self.buildlocform()
        self.itemeditv2.set('')
        self.itemeditdescv2.set('')
        self.itemeditcatv2.set('')
        self.itemeditpricev2.set('')

        Button(self.form2, text='apply', command=self.aplaychng3, width=20).place(x=242, y=360,
                                                                                height=40)
    def aplaychng3(self):



        self.itemeditv2.set((self.itemeditv2.get()).upper())
        self.itemeditdescv2.set((self.itemeditdescv2.get()).upper())
        self.itemeditcatv2.set((self.itemeditcatv2.get()).upper())
        self.itemeditpricev2.set((self.itemeditpricev2.get()).upper())
        if self.itemeditv2.get() == '' or self.itemeditdescv2.get() == '' or self.itemeditcatv2.get() == '' or self.itemeditpricev2.get() == '':
            messagebox.showerror("Error", "Please Fill All Fields")
            return
        self.cur.execute(
            "insert into location (location_name,location_Desc,location_Cat,location_faculty)values(?,?,?,?)",
            (self.itemeditv2.get(), self.itemeditdescv2.get(),
             self.itemeditcatv2.get(), self.itemeditpricev2.get()))
        self.itemeditv2.set('')
        self.itemeditdescv2.set('')
        self.itemeditcatv2.set('')
        self.itemeditpricev2.set('')
        messagebox.showinfo('Success', 'Item Added Successfully')
        self.tree.delete(*self.tree.get_children())



        self.formwin2.destroy()
        self.base.commit()
        self.getlocation()
        self.base.commit()

    def assign(self):
        cur = self.tree.selection()
        cur = self.tree.item(cur)
        li = cur['values']
        self.a = StringVar()
        self.b = StringVar()
        c = StringVar()
        self.assignw = ttkbootstrap.Toplevel()
        self.assignw.title('assign to location ')
        self.assignw.geometry('600x550+700+200')
        self.searcha = mycombobox(self.assignw, text='search', textvar=self.a, font="roboto 14", width=15, )

        self.searchc = ttk.Spinbox(self.assignw, from_=1.0, to=100.0, textvariable=c, font="roboto 14", width=5, )
        self.searchc.grid(column=2, row=1, padx=5, pady=10, sticky='w')

        self.searchbut4 = ttk.Button(self.assignw, text='select', command=self.clicksearcha)
        self.searchbut5 = ttk.Button(self.assignw, text='assign', command=self.grad_date)
        self.searchbut4.grid(column=3, row=1, padx=5, pady=10, sticky='w')
        self.searchbut5.grid(column=3, row=6, padx=5, pady=10, sticky='w')
        label2 = ttk.Label(self.assignw, text='select product')
        label3 = ttk.Label(self.assignw, text='select location')
        self.label4 = ttk.Label(self.assignw, text='select amount')

        self.searchb = mycombobox(self.assignw, text='search', textvariable=self.b, font="roboto 14", width=15, )
        self.cur.execute("select product_desc from products ORDER BY product_desc ASC")
        lil = self.cur.fetchall()
        ab = []
        for i in range(0, len(lil)):
            ab.append(lil[i][0])
        self.searcha.set_completion_list(ab)
        if (bool(li)):
            label = ttk.Label(self.assignw, text='assign  ' + li[1] + ' to location')
            self.searchc = ttk.Spinbox(self.assignw, from_=1.0, to=li[5], textvariable=c, font="roboto 14", width=5, )
            self.searchc.grid(column=2, row=1, padx=5, pady=5, sticky='w')
            self.searcha.current(ab.index(li[2]))
        else:
            label = ttk.Label(self.assignw, text='assign  product  to location')

        ab = []
        self.cur.execute("select location_name from location")
        lil = self.cur.fetchall()
        for i in range(0, len(lil)):
            ab.append(lil[i][0])
        self.searchb.set_completion_list(ab)
        self.searcha.bind("<<ComboboxSelect>>", self.clicksearcha)
        self.assignw.protocol('WM_DELETE_WINDOW', self.__assign_del__)
        if (not bool(lil)):
            self.searcha.set('change product')
            self.searcha.bind('<Button-1> ', self.cleara)

        label.grid(column=0, row=0, padx=5, pady=10, sticky='w')
        label2.grid(column=0, row=1, padx=5, pady=10, sticky='w')
        label3.grid(column=0, row=2, padx=5, pady=10, sticky='w')
        label4 = ttk.Label(self.assignw, text='set assign period')
        label4.grid(column=0, row=3, padx=5, pady=10, sticky='w')
        self.a1 = spin()
        frame1 = Frame(self.assignw)
        self.a1.spinframe(frame1)
        self.b1 = spin()
        frame2 = Frame(self.assignw)
        self.b1.spinframe(frame2)

        frame1.grid(column=1, row=4, padx=5, pady=10, sticky='w')
        frame2.grid(column=1, row=5, padx=5, pady=10, sticky='w')
        label5 = ttk.Label(self.assignw, text='set start date')
        label5.grid(column=0, row=4, padx=5, pady=10, sticky='w')
        label6 = ttk.Label(self.assignw, text='set end date')
        label6.grid(column=0, row=5, padx=5, pady=10, sticky='w')

        self.searcha.grid(column=1, row=1, padx=5, pady=10, sticky='w')
        self.searchb.grid(column=1, row=2, padx=5, pady=10, sticky='w')

    def cleara(self, event):
        self.searcha.set('')

    def __assign_del__(self):
        if messagebox.askyesno("Quit", " stop assigin products ?") == True:

            self.assignw.destroy()

    def clicksearcha(self):
        if (self.searcha.get() == 'change product' or self.searcha.get() == ''):
            messagebox.showerror('error', 'no data was provided ')
            return
        print(self.searcha.get())

        self.cur.execute('select stocks from products where product_desc="' + self.searcha.get() + '"')
        a = self.cur.fetchall()
        print('buh')
        self.searchc = ttk.Spinbox(self.assignw, from_=1.0, to=a[0], font="roboto 14", width=5, )
        self.label4.grid(column=1, row=1, padx=5, pady=5, sticky='w')
        self.searchc.grid(column=2, row=1, padx=5, pady=5, sticky='w')

    def grad_date(self):
        if (self.searcha.get() == 'change product' or self.searcha.get() == ''):
            messagebox.showerror('error', 'no data was provided ')
            return
        if (self.searchb.get() == 'change product' or self.searchb.get() == ''):
            messagebox.showerror('error', 'no data was provided ')
            return
        if (self.searchc.get() == 'change product' or self.searchc.get() == ''):
            messagebox.showerror('error', 'no data was provided ')
            return

        date = datetime(year=self.a1.SelectedYear.get(),
                        month=self.a1.Month_Names.index(self.a1.SelectedMonthName.get()), day=self.a1.SelectedDay.get())
        date_time_obj1 = date
        date = datetime(year=self.b1.SelectedYear.get(),
                        month=self.b1.Month_Names.index(self.b1.SelectedMonthName.get()), day=self.b1.SelectedDay.get())
        date_time_obj2 = date

        errors = 0

        if date_time_obj1 > date_time_obj2:
            messagebox.showerror("Error", "end date is before start date")
            return
        else:
            per1 = pd.date_range(start=date_time_obj1,
                                 end=date_time_obj2, freq='1D')
            self.cur.execute(
                'select productid,product_name,stocks from products where product_desc="' + self.searcha.get() + '"')
            a = self.cur.fetchall()

            self.cur.execute(
                'select location_ID, location_name from location where location_name="' + self.searchb.get() + '"')
            b = self.cur.fetchall()
            self.cur.execute('select * from allocation')
            c = self.cur.fetchall()
            i = 0
            g = ''

            for values in per1:

                self.cur.execute(
                    'select sum(quantity) from allocation where product_id=' + str(a[0][0]) + ' and date=("' + str(
                        values) + '")')
                d = self.cur.fetchall()
                q = d[0][0]
                if (q == None):
                    q = 0

                print(d[0][0])
                if (a[i][2] < q + int(self.searchc.get())):
                    g = g + str(values) + '\\\n'
                    print(g)
            print(bool(g))

            if (bool(g)):
                messagebox.showerror('error', self.searcha.get() + 'dose not have free units avialable during ' + g)
                return

            print(c)

            for values in per1:
                try:
                    self.cur.execute(
                        'insert into allocation (location_id,product_id,date,locationname,productname,quantity) values (' + str(
                            b[0][0]) + ',' + str(a[0][0]) + ',"' + str(values) + '","' + str(b[0][1]) + '","' + str(
                            a[0][1]) + '",' + str(self.searchc.get() + ')'))
                except sqlite3.Error as er:

                    errors = errors + 1

                    s = ('SQLite error: %s' % (' '.join(er.args)))
                    print('SQLite error: %s' % (' '.join(er.args)))
                    print("Exception class is: ", er.__class__)
                    print('SQLite traceback: ')
                    exc_type, exc_value, exc_tb = sys.exc_info()
                    print(traceback.format_exception(exc_type, exc_value, exc_tb))
                    if ''.join(
                            er.args) == 'UNIQUE constraint failed: allocation.product_id, allocation.location_id, allocation.date':
                        l = (
                        str(b[0][0]), str(a[0][0]), str(values), str(b[0][1]), str(a[0][1]), str(self.searchc.get()))
                        self.failelines.append(l)

                        self.cur.execute('select * from products where product_id =? AND location_id=? and date=? ' +    (str(b[0][0]), str(a[0][0]), str(values)))
                        l = self.cur.fetchall()
                        self.fai.append(l)

        if errors > 0:
            messagebox.showinfo("error:" + str(errors) + 'duplicates')
            self.pointer = 4

            self.updatedppro()
            self.base.commit()
        self.base.commit()

        if errors == 0:
            messagebox.showinfo("Success", "process successful")

            self.__assign_del__()

    def updatedppro(self):

        self.rep = ttkbootstrap.Toplevel()
        self.rep.title('do u want to replace ')
        self.rep.geometry('500x500+300+300')
        lable = tkinter.Label(self.rep, text='the folllowing items are already assigned   ')
        lable.grid(column=0, row=0, padx=5, pady=5, sticky='w')
        text = Text(self.rep, width=60, height=10, wrap="none")
        ys = ttk.Scrollbar(self.rep, orient='vertical', command=text.yview)
        xs = ttk.Scrollbar(self.rep, orient='horizontal', command=text.xview)
        text.grid(column=0, row=1, padx=5, pady=5, sticky='w')
        xs.grid(column=0, row=2, sticky='we')
        ys.grid(column=1, row=1, sticky='ns')
        i = 0.0

        for values in self.failelines:
            text.insert('' + str(i), str(values) + '...\n')
            i = i + 1

        lable2 = tkinter.Label(self.rep, text='replace  ' + str(self.fai[0]) + '?')
        lable2.grid(column=0, row=3, padx=5, pady=5, sticky='w')
        frame = ttk.Frame(self.rep)
        frame.grid(column=0, row=4)

        if (self.pointer == 1):
            Button(frame, text="yes", command=self.replace1).grid(column=0, row=0, padx=5, pady=5, sticky='w')
            Button(frame, text="yes to all", command=self.replaceall).grid(column=1, row=0, padx=5, pady=5, sticky='w')
        elif (self.pointer == 2):
            Button(frame, text="yes", command=self.replace1s).grid(column=0, row=0, padx=5, pady=5, sticky='w')
            Button(frame, text="yes to all", command=self.replacealls).grid(column=1, row=0, padx=5, pady=5, sticky='w')
        elif (self.pointer == 3):
            Button(frame, text="yes", command=self.replace1l).grid(column=0, row=0, padx=5, pady=5, sticky='w')
            Button(frame, text="yes to all", command=self.replacealll).grid(column=1, row=0, padx=5, pady=5, sticky='w')
        else:
            Button(frame, text="yes", command=self.replace1a).grid(column=0, row=0, padx=5, pady=5, sticky='w')
            Button(frame, text="yes to all", command=self.replacealla).grid(column=1, row=0, padx=5, pady=5, sticky='w')
        Button(frame, text="no", command=self.skip1).grid(column=2, row=0, padx=5, pady=5, sticky='w')
        Button(frame, text="no to all", command=self.skipall).grid(column=3, row=0, padx=5, pady=5, sticky='w')

    def replace1(self):

        self.cur.execute('update products set product_name=("' + str(self.failelines[0][1]) + '"),'
                         + ' product_desc=("' + str(self.failelines[0][2]) + '"),'
                         + ' product_cat=("' + str(self.failelines[0][3]) + '"),' + ' product_price=' + str(
            self.failelines[0][4]) + ','
                         + ' stocks=' + str(self.failelines[0][5]) + ' where productid=' + str(self.failelines[0][0]))
        self.failelines.pop(0)
        self.fai.pop(0)

        self.base.commit()
        self.rep.destroy()
        if (bool(self.failelines)):
            self.updatedppro()

    def replace1a(self):

        self.cur.execute('update allocation set locationname=("' + str(self.failelines[0][3]) + '"),'
                         + ' productname=("' + str(self.failelines[0][4]) + '"),'
                         + ' quantity=quantity+' + str(self.failelines[0][5]) + ' where location_id=' + str(
            self.failelines[0][0]) + ' and product_id=' + str(self.failelines[0][1]) + ' and date="' + str(
            self.failelines[0][2]) + '"')
        self.failelines.pop(0)
        self.fai.pop(0)

        self.base.commit()
        self.rep.destroy()
        if (bool(self.failelines)):
            self.updatedppro()

    def replace1s(self):

        self.cur.execute('update sales set invoice=(' + str(self.failelines[0][1]) + '),'
                         + ' Product_id=(' + str(self.failelines[0][2]) + '),'
                         + ' Quantity=(' + str(self.failelines[0][3]) + '),' + ' Date="' + str(
            self.failelines[0][4]) + '",'
                         + ' Time=("' + str(self.failelines[0][5]) + '"), users="' + str(
            self.failelines[0][6]) + '",priority="' + str(self.failelines[0][7]) + '" where Trans_id=' + str(
            self.failelines[0][0]))
        self.failelines.pop(0)
        self.fai.pop(0)

        self.base.commit()
        self.rep.destroy()
        if (bool(self.failelines)):
            self.updatedppro()

    def replace1l(self):

        self.cur.execute('update location set location_name=("' + str(self.failelines[0][1]) + '"),'
                         + ' location_Desc=("' + str(self.failelines[0][2]) + '"),'
                         + ' location_Cat=("' + str(self.failelines[0][3]) + '"),' + ' location_faculty="' + str(
            self.failelines[0][4]) + '"where location_ID=' + str(
            self.failelines[0][0]))
        self.failelines.pop(0)
        self.fai.pop(0)

        self.base.commit()
        self.rep.destroy()
        if (bool(self.failelines)):
            self.updatedppro()

    def replacealls(self):
        i = 0

        for values in self.failelines:
            self.cur.execute('update sales set invoice=(' + str(self.failelines[i][1]) + '),'
                             + ' Product_id=(' + str(self.failelines[i][2]) + '),'
                             + ' Quantity=(' + str(self.failelines[i][3]) + '),' + ' Date="' + str(
                self.failelines[i][4]) + '",'
                             + ' Time=("' + str(self.failelines[i][5]) + '"), users="' + str(
                self.failelines[i][6]) + '",priority="' + str(self.failelines[i][7]) + '"   where Trans_id=' + str(
                self.failelines[i][0]))

            i = i + 1

        messagebox.showinfo('success', 'db updated')
        self.base.commit()
        self.rep.destroy()

    def replaceall(self):
        i = 0

        for values in self.failelines:
            self.cur.execute('update products set product_name=("' + str(self.failelines[i][1]) + '"),'
                             + ' product_desc=("' + str(self.failelines[i][2]) + '"),'
                             + ' product_cat=("' + str(self.failelines[i][3]) + '"),' + ' product_price=' + str(
                self.failelines[i][4]) + ','
                             + ' stocks=' + str(self.failelines[i][5]) + ' where productid=' + str(
                self.failelines[i][0]))

            i = i + 1

        messagebox.showinfo('success', 'db updated')
        self.base.commit()
        self.rep.destroy()

    def replacealla(self):
        i = 0

        for values in self.failelines:
            self.cur.execute('update allocation set locationname=("' + str(self.failelines[i][3]) + '"),'
                             + ' productname=("' + str(self.failelines[i][4]) + '"),'
                             + ' quantity=("' + str(self.failelines[i][5]) + '"),' + ' where location_id=' + str(
                self.failelines[i][0]) + 'and product_id=' + str(self.failelines[i][1]) + 'and date="' + +str(
                self.failelines[i][2]) + '"')

            i = i + 1

        messagebox.showinfo('success', 'db updated')
        self.base.commit()
        self.rep.destroy()

    def replacealll(self):
        i = 0

        for values in self.failelines:
            self.cur.execute('update location set location_name=("' + str(self.failelines[i][1]) + '"),'
                             + ' location_Desc=("' + str(self.failelines[i][2]) + '"),'
                             + ' location_Cat=("' + str(self.failelines[i][3]) + '"),' + ' location_faculty="' + str(
                self.failelines[i][4]) + 'where Trans_id=' + str(
                self.failelines[i][0]))

            i = i + 1

        messagebox.showinfo('success', 'db updated')
        self.base.commit()
        self.rep.destroy()

    def skip1(self):

        self.failelines.pop(0)
        self.fai.pop(0)

        self.rep.destroy()
        if (bool(self.failelines)):
            self.updatedppro()

    def skipall(self):

        for values in self.failelines:
            self.failelines.pop(0)
            self.fai.pop(0)


        self.rep.destroy()
    def popschedulea(self):
        self.pointer2=0
        self.popschedule()
    def popschedule(self):
        self.sch = ttkbootstrap.Toplevel(bg="#000000")
        self.sch.title('schedule ')
        self.sch.geometry('1200x800-300-0')

        frame=ttkbootstrap.Frame(self.sch, width=800, height=120, bootstyle="dark")
        frame.grid(column=0, row=0)

        self.frame2 = ttkbootstrap.Frame(self.sch,width=1200, height=800,bootstyle="info")
        self.frame2.grid(column=0, row=1)
        self.frame2.grid_propagate(True)
        frame1 = Frame(frame)


        ttkbootstrap.Frame(frame,width=800, height=0,bootstyle="dark").grid(column=0, row=4,columnspan=4)
        frame1.grid(column=5, row=1, padx=5, pady=5, sticky='w')
        ttkbootstrap.Label(frame, text='schedule', font="roboto 20 bold", bootstyle="inverse-dark").grid(column=0, row=0,columnspan=8)
        if (self.pointer2 == 0):
         self.a3 = spin()
         self.a3.spinframe(frame1)
         ttkbootstrap.Label(frame, text='set date:', font="roboto 14 bold", bootstyle="inverse-dark").grid(column=4, row=1, sticky='e')
         ttkbootstrap.Button(frame, text="set", command=self.buildsch).grid(column=7, row=1, padx=5, pady=5, sticky='e')

         date = datetime(year=self.a3.SelectedYear.get(),
                         month=self.a3.Month_Names.index(self.a3.SelectedMonthName.get()),
                         day=self.a3.SelectedDay.get())
         self.date = date
        elif(self.pointer2==1):
         self.buildschp()
        else :
            self.buildschl()



        self.cur.execute("select product_name from products")
        li = self.cur.fetchall()
        a = []
        i=0

        for v in li:
            a.append(li[i][0])
            i+=1
    def buildschp(self):
        cur = self.tree.selection()
        cur = self.tree.item(cur)
        li2 = cur['values']

        self.cur.execute("select max(date) from allocation")
        li1 = self.cur.fetchall()
        max=li1[0][0]
        self.cur.execute("select min(date) from allocation")
        li1 = self.cur.fetchall()
        min = li1[0][0]
        per1 = pd.date_range(start=min,
                             end=max, freq='1D')

        self.cur.execute("select location_name,location_id from location")
        li = self.cur.fetchall()

        b= []
        i = 0

        b.append('date')

        for v in li:
            b.append(li[i][0])
            i += 1
        b=tuple(b)
        print(b)
        scrollbarx = ttkbootstrap.Scrollbar(self.frame2, orient=HORIZONTAL, bootstyle='secondary')
        scrollbary = ttkbootstrap.Scrollbar(self.frame2, orient=VERTICAL, bootstyle='secondary')
        tree = ttkbootstrap.Treeview(self.frame2, columns=(b), selectmode="browse", height=45,
                                          yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set,
                                          bootstyle='info')
        tree.grid(row=1, column=1, )

        scrollbary.config(command=tree.yview)
        scrollbarx.grid(row=2, column=1, sticky="we")
        scrollbarx.config(command=tree.xview)
        scrollbary.grid(row=1, column=0, sticky="ns",)
        w=round(1200/len(b))
        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=w)


        i=2
        for v in li:
            print( len(b))
            if i<len(b)/1.2:
             tree.column('#'+str(i), stretch=NO, minwidth=0, width=w)
            else:
                tree.column('#' + str(i), stretch=YES, minwidth=w, width=0)

            tree.heading('#'+str(i), text=v[0], anchor=W)
            i+=1
        i=0
        j=0
        values=()
        for v in per1:
            values = []
            i = 0
            values.append(per1[j])
            for va in li:

               self.cur.execute(
                'select quantity from allocation where product_id=' + str(li2[0])
                     + ' and date=("' + str(v)
                     + '")and location_id='+str(va[1]))
               c=self.cur.fetchall()
               if (c):
                   values.append(c)
               else:
                   values.append('-')
               i+=1
            tree.insert('', 'end', values=(values))
            j+=1

    def buildsch(self):
            date = datetime(year=self.a3.SelectedYear.get(),
                            month=self.a3.Month_Names.index(self.a3.SelectedMonthName.get()),
                            day=self.a3.SelectedDay.get())
            self.date = date
            self.cur.execute("select product_name,productid from products")
            li1 = self.cur.fetchall()
            a = []
            i = 0
            a.append('location')
            for v in li1:
                a.append(li1[i][0])
                i += 1
            a = tuple(a)
            self.cur.execute("select location_name,location_id from location")
            li = self.cur.fetchall()

            b = []
            i = 0
            for v in li:
                b.append(li[i][0])
                i += 1
            b = tuple(b)
            scrollbarx = ttkbootstrap.Scrollbar(self.frame2, orient=HORIZONTAL, bootstyle='secondary')
            scrollbary = ttkbootstrap.Scrollbar(self.frame2, orient=VERTICAL, bootstyle='secondary')
            tree = ttkbootstrap.Treeview(self.frame2, columns=(a), selectmode="browse", height=40,
                                         yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set,
                                         bootstyle='info')
            tree.grid(row=1, column=1)
            w = round(1200 / len(a))

            scrollbary.config(command=tree.yview)
            scrollbarx.grid(row=2, column=1, sticky="we")
            scrollbarx.config(command=tree.xview)
            scrollbary.grid(row=1, column=0, sticky="ns", )
            tree.column('#0', stretch=NO, minwidth=0, width=0)

            i = 1


            for v in a:
                if i < len(a)/1.2:
                    tree.column('#' + str(i), stretch=NO, minwidth=0, width=w)
                else:
                    tree.column('#' + str(i), stretch=YES, minwidth=w, width=0)

                tree.heading('#' + str(i), text=v, anchor=W)
                i += 1
            i = 0
            j = 0
            values = ()
            for v in li:
                values = []
                i = 0
                values.append(v[0])
                for va in li1:

                    self.cur.execute(
                        'select quantity from allocation where product_id=' + str(va[1])
                        + ' and date=("' + str(self.date)
                        + '")and location_id=' + str(v[1]))
                    c = self.cur.fetchall()
                    if (c):
                        values.append(c)
                    else:
                        values.append('-')
                    i += 1
                tree.insert('', 'end', values=(values))
                j += 1

    def buildschl(self):
        cur = self.tree.selection()
        cur = self.tree.item(cur)
        li2 = cur['values']

        self.cur.execute("select max(date) from allocation")
        li1 = self.cur.fetchall()
        max = li1[0][0]
        self.cur.execute("select min(date) from allocation")
        li1 = self.cur.fetchall()
        min = li1[0][0]
        per1 = pd.date_range(start=min,
                             end=max, freq='1D')

        self.cur.execute("select product_name,productid from products")
        li = self.cur.fetchall()
        b = []
        i = 0
        b.append('location')
        for v in li:
            b.append(li[i][0])
            i += 1
        b = tuple(b)
        print(b)
        scrollbarx = ttkbootstrap.Scrollbar(self.frame2, orient=HORIZONTAL, bootstyle='secondary')
        scrollbary = ttkbootstrap.Scrollbar(self.frame2, orient=VERTICAL, bootstyle='secondary')
        tree = ttkbootstrap.Treeview(self.frame2, columns=(b), selectmode="browse", height=40,
                                     yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set,
                                     bootstyle='info')
        tree.grid(row=1, column=1, )

        scrollbary.config(command=tree.yview)
        scrollbarx.grid(row=2, column=1, sticky="we")
        scrollbarx.config(command=tree.xview)
        scrollbary.grid(row=1, column=0, sticky="ns", )
        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=120)
        w = round(1200 / len(b))

        i = 2
        for v in li:
            if i < len(b)/1.2:
                tree.column('#' + str(i), stretch=NO, minwidth=0, width=w)
            else:
                tree.column('#' + str(i), stretch=YES, minwidth=w, width=0)

            tree.heading('#' + str(i), text=v[0], anchor=W)
            i += 1
        i = 0
        j = 0
        values = ()
        for v in per1:
            values = []
            i = 0
            values.append(per1[j])
            for va in li:

                self.cur.execute(
                    'select quantity from allocation where product_id=' + str(va[1])
                    + ' and date=("' + str(v)
                    + '")and location_id=' + str(li2[0]))
                c = self.cur.fetchall()
                if (c):
                    values.append(c)
                else:
                    values.append('-')
                i += 1
            tree.insert('', 'end', values=(values))
            j += 1


