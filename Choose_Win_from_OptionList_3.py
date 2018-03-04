from tkinter import *
from Emp_Window import *

class Open_Window:
    def display_Form(self,choosenform):
        root = Tk()
        root.title(choosenform+" Window ")
        labelframe = LabelFrame(root, text=choosenform+" Data ")
        labelframe.pack(fill="both", expand="yes")

        if choosenform=='Emp':
            emp=Emp_Window(root, labelframe)
        


##o=Open_Window()
##o.display_Form("EMP")
