from tkinter import *
from tkinter.ttk import *
import psutil
from datetime import datetime


def doNothing():
    print("LMAO")

def cpuLogs(self):
    p = str(psutil.cpu_percent())
    self.insert(END, p)
    self.after(5000, lambda:cpuLogs(self))
    with open("C:\\Users\\dmitr\\Downloads\\cpuLogs.txt", "a") as myfile:
        myfile.write(p)
        myfile.write('\n')


def memoryLogs(self):
    p = psutil.virtual_memory()
    s = "At " + datetime.now().strftime("%Y-%m-%d %H:%M") + " " + str(p.percent) + "% RAM usage"
    self.insert(END, s)
    self.after(5000, lambda:memoryLogs(self))
    with open("C:\\Users\\dmitr\\Downloads\\memoryLogs.txt", "a") as myfile:
        myfile.write(s)
        myfile.write('\n')

def diskLogs(self):
    p = str(psutil.disk_usage('C:/'))
    self.insert(END, p)
    self.after(5000, lambda:diskLogs(self))
    with open("C:\\Users\\dmitr\\Downloads\\diskLogs.txt", "a") as myfile:
        myfile.write(p)
        myfile.write('\n')

def netLogs(self):
    p = str(psutil.net_io_counters())
    self.insert(END, p)
    self.after(5000, lambda:netLogs(self))
    with open("C:\\Users\\dmitr\\Downloads\\netLogs.txt", "a") as myfile:
        myfile.write(p)
        myfile.write('\n')

def procLogs(self):
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        p = str(proc.info)
        self.insert(END, p)
        self.after(50000, lambda:procLogs(self))

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