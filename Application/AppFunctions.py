from tkinter import *
from tkinter.ttk import *
import psutil
from datetime import datetime


def doNothing():
    print("LMAO")

def memoryLogs(self):
    p = psutil.virtual_memory()
    s = "At " + datetime.now().strftime("%Y-%m-%d %H:%M") + " " + str(p.percent) + "% RAM usage"
    self.insert(END, s)
    self.after(60000, lambda:memoryLogs(self))

def diskLogs(self):
    p = str(psutil.disk_usage('C:/'))
    self.insert(END, p)
    self.after(5000, lambda:diskLogs(self))

def netLogs(self):
    p = str(psutil.net_io_counters())
    self.insert(END, p)
    self.after(10000, lambda:netLogs(self))

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