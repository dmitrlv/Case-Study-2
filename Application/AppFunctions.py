from tkinter import *
from tkinter.ttk import *
import psutil


def doNothing():
    print("LMAO")

def memoryLogs(self):
    p = psutil.virtual_memory()
    self.insert(END, p.percent)
    self.after(1000, lambda:memoryLogs(self))

def createNewWindow1(self):
    newWindow1 = Toplevel(self)
    pass

def createNewWindow2(self):
    newWindow2 = Toplevel(self)
    pass

def createNewWindow3(self):
    newWindow3 = Toplevel(self)
    pass

def createNewWindow4(self):
    newWindow4 = Toplevel(self)
    pass