from tkinter import *
class ValueContainedCheckButton(Checkbutton):
    def __init__(self,master,**cnf):
        super().__init__(master, cnf)
        self.val = IntVar()
        self.configure(variable=self.val)
    __value = False
    def switchValue(self):
        self.__value = not self.__value
        
    def getValue(self):
        return self.__value #bool(self.val.get())    
    