
import sqlite3
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

import ttkbootstrap

from userlogin import Login
from Admin_menu import *
from User_menu import User

import Addtional_features
import tkinter as tk
from datetime import datetime
from PIL import Image, ImageTk
from io import BytesIO
import requests
import tkinter as tk
from datetime import datetime
from PIL import Image, ImageTk
from io import BytesIO
import requests
import os
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk, THEMES
from ttkwidgets import ScaleEntry
from ttkwidgets.autocomplete import AutocompleteCombobox
from PIL import Image











class Main(Login,Admin,User):

    def __init__(self):

        f = open('C:\\Users\\hp\\PycharmProjects\\pythonProject4\\images\\var', 'r')
        if f.mode == 'r':
            Addtional_features.theme = f.read()
        Login.__init__(self)
        self.loginw.mainloop()
        self.loginw.state('withdraw')
        # LOGIN WINDOW EXITS
        self.mainw = ttkbootstrap.Toplevel(bg="#AAAAAA")
        self.style = ttkbootstrap.Style(Addtional_features.theme)
        print(datetime.now().strftime('%A, %d %B %Y\n'))
        print("LOADING, PLEASE WAIT...\n")
        # CREATE WINDOW - RESIZE FALSE - SIZE - TITLE CARD
        self.mainw.geometry('1900x780')
        self.mainw.state('zoomed')
        # DRAW TOP BLUE BAR - DRAW TITLE - DRAW DATETIME
        self.mainw.title("Inventory")
        self.mainw.resizable(0,0)
        self.mainw.protocol('WM_DELETE_WINDOW', self.__Main_del__)
        self.getdetails()

    # OVERRIDING CLOSE BUTTON && DESTRUCTOR FOR CLASS LOGIN AND MAIN WINDOW


    def hello(self):

        self.edit=ttkbootstrap.Toplevel()
        self.edit.title('Theme Demo')
        self.edit.geometry('400x450')
        self.edit.protocol('WM_DELETE_WINDOW', self.__login_del_)

        style = ttkbootstrap.Style(Addtional_features.theme)

        # label
        label = ttk.Label(self.edit, text='Name:')
        label.grid(column=0, row=0, padx=10, pady=10, sticky='w')
        # entry

        # button
        btn = ttk.Button(self.edit, text='save',command=self.save_theme)
        btn.grid(column=2, row=0, padx=10, pady=10, sticky='w')

        # radio button
        self.selected_theme = tk.StringVar()
        theme_frame = ttk.LabelFrame(self.edit, text='Themes')
        theme_frame.grid(padx=10, pady=10, ipadx=20, ipady=20, sticky='w')


        for theme_name in self.style.theme_names():
            rb = ttk.Radiobutton(
                theme_frame,
                text=theme_name,
                value=theme_name,
                variable=self.selected_theme,
                command=self.change_theme)
            rb.pack(expand=True, fill='both')


    def save_theme(self):
        Addtional_features.change = False
        file1 = open("C:\\Users\\hp\\PycharmProjects\\pythonProject4\\images\\var", "w")
        Addtional_features.theme = self.selected_theme.get()

        str1 = Addtional_features.theme
        file1.truncate(0)
        file1.write(str1)
        file1.close()


    def change_theme(self):
        Addtional_features.change = True
        self.style.theme_use(self.selected_theme.get())


    def __login_del_(self):
        if (Addtional_features.change is True) :
            if messagebox.askyesno("Quit", " save changes?") == True:
                file1 = open("C:\\Users\\hp\\PycharmProjects\\pythonProject4\\images\\var", "w")
                Addtional_features.theme=self.selected_theme.get()

                str1 = Addtional_features.theme
                file1.truncate(0)
                file1.write(str1)
                file1.close()
                self.edit.destroy()

            else:

                self.style.theme_use(Addtional_features.theme)
                self.edit.destroy()
        else:
            print (Addtional_features.change)
            self.edit.destroy()


    def __Main_del__(self):
        if messagebox.askyesno("Quit", " Leave Inventory?") == True:
            self.loginw.quit()
            self.mainw.quit()
            exit(0)
        else:
            pass

    # FETCH USER DETAILS FROM PRODUCTS,USERS AND INVENTORY TABLE
    def getdetails(self):
        self.cur.execute("CREATE TABLE if not exists products(product_id varchar (20),product_name varchar (50) NOT NULL,product_desc varchar (50) NOT NULL,product_cat varchar (50),product_price INTEGER NOT NULL,stocks INTEGER NOT NULL,PRIMARY KEY(product_id));")
        self.cur.execute("CREATE TABLE if not exists sales (Trans_id	INTEGER,invoice INTEGER NOT NULL,Product_id	varchar (20),Quantity INTEGER NOT NULL,Date	varchar (20),Time varchar (20),Users varchar(20),priority varchar(20),PRIMARY KEY(Trans_id));")
        self.cur.execute("select * from products ")
        self.products = self.cur.fetchall()
        capuser = self.username.get()
        capuser = capuser.upper()
        self.cur.execute("select account_type from users where username= ? ", (capuser,))
        l = self.cur.fetchall()
        self.account_type = l[0][0]
        self.buildmain()

    #  ADD WIDGETS TO TOP OF MAIN WINDOW
    def buildmain(self):
        if self.account_type == 'ADMIN':
            super(Admin).__init__()
            self.admin_mainmenu(8,8)


        else:
            super(User).__init__()
            self.user_mainmenu(8,8)
        self.currentuser = Addtional_features.user
        self.logout.config(command=self.__Main_del__)
        self.changeuser.config(command=self.change_user)
        self.topframe=ttkbootstrap.Frame(self.mainw,width=1600,height=120,bootstyle="primary")
        self.topframe.place(x=0,y=0)
        self.lable=ttkbootstrap.Label(self.topframe,text="Inventory System",bootstyle="inverse_primary",anchor="center")
        self.lable.config(font="Roboto 30 bold",anchor="center")
        self.lable.place(x=360,y=30)
        mi = PhotoImage(file="images/myprofile.png")
        mi = mi.subsample(4,4)
        self.myprofile = ttkbootstrap.Label(self.topframe,bootstyle="inverse_primary",text=(self.username.get()).capitalize(),image=mi, compound=TOP)
        self.myprofile.image = mi
        self.myprofile.place(x=1300,y=15)
        self.Labl2 = ttkbootstrap.Label(self.topframe, text=datetime.now().strftime('%A, %d %B %Y'),bootstyle='inverse_primary', font="Roboto 15 ")
        self.Labl2.config(bootstyle="inverse_primary", anchor="w")
        self.Labl2.place(x=30, y=8)
        mi = PhotoImage(file="images/myprofile.png")
        mi = mi.subsample(4, 4)
        self.myprofile = ttk.Label(self.topframe, text=(self.username.get()).capitalize(),bootstyle='inverse_primary', image=mi, compound=TOP)
        self.myprofile.image = mi
        self.myprofile.place(x=1300, y=15)

        self.menubar = Menu(self.mainw)
        # create a pulldown menu, and add it to the menu bar
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Open", command=self.hello)
        self.filemenu.add_command(label="Save", command=self.hello)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.mainw.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        # create more pulldown menus
        self.editmenu = Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label="Cut", command=self.hello)
        self.editmenu.add_command(label="Copy", command=self.hello)
        self.editmenu.add_command(label="Paste", command=self.hello)
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)

        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="About", command=self.hello)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)

        self.mainw.config(menu=self.menubar)


        if self.account_type == 'ADMIN':
            self.adminlabel= ttkbootstrap.Label(self.topframe,text=self.currentuser+"(Admin)",bootstyle='inverse_primary',font="Roboto 10 bold",)
        else:
            self.adminlabel =Label(self.topframe, text=self.currentuser+" User", font="Roboto 10 bold", bg="#4267b2")
        self.box = Canvas(self.mainw, width=400, height=700)
        self.box.place(x=1200, y=160)




        self.threshold_box =ttkbootstrap.Frame(self.box, width=325, height=700, bootstyle="info",padding=(3,3,12,12))
        self.threshold_box.grid(row=1,column=0)
        self.threshold_box.grid_propagate (False)
        self.topframe2 = tk.Canvas(self.mainw, width=400, height=40)
        self.topframe2.place(x=1200, y=120)

        self.Labl3= Label(self.topframe2,text="dashboard",font='Montserrat 12 bold',bg="#4267b2",anchor="center")
        self.Labl3.place(x=100, y=12)





        self.adminlabel.place(x=1300,y=80)



        # DATE TIME LABEL


    # METHODS FOR ITEMS AND CHANGE USER BUTTONS
    def change_user(self):
        if messagebox.askyesno("Alert!", "Do  you want to change user?") == True:
            self.base.commit()
            self.currentuser=''
            self.mainw.destroy()
            self.loginw.destroy()
            Login.__init__(self)
            self.loginw.mainloop()


if __name__ == '__main__':
    b=0
    w = Main()
    w.base.commit()
    w.mainw.mainloop()
