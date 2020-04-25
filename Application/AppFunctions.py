from tkinter import *
from tkinter.ttk import *
import psutil
from datetime import datetime



def doNothing():
    print("LMAO")

def cpuLogs(self, checkButtonCPUVar):
    if checkButtonCPUVar.get() == 0:
        p = str(psutil.cpu_percent())
        s = "At " + datetime.now().strftime("%Y-%m-%d %H:%M") + " " + p + "% CPU usage\n"
        s = "At " + datetime.now().strftime("%Y-%m-%d %H:%M") + " " + p + "% CPU usage"
    elif checkButtonCPUVar.get() == 1:
        s = str(psutil.cpu_times(percpu=False))
        s = str(psutil.cpu_times(percpu=False)) + " CPU usage %" + str(psutil.cpu_percent())
    self.insert(END, s)
    self.after(5000, lambda:cpuLogs(self, checkButtonCPUVar))
    with open(".\\cpuLogs.txt", "a") as myfile:
        myfile.write(s)
        myfile.write("\n")



def memoryLogs(self, checkButtonRAMVar):
    if checkButtonRAMVar.get() == 0:
        p = psutil.virtual_memory()
        s = "At " + datetime.now().strftime("%Y-%m-%d %H:%M") + " " + str(p.percent) + "% RAM usage\n"
        s = "At " + datetime.now().strftime("%Y-%m-%d %H:%M") + " " + str(p.percent) + "% RAM usage"
    elif checkButtonRAMVar.get() == 1:
        s = str(psutil.virtual_memory())
    self.insert(END, s)
    self.after(5000, lambda:memoryLogs(self, checkButtonRAMVar))
    with open(".\\memoryLogs.txt", "a") as myfile:
        myfile.write(s)
        myfile.write("\n")


def diskLogs(self, checkButtonDiskVar):
    if checkButtonDiskVar.get() == 0:
        p = psutil.disk_io_counters(perdisk=False, nowrap=True)
        s = "At " + datetime.now().strftime("%Y-%m-%d %H:%M") + " Read time was: " + str(p.read_time) + "ms and write time was: " + str(p.write_time) +"ms.\n"
        s = "At " + datetime.now().strftime("%Y-%m-%d %H:%M") + " Read time was: " + str(p.read_time) + "ms and write time was: " + str(p.write_time) +"ms."
    elif checkButtonDiskVar.get() == 1:
        s = str(psutil.disk_io_counters(perdisk=False, nowrap=True))
    self.insert(END, s)
    self.after(5000, lambda:diskLogs(self, checkButtonDiskVar))
    with open(".\\diskLogs.txt", "a") as myfile:
        myfile.write(s)
        myfile.write("\n")


def netLogs(self, checkButtonNetworkVar):
    global bytesSentPrev
    global bytesRecPrev
    if checkButtonNetworkVar.get() == 0:
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
    elif checkButtonNetworkVar.get() == 1:
        s = str(psutil.net_io_counters())
    self.insert(END, s)
    self.after(5000, lambda:netLogs(self, checkButtonNetworkVar))
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
    c = "CPU Load: {}%".format(p)
    self.config(text=c)
    self.after(1000, lambda:updateCPUlabel(self))

def updateMemorylabel(self):
    perc = str(psutil.virtual_memory().percent)
    totalMem = str(round(psutil.virtual_memory().total/1000000000, 0))
    usedMem = str(round(psutil.virtual_memory().used/1000000000, 1))
    c = "Memory Load: {}% {}GB/{}GB".format(perc, usedMem, totalMem)
    self.config(text=c)
    self.after(1000, lambda:updateMemorylabel(self))

def updateSpacelabel(self):
    totalDisk = str(round(psutil.disk_usage('/').total/1000000000, 0))
    usedDisk = str(round(psutil.disk_usage('/').used/1000000000, 1))
    c = "Disk Usage: {}GB/{}GB".format(usedDisk, totalDisk)
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