import tkinter
import tkinter.ttk
from tkinter import filedialog as fd, messagebox, filedialog
from tkinter import *
import numpy
import pandas as pd
from collections import defaultdict
from datetime import datetime as dt

import ttkbootstrap
import xlrd
from tkinter  import *
from tkinter  import ttk
from datetime import datetime
from collections import OrderedDict

global SelectedMonthLength

user=''
theme=''
change=False



tkinter_umlauts=['odiaeresis', 'adiaeresis', 'udiaeresis', 'Odiaeresis', 'Adiaeresis', 'Udiaeresis', 'ssharp']
class myentry(tkinter.Entry):
        def set_completion_list(self, completion_list):
                self._completion_list = sorted(completion_list, key=str.lower)
                self._hits = []
                self._hit_index = 0
                self.position = 0
                self.bind('<KeyRelease>', self.handle_keyrelease)

        def autocomplete(self, delta=0):
                if delta:
                        self.delete(self.position, tkinter.END)
                else:
                        self.position = len(self.get())
                _hits = []
                for element in self._completion_list:
                        if element.lower().startswith(self.get().lower()):
                                _hits.append(element)
                if _hits != self._hits:
                        self._hit_index = 0
                        self._hits=_hits
                if _hits == self._hits and self._hits:
                        self._hit_index = (self._hit_index + delta) % len(self._hits)
                if self._hits:
                        self.delete(0,tkinter.END)
                        self.insert(0,self._hits[self._hit_index])
                        self.select_range(self.position,tkinter.END)

        def handle_keyrelease(self, event):
                if event.keysym == "BackSpace":
                        self.delete(self.index(tkinter.INSERT), tkinter.END)
                        self.position = self.index(tkinter.END)
                if event.keysym == "Left":
                        if self.position < self.index(tkinter.END):
                                self.delete(self.position, tkinter.END)
                        else:
                                self.position = self.position-1
                                self.delete(self.position, tkinter.END)
                if event.keysym == "Right":
                        self.position = self.index(tkinter.END)
                if event.keysym == "Down":
                        self.autocomplete(1)
                if event.keysym == "Up":
                        self.autocomplete(-1)
                if len(event.keysym) == 1 or event.keysym in tkinter_umlauts:
                        self.autocomplete()



class  mycombobox(tkinter.ttk.Combobox):

        def set_completion_list(self, completion_list):
                self._completion_list = sorted(completion_list)
                self._hits = []
                self._hit_index = 0
                self.position = 0
                self.bind('<KeyRelease>', self.handle_keyrelease)
                self['values'] = self._completion_list

        def autocomplete(self, delta=0):
                if delta:
                        self.delete(self.position, tkinter.END)
                else:
                        self.position = len(self.get())
                _hits = []
                for element in self._completion_list:
                        if element.lower().startswith(self.get().lower()): # Match case insensitively
                                _hits.append(element)
                if _hits != self._hits:
                        self._hit_index = 0
                        self._hits=_hits
                if _hits == self._hits and self._hits:
                        self._hit_index = (self._hit_index + delta) % len(self._hits)
                if self._hits:
                        self.delete(0,tkinter.END)
                        self.insert(0,self._hits[self._hit_index])
                        self.select_range(self.position,tkinter.END)

        def handle_keyrelease(self, event):
                if event.keysym == "BackSpace":
                        self.delete(self.index(tkinter.INSERT), tkinter.END)
                        self.position = self.index(tkinter.END)
                if event.keysym == "Left":
                        if self.position < self.index(tkinter.END):
                                self.delete(self.position, tkinter.END)
                        else:
                                self.position = self.position-1
                                self.delete(self.position, tkinter.END)
                if event.keysym == "Right":
                        self.position = self.index(tkinter.END)
                if len(event.keysym) == 1:
                        self.autocomplete()
# TEST THIS
def test(test_list):
        root = tkinter.Tk(className=' AutocompleteEntry demo')
        entry = myentry(root)
        entry.set_completion_list(test_list)
        entry.pack()
        entry.focus_set()
        combo = mycombobox(root)
        combo.set_completion_list(test_list)
        combo.pack()
        combo.focus_set()
        root.bind('<Control-Q>', lambda event=None: root.destroy())
        root.bind('<Control-q>', lambda event=None: root.destroy())
        root.mainloop()
def treeview_sort_column(tv, col, reverse):
    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    l.sort(reverse=reverse)

    # rearrange items in sorted positions
    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)

    # reverse sort next time
    tv.heading(col, text=col, command=lambda _col=col: \
                 treeview_sort_column(tv, _col, not reverse))
def importexele (tree,col):

        filename = fd.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("xlxs files", ".*xlsx"),("all files","*.*")))
        if filename:
                try:
                        filename = r"{}".format(filename)
                        df = pd.read_excel(filename,
     engine='openpyxl',)

                except ValueError:
                        messagebox.showinfo("error", "File could not be opened")
                        messagebox.showinfo("error", "File could not be opened")
                except FileNotFoundError:
                        messagebox.showinfo("error", "File Not Found")
        tree.delete(*tree.get_children())


        df_rows = df.to_numpy().tolist()
  
        for row in df_rows:

                tree.insert("", "end", values=row)
def exportexele(tree, monthToExport=None):
        file = filedialog.asksaveasfilename(title="Select file",  defaultextension = "nameOfFile.xlsx",
                                            filetypes=[("Excel file", "*.xlsx")])
        if file:

                dict = defaultdict(list)
                ids = tree.get_children()
                dict = defaultdict(list)
                for id in ids:
                        for i in range(0, len(tree['column'])):



                                dict[""+str(i)].append(tree.item(id)["values"][i])

                dict = pd.DataFrame.from_dict(dict)

                dict.to_excel(file, engine='xlsxwriter', index=False)

        else:

                print("You did not save the file")
class spin(tkinter.Frame):
 def spinframe(self,mainframe):
         # put here so IntVar (etc.) is useable during initialization
        style = ttkbootstrap.Style(theme)

        StartUpDateTime = datetime.now()
        DefaultYear = StartUpDateTime.year
        DefaultMonthNumber = StartUpDateTime.month
        DefaultDayOfMonth = StartUpDateTime.day

        # These are only used to build the Month name & length dictionary  
        YearAndMonthLengths = [365, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        EnglishMonthNames = ('Entire Year', 'January', 'February', 'March',
                             'April', 'May', 'June', 'July', 'August', 'September',
                             'October', 'November', 'December')

        # ItalianMonthNames = ....


        self.Month_Names  = EnglishMonthNames  # comment out this line to use French

        # Create dictionary containing month names that appear in the Month spinbox.
        # OrderedDict used because Month name (=key) field must be language-independent.

        DaysInMonth = OrderedDict()
        for i in range(0, len(self.Month_Names )):
                DaysInMonth[self.Month_Names [i]] = YearAndMonthLengths[i]

        DefaultMonthName = self.Month_Names [DefaultMonthNumber]
        DefaultMonthLength = DaysInMonth[DefaultMonthName]
        # Initialize the Spinbox interface variables to todays date
        self.SelectedYear = IntVar(value=DefaultYear)
        self.SelectedMonthName = StringVar(value=DefaultMonthName)
        SelectedMonthLength = IntVar(value=DefaultMonthLength)
        self.SelectedDay = IntVar(value=DefaultDayOfMonth)

        # -------------------------------------------------------------------------------

        def GetChosenMonthLength(*args):
                SelectedMonthLength.set(DaysInMonth[self.SelectedMonthName.get()])
                return

        def update_days():
                 maxdays = int(DaysInMonth[self.SelectedMonthName.get()])
                 DaySpinBox.config(to=maxdays)



         # -------------------------------------------------------------------------------


        # Show today's date.  If it's July 17th, 2023 the spinboxes must be initialized
        # to "July" ("julliet" if using French), "17" and "2023".
        YearSpinBox = ttkbootstrap.Spinbox(mainframe,
                              from_=2000, to=2050,
                              textvariable=self.SelectedYear,
                              wrap=TRUE, state='readonly', width=6)
        MonthSpinBox = ttkbootstrap.Spinbox(mainframe,
                               values=tuple(DaysInMonth.keys())[1:],
                               textvariable=self.SelectedMonthName,
                               wrap=TRUE, state='readonly', width=7,command=update_days)
        DaySpinBox = ttkbootstrap.Spinbox(mainframe,
                             from_=1,
                             to=SelectedMonthLength.get(),
                             #                       to = DaysInMonth[ SelectedMonthName.get() ],
                             #                       values = tuple( str( i ) for i in range( 1, SelectedMonthLength.get() + 1 ) ),
                             #                       values = lambda : tuple( str( i ) for i in range( 1, DaysInMonth[ SelectedMonthName.get() ] + 1 ) )
                             textvariable=self.SelectedDay,
                             wrap=TRUE, state='readonly', width=10
                             )
        MonthSpinBox.grid(row=0, column=0)
        DaySpinBox.grid(row=0, column=1)
        YearSpinBox.grid(row=0, column=2)


        self.SelectedMonthName.trace('w', GetChosenMonthLength)

        







        


