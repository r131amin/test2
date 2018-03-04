from tkinter import *
from Choose_Win_from_OptionList_3 import *
#from functools import partial #used to pass variables in the command option

class Choose_Win:
  
    def __init__(self):


        self.r=Tk()
        frame = Frame(self.r)
        frame.pack()

        self.r.title("In the name of ALLH")

        optionList = ['Emp', 'Department']
        self.choosedWin = StringVar(master=self.r)
        #self.choosedlevel.set(optionList[0])
        om = OptionMenu(self.r, self.choosedWin, *optionList)
        om.pack()

        a=Open_Window()
        
        Button(self.r, text='Go',
               #command=partial(a.display_Form, choosen) #pass some values
            command= lambda: a.display_Form(self.choosedWin.get())
               ,cursor="boat",justify=CENTER).pack()
        """
        Python will call the callback function before creating the widget, and pass the function’s return value to Tkinter. Tkinter then attempts to convert the return value to a string, and tells Tk to call a function with that name when the button is activated. This is probably not what you wanted.
        For simple cases like this, you can use a lambda expression as a link between Tkinter and the callback function:
        """
        self.r.mainloop()
##    def quit(self):
##        self.r.quit()

a=Choose_Win()
