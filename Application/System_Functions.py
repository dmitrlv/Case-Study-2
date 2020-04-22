import psutil
from time import sleep
import matplotlib.pyplot as plt
from drawnow import *

values = []

plt.ion()
cnt=0

def plotValues():
    plt.title('Virtual Memory usage')
    plt.grid(True)
    plt.ylabel('Percentage')
    plt.plot(values, 'g', label='values')
    plt.legend(loc='lower left')


for i in range(0,26):
    values.append(0)
    
while(cnt < 24):
    p = psutil.virtual_memory()
    valueRead = p.percent
    sleep(1.0)
    valueInInt = int(valueRead)
    print(valueInInt)
    values.append(valueInInt)
    values.remove(0)
    drawnow(plotValues)
    cnt+=1

pass