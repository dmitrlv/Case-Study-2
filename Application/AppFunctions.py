from tkinter import *
from tkinter.ttk import *
import psutil
from datetime import datetime



def doNothing():
    print("LMAO")

def cpuLogs(self):
    p = str(psutil.cpu_percent())
    s = "At " + datetime.now().strftime("%Y-%m-%d %H:%M") + " " + p + "% CPU usage\n"
    self.insert(END, s)
    self.after(5000, lambda:cpuLogs(self))
    with open(".\\cpuLogs.txt", "a") as myfile:
        myfile.write(s)


def memoryLogs(self):
    p = psutil.virtual_memory()
    s = "At " + datetime.now().strftime("%Y-%m-%d %H:%M") + " " + str(p.percent) + "% RAM usage\n"
    self.insert(END, s)
    self.after(5000, lambda:memoryLogs(self))
    with open(".\\memoryLogs.txt", "a") as myfile:
        myfile.write(s)

def diskLogs(self):
    p = psutil.disk_io_counters(perdisk=False, nowrap=True)
    s = "At " + datetime.now().strftime("%Y-%m-%d %H:%M") + " Read time was: " + str(p.read_time) + "ms and write time was: " + str(p.write_time) +"ms.\n"
    self.insert(END, s)
    self.after(5000, lambda:diskLogs(self))
    with open(".\\diskLogs.txt", "a") as myfile:
        myfile.write(s)

def netLogs(self):
    global bytesSentPrev
    global bytesRecPrev
    p = psutil.net_io_counters()
    bytesSentNow = p.bytes_sent
    bytesRecNow = p.bytes_recv
    try:
        bytesSentDelta = bytesSentNow - bytesSentPrev
        bytesRecDelta = bytesRecNow - bytesRecPrev
        s = "At " + datetime.now().strftime("%Y-%m-%d %H:%M") + " MB sent delta: " + str(round(bytesSentDelta/1000000, 1)) + ". MB received delta: " + str(round(bytesRecDelta/1000000, 1))
    except NameError:
        bytesSentDelta = bytesSentNow
        bytesRecDelta = bytesRecNow
        s = "MB sent from the start of the server: " + str(round(bytesSentDelta/1000000, 1)) + ". MB received from the start of the server: " + str(round(bytesRecDelta/1000000, 1))
    bytesSentPrev = bytesSentNow
    bytesRecPrev = bytesRecNow
    self.insert(END, s)
    self.after(5000, lambda:netLogs(self))
    with open(".\\netLogs.txt", "a") as myfile:
        myfile.write(s)
        myfile.write('\n')

def procLogs(self):
    self.delete(0,END)
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        p = str(proc.info)
        self.insert(END, p)
    self.after(10000, lambda:procLogs(self))

def updateCPUlabel(self):
    p = str(psutil.cpu_percent())
    c = "CPU Load: " + p
    self.config(text=c)
    self.after(1000, lambda:updateCPUlabel(self))

def updateMemorylabel(self):
    p = psutil.virtual_memory()
    c = "Memory Load: " + str(p.percent)
    self.config(text=c)
    self.after(1000, lambda:updateMemorylabel(self))

def updateSpacelabel(self):
    p = psutil.disk_usage('/')
    c = "Disk Usage: " + str(p.percent)
    self.config(text=c)
    self.after(1000, lambda:updateSpacelabel(self))
        
def checkBoxLogTab(self):
    pass

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