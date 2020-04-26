from tkinter import *
from tkinter.ttk import *
import psutil
from datetime import datetime
import sqlite3
import databaseMaker as dbMaker
import socket
import os
#import ServerReceive as serv

dateNow = str(datetime.now().strftime("%Y-%m-%d %H:%M"))

def doNothing():
    pass
    
def usersConnect():
    pass
    #serv.connect()

def cpuLogs(self, checkButtonCPUVar):
    if checkButtonCPUVar.get() == 0:
        p = str(psutil.cpu_percent())
        s = "At " + dateNow + " " + p + "% CPU usage"
    elif checkButtonCPUVar.get() == 1:
        s = str(psutil.cpu_stats()) + " CPU usage %" + str(psutil.cpu_percent())
    self.insert(END, s)
    dbMaker.c.execute("""CREATE TABLE IF NOT EXISTS 'cpu'(
        date text,
        ctx_switches int,
        interrupts int,
        soft_interrupts int,
        syscalls int,
        percentage float
    );
    """)
    self.after(5000, lambda:(cpuLogs(self, checkButtonCPUVar), dbMaker.insertCPUinfoDB()))
    with open(".\\cpuLogs.txt", "a") as myfile:
        myfile.write(s)
        myfile.write("\n")


def memoryLogs(self, checkButtonRAMVar):
    if checkButtonRAMVar.get() == 0:
        p = psutil.virtual_memory()
        s = "At " + dateNow + " " + str(p.percent) + "% RAM usage"
    elif checkButtonRAMVar.get() == 1:
        s = str(psutil.virtual_memory())
    self.insert(END, s)
    dbMaker.c.execute("""CREATE TABLE IF NOT EXISTS 'ram'(
        date text,
        total int,
        available int,
        used int,
        free int,
        percentage float
    );
    """)
    self.after(5000, lambda:(memoryLogs(self, checkButtonRAMVar), dbMaker.insertMemoryInfoDB()))
    with open(".\\memoryLogs.txt", "a") as myfile:
        myfile.write(s)
        myfile.write("\n")


def diskLogs(self, checkButtonDiskVar):
    if checkButtonDiskVar.get() == 0:
        p = psutil.disk_io_counters(perdisk=False, nowrap=True)
        s = "At " + dateNow + " Read time was: " + str(p.read_time) + "ms and write time was: " + str(p.write_time) +"ms."
    elif checkButtonDiskVar.get() == 1:
        s = str(psutil.disk_io_counters(perdisk=False, nowrap=True))
    self.insert(END, s)
    dbMaker.c.execute("""CREATE TABLE IF NOT EXISTS 'diskio'(
        date text,
        read_count int,
        write_count int,
        read_bytes int,
        write_bytes int,
        read_time int,
        write_time int
    );
    """)
    self.after(5000, lambda:(diskLogs(self, checkButtonDiskVar), dbMaker.insertDiskInfoDB()))
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
            s = "At " + dateNow + " MB sent delta: " + str(round(bytesSentDelta/1000000, 1)) + ". MB received delta: " + str(round(bytesRecDelta/1000000, 1))
        except NameError:
            bytesSentDelta = bytesSentNow
            bytesRecDelta = bytesRecNow
            s = "MB sent from the start of the server: " + str(round(bytesSentDelta/1000000, 1)) + ". MB received from the start of the server: " + str(round(bytesRecDelta/1000000, 1))
        bytesSentPrev = bytesSentNow
        bytesRecPrev = bytesRecNow
    elif checkButtonNetworkVar.get() == 1:
        s = str(psutil.net_io_counters())
    self.insert(END, s)
    dbMaker.c.execute("""CREATE TABLE IF NOT EXISTS 'networkio'(
        date text,
        bytes_sent int,
        bytes_recv int,
        packets_sent int,
        packets_recv int,
        errin int,
        errout int,
        dropin int,
        dropout int
    );
    """)
    self.after(5000, lambda:(netLogs(self, checkButtonNetworkVar), dbMaker.insertNetInfoDB()))
    with open(".\\netLogs.txt", "a") as myfile:
        myfile.write(s)
        myfile.write('\n')


def procLogs(self):
    self.delete(0,END)
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        p = str(proc.info)
        p = ''.join(c for c in p if c not in '\'{}') #strips string from characters '{}
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
    global s
    global conn 
    global msg
    newWindow1 = Toplevel(self)
    newWindow1.geometry("900x600")
    listboxUserProcesses1 = Listbox(newWindow1, height=60)
    listboxUserProcesses1.pack(fill=X)
    # usersConnect()
    #while len(msg) > 0:
    #    msg = conn.recv(4096)
    #    listboxUserProcesses1.insert(END, msg.decode("utf-8"))
    with open("user1Proc.txt", "r") as rf:
        while(True):
            chunkToRead = rf.read(1)
            stringToListbox = ''
            while chunkToRead != '\n' and chunkToRead != '':
                stringToListbox = stringToListbox + chunkToRead
                chunkToRead = rf.read(1)
            listboxUserProcesses1.insert(END, stringToListbox)
            if chunkToRead == '':
                break

def createNewWindow2(self):
    newWindow2 = Toplevel(self)
    newWindow2.geometry("900x600")
    listboxUserProcesses2 = Listbox(newWindow2, height=60)
    listboxUserProcesses2.pack(fill=X)

def createNewWindow3(self):
    newWindow3 = Toplevel(self)
    newWindow3.geometry("900x600")
    listboxUserProcesses3 = Listbox(newWindow3, height=60)
    listboxUserProcesses3.pack(fill=X)

def createNewWindow4(self):
    newWindow4 = Toplevel(self)
    newWindow4.geometry("900x600")
    listboxUserProcesses4 = Listbox(newWindow4, height=60)
    listboxUserProcesses4.pack(fill=X)

