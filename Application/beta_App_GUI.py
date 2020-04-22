from tkinter import *
from tkinter.ttk import *
from tkinter import font as tkFont
import psutil
import AppFunctions as func


root = Tk()

mainMenu = Menu(root)
root.geometry("900x600")



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
mainFrame.place(x=200, y=150)

labelStatus = Label(mainFrame, text="Status: Running")
labelStatus.config(font=("Calibri", 20))
labelCPU = Label(mainFrame, text="CPU Usage: 15%")
labelCPU.config(font=("Calibri", 20))
labelMemory = Label(mainFrame, text="Memory Usage: 15%")
labelMemory.config(font=("Calibri", 20))
labelSpace = Label(mainFrame, text="Diskspace: 4Gb/50Gb")
labelSpace.config(font=("Calibri", 20))
labelUsers = Label(mainFrame, text="Users connected: 4")
labelUsers.config(font=("Calibri", 20))
# labelStatus.place(x=250, y=100)
# labelCPU.place(x=250, y=120)
# labelMemory.place(x=250, y=140)
# labelSpace.place(x=250, y=160)
# labelUsers.place(x=250, y=180)
labelStatus.pack(anchor=E)
labelCPU.pack(anchor=E)
labelMemory.pack(anchor=E)
labelSpace.pack(anchor=E)
labelUsers.pack(anchor=E)

page2 = Frame(nb)
nb.add(page2, text='Real-Time Statistics')

page3 = Frame(nb)
nb.add(page3, text='Logs')

listboxFrame1 = Frame(page3)
labelCPU = Label(listboxFrame1, text="CPU")
labelCPU.pack()
listboxFrame1.place(x=100, y=50)
listboxLogs1 = Listbox(listboxFrame1, width=40)
listboxLogs1.pack()

listboxFrame2 = Frame(page3)
labelMemory = Label(listboxFrame2, text="Memory")
labelMemory.pack()
listboxFrame2.place(x=550, y=50)
listboxLogs2 = Listbox(listboxFrame2, width=40)
listboxLogs2.pack()

listboxFrame3 = Frame(page3)
labelDisk = Label(listboxFrame3, text="Disk")
labelDisk.pack()
listboxFrame3.place(x=100, y=300)
listboxLogs3 = Listbox(listboxFrame3, width=40)
listboxLogs3.pack()

listboxFrame4 = Frame(page3)
labelNetwork = Label(listboxFrame4, text="Network")
labelNetwork.pack()
listboxFrame4.place(x=550, y=300)
listboxLogs4 = Listbox(listboxFrame4, width=40)
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
buttonApplication1 = Button(frameUser1, text="Opened Applications", command=func.createNewWindow1)
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
buttonApplication2 = Button(frameUser2, text="Opened Applications", command=func.createNewWindow2)
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
buttonApplication3 = Button(frameUser3, text="Opened Applications", command=func.createNewWindow3)
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
buttonApplication4 = Button(frameUser4, text="Opened Applications", command=func.createNewWindow4)
#labelApplication4.config(font=("Calibri", 20))
buttonApplication4.pack()

func.memoryLogs()
root.mainloop()