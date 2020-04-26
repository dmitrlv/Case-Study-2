from tkinter import *
from tkinter.ttk import *
from tkinter import font as tkFont
import psutil
import AppFunctions as func
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
from matplotlib import pyplot as plt

style.use("ggplot")



f = Figure(figsize=(4.5,2), dpi=100)
k = Figure(figsize=(4.5,2), dpi=100)
l = Figure(figsize=(4.5,2), dpi=100)
m = Figure(figsize=(4.5,2), dpi=100)

a = f.add_subplot(111)
f.suptitle("CPU Usage")
b = k.add_subplot(111)
k.suptitle("Memory Usage")
c = l.add_subplot(111)
l.suptitle("Disk Usage")
d = m.add_subplot(111)
m.suptitle("Network Usage")

values1 = []
values2 = []
values3_1 = []
values3_2 = []
values4_1 = []
values4_2 = []


for i in range(0,25):
    values1.append(0)
    values2.append(0)
    values3_1.append(0)
    values3_2.append(0)
    values4_1.append(0)
    values4_2.append(0)

def animate(i):
    global values1
    global values2
    global values3_1
    global values3_2
    global values4_1
    global values4_2
    # global bytesSentPrev
    # global bytesRecPrev
    # global bytesSentDelta
    # global bytesRecDelta
    global s1
    global s2
    pullData1 = str(psutil.cpu_percent())
    p = psutil.virtual_memory()
    pullData2 = str(p.percent)
    y = psutil.disk_io_counters(perdisk=False, nowrap=True)
    pullData3_1 = str(y.read_time)
    pullData3_2 = str(y.write_time)
    # c = psutil.net_io_counters()
    # bytesSentNow = c.bytes_sent
    # bytesRecNow = c.bytes_recv
    animate_for_bytes()
    values1.append(float(pullData1))
    values2.append(float(pullData2))
    values3_1.append(int(pullData3_1))
    values3_2.append(int(pullData3_2))
    values4_1.append(float(s1))
    values4_2.append(float(s2))
    del values1[0]
    del values2[0]
    del values3_1[0]
    del values3_2[0]
    del values4_1[0]
    del values4_2[0]

    a.clear()
    b.clear()
    c.clear()
    d.clear()
    a.plot(values1)
    b.plot(values2)
    c.plot(values3_1)
    c.plot(values3_2)
    d.plot(values4_1)
    d.plot(values4_2)
    a.set_ylim([0,100])
    b.set_ylim([0,100])
    #c.set_ylim([0,100])

def animate_for_bytes():
    global s1
    global s2
    global bytesSentPrev
    global bytesRecPrev
    p = psutil.net_io_counters()
    bytesSentNow = p.bytes_sent
    bytesRecNow = p.bytes_recv
    try:
        bytesSentDelta = bytesSentNow - bytesSentPrev
        bytesRecDelta = bytesRecNow - bytesRecPrev
        s1 = round(bytesSentDelta/1000000, 1)
        s2 = round(bytesRecDelta/1000000, 1)
    except NameError:
        bytesSentDelta = bytesSentNow
        bytesRecDelta = bytesRecNow
        s1 = round(bytesSentDelta/1000000, 1)
        s2 = round(bytesRecDelta/1000000, 1)
    bytesSentPrev = bytesSentNow
    bytesRecPrev = bytesRecNow

root = Tk()

mainMenu = Menu(root)
root.geometry("900x600")
root.title("Server application")



#Calibri = tkFont.Font(family='Calibri', size=20, weight=tkFont.BOLD)

rows = 0
while rows < 50:
    root.rowconfigure(rows, weight=1)
    root.columnconfigure(rows, weight=1)
    rows += 1

root.config(menu=mainMenu)

helpMenu = Menu(mainMenu)
mainMenu.add_cascade(label="Help", menu = helpMenu)
helpMenu.add_command(label="About", command=func.doNothing)
helpMenu.add_command(label="Manual", command=func.doNothing)

tabsMenu = Menu(mainMenu)
mainMenu.add_cascade(label="Tabs", menu = tabsMenu)
tabsMenu.add_command(label="tab1", command=func.doNothing)
tabsMenu.add_command(label="tab2", command=func.doNothing)
tabsMenu.add_command(label="tab3", command=func.doNothing)
tabsMenu.add_command(label="tab4", command=func.doNothing)

nb = Notebook(root)
nb.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NSEW')

page1 = Frame(nb)
nb.add(page1, text='Main')

mainFrame = Frame(page1)
mainFrame.place(x=0, y=0)

cpuTxtVar = StringVar()
memoryTxtVar = StringVar()
diskTxtVar = StringVar()
UsersTxtVar = StringVar()

labelStatus = Label(mainFrame, text="Status: Running")
labelStatus.config(font=("Calibri", 20))
labelCPU = Label(mainFrame)
func.updateCPUlabel(labelCPU)
labelCPU.config(font=("Calibri", 20))
labelMemory = Label(mainFrame)
func.updateMemorylabel(labelMemory)
labelMemory.config(font=("Calibri", 20))
labelSpace = Label(mainFrame)
func.updateSpacelabel(labelSpace)
labelSpace.config(font=("Calibri", 20))
labelStatus.pack(anchor=W)
labelCPU.pack(anchor=W)
labelMemory.pack(anchor=W)
labelSpace.pack(anchor=W)



page2 = Frame(nb)
nb.add(page2, text='Real-Time Statistics')

graphFrame1 = Frame(page2)
graphFrame1.place(x=0, y=50)
canvas1 = FigureCanvasTkAgg(f, graphFrame1)
canvas1.draw()
canvas1.get_tk_widget().pack(side=TOP, fill=BOTH, expand=TRUE)

graphFrame2 = Frame(page2)
graphFrame2.place(x=450, y=50)
canvas2 = FigureCanvasTkAgg(k, graphFrame2)
canvas2.draw()
canvas2.get_tk_widget().pack(side=TOP, fill=BOTH, expand=TRUE)

graphFrame3 = Frame(page2)
graphFrame3.place(x=0, y=300)
canvas3 = FigureCanvasTkAgg(l, graphFrame3)
canvas3.draw()
canvas3.get_tk_widget().pack(side=TOP, fill=BOTH, expand=TRUE)

graphFrame2 = Frame(page2)
graphFrame2.place(x=450, y=300)
canvas2 = FigureCanvasTkAgg(m, graphFrame2)
canvas2.draw()
canvas2.get_tk_widget().pack(side=TOP, fill=BOTH, expand=TRUE)

page3 = Frame(nb)
nb.add(page3, text='Logs')

listboxFrame1 = Frame(page3)
labelCPU = Label(listboxFrame1, text="CPU")
labelCPU.pack()
listboxFrame1.place(x=100, y=50)
listboxLogs1 = Listbox(listboxFrame1, width=40)
scrollbar_x1 = Scrollbar(listboxFrame1, orient=HORIZONTAL)
listboxLogs1.config(xscrollcommand=scrollbar_x1.set)
scrollbar_x1.config(command=listboxLogs1.xview)
scrollbar_x1.pack(side=BOTTOM, fill=X)
scrollbar_y1 = Scrollbar(listboxFrame1)
listboxLogs1.config(yscrollcommand=scrollbar_y1.set)
scrollbar_y1.config(command=listboxLogs1.yview)
scrollbar_y1.pack(side=RIGHT, fill=Y)
listboxLogs1.pack()

listboxFrame2 = Frame(page3)
labelMemory = Label(listboxFrame2, text="Memory")
labelMemory.pack()
listboxFrame2.place(x=550, y=50)
listboxLogs2 = Listbox(listboxFrame2, width=40)
scrollbar_x2 = Scrollbar(listboxFrame2, orient=HORIZONTAL)
listboxLogs2.config(xscrollcommand=scrollbar_x2.set)
scrollbar_x2.config(command=listboxLogs2.xview)
scrollbar_x2.pack(side=BOTTOM, fill=X)
scrollbar_y2 = Scrollbar(listboxFrame2)
listboxLogs2.config(yscrollcommand=scrollbar_y2.set)
scrollbar_y2.config(command=listboxLogs2.yview)
scrollbar_y2.pack(side=RIGHT, fill=Y)
listboxLogs2.pack()


listboxFrame3 = Frame(page3)
labelDisk = Label(listboxFrame3, text="Disk")
labelDisk.pack()
listboxFrame3.place(x=100, y=300)
listboxLogs3 = Listbox(listboxFrame3, width=40)
scrollbar_x3 = Scrollbar(listboxFrame3, orient=HORIZONTAL)
listboxLogs3.config(xscrollcommand=scrollbar_x3.set)
scrollbar_x3.config(command=listboxLogs3.xview)
scrollbar_x3.pack(side=BOTTOM, fill=X)
scrollbar_y3 = Scrollbar(listboxFrame3)
listboxLogs3.config(yscrollcommand=scrollbar_y3.set)
scrollbar_y3.config(command=listboxLogs3.yview)
scrollbar_y3.pack(side=RIGHT, fill=Y)
checkButtonCPUVar = IntVar()
checkButtonRAMVar = IntVar()
checkButtonDiskVar = IntVar()
checkButtonNetworkVar = IntVar()
checkButtonCPULogs = Checkbutton(page3, text="Disable CPU logs formatting (more information)", variable=checkButtonCPUVar)
checkButtonRAMLogs = Checkbutton(page3, text="Disable RAM logs formatting (more information)", variable=checkButtonRAMVar)
checkButtonDiskLogs = Checkbutton(page3, text="Disable Disk logs formatting (more information)", variable=checkButtonDiskVar)
checkButtonNetworkLogs = Checkbutton(page3, text="Disable Network logs formatting (more information)", variable=checkButtonNetworkVar)
checkButtonCPULogs.place(x=100, y=250)
checkButtonRAMLogs.place(x=550, y=250)
checkButtonDiskLogs.place(x=100, y=500)
checkButtonNetworkLogs.place(x=550, y=500)
listboxLogs3.pack()

listboxFrame4 = Frame(page3)
labelNetwork = Label(listboxFrame4, text="Network")
labelNetwork.pack()
listboxFrame4.place(x=550, y=300)
listboxLogs4 = Listbox(listboxFrame4, width=40)
scrollbar_x4 = Scrollbar(listboxFrame4, orient=HORIZONTAL)
listboxLogs4.config(xscrollcommand=scrollbar_x4.set)
scrollbar_x4.config(command=listboxLogs4.xview)
scrollbar_x4.pack(side=BOTTOM, fill=X)
scrollbar_y4 = Scrollbar(listboxFrame4)
listboxLogs4.config(yscrollcommand=scrollbar_y4.set)
scrollbar_y4.config(command=listboxLogs4.yview)
scrollbar_y4.pack(side=RIGHT, fill=Y)
listboxLogs4.pack()

page4 = Frame(nb)
nb.add(page4, text='Users')

frameUser1 = Frame(page4)
frameUser1.place(x=100, y=50)
labelUser1 = Label(frameUser1, text="user1")
labelUser1.config(font=("Calibri", 25))
labelUser1.pack()
labelUptime1 = Label(frameUser1, text="Uptime: 3:00:00")
labelUptime1.config(font=("Calibri", 20))
labelUptime1.pack()
labelStatus1 = Label(frameUser1, text="Status: Active")
labelStatus1.config(font=("Calibri", 20))
labelStatus1.pack()
buttonApplication1 = Button(frameUser1, text="Opened Applications", command = lambda:func.createNewWindow1(root))
buttonApplication1.pack()

frameUser2 = Frame(page4)
frameUser2.place(x=600, y=50)
labelUser2 = Label(frameUser2, text="user2")
labelUser2.config(font=("Calibri", 25))
labelUser2.pack()
labelUptime2 = Label(frameUser2, text="Uptime: 3:00:00")
labelUptime2.config(font=("Calibri", 20))
labelUptime2.pack()
labelStatus2 = Label(frameUser2, text="Status: Active")
labelStatus2.config(font=("Calibri", 20))
labelStatus2.pack()
buttonApplication2 = Button(frameUser2, text="Opened Applications", command= lambda:func.createNewWindow2(root))
buttonApplication2.pack()

frameUser3 = Frame(page4)
frameUser3.place(x=100, y=300)
labelUser3 = Label(frameUser3, text="user3")
labelUser3.config(font=("Calibri", 25))
labelUser3.pack()
labelUptime3 = Label(frameUser3, text="Uptime: 3:00:00")
labelUptime3.config(font=("Calibri", 20))
labelUptime3.pack()
labelStatus3 = Label(frameUser3, text="Status: Active")
labelStatus3.config(font=("Calibri", 20))
labelStatus3.pack()
buttonApplication3 = Button(frameUser3, text="Opened Applications", command= lambda:func.createNewWindow3(root))
buttonApplication3.pack()

frameUser4 = Frame(page4)
frameUser4.place(x=600, y=300)
labelUser4 = Label(frameUser4, text="user4")
labelUser4.config(font=("Calibri", 25))
labelUser4.pack()
labelUptime4 = Label(frameUser4, text="Uptime: 3:00:00")
labelUptime4.config(font=("Calibri", 20))
labelUptime4.pack()
labelStatus4 = Label(frameUser4, text="Status: Active")
labelStatus4.config(font=("Calibri", 20))
labelStatus4.pack()
buttonApplication4 = Button(frameUser4, text="Opened Applications", command= lambda:func.createNewWindow4(root))
#labelApplication4.config(font=("Calibri", 20))
buttonApplication4.pack()

page5 = Frame(nb)
nb.add(page5, text='Processes')

listboxFrame5 = Frame(page5)
listboxFrame5.pack(fill=X)
listboxLogs5 = Listbox(listboxFrame5, height=60)
scrollbar_x5 = Scrollbar(listboxFrame5, orient=HORIZONTAL)
listboxLogs5.config(xscrollcommand=scrollbar_x5.set)
scrollbar_x5.config(command=listboxLogs5.xview)
scrollbar_x5.pack(side=BOTTOM, fill=X)
scrollbar_y5 = Scrollbar(listboxFrame5)
listboxLogs5.config(yscrollcommand=scrollbar_y5.set)
scrollbar_y5.config(command=listboxLogs5.yview)
scrollbar_y5.pack(side=RIGHT, fill=Y)
listboxLogs5.pack(fill=X)




func.cpuLogs(listboxLogs1, checkButtonCPUVar)
func.memoryLogs(listboxLogs2, checkButtonRAMVar)
func.diskLogs(listboxLogs3, checkButtonDiskVar)
func.netLogs(listboxLogs4, checkButtonNetworkVar)
func.procLogs(listboxLogs5)


ani1 = animation.FuncAnimation(f, animate, interval=1000)
ani2 = animation.FuncAnimation(k, animate, interval=1000)
ani3 = animation.FuncAnimation(l, animate, interval=1000)
ani4 = animation.FuncAnimation(m, animate, interval=1000)

root.mainloop()