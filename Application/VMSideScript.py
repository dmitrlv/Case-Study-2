import psutil
from time import sleep
import socket


def getCPUStats():
    cpuPerc = psutil.cpu_percent()
    return cpuPerc

def getRAMStats():
    return psutil.virtual_memory()

def getDiskStats():
    return psutil.disk_io_counters(perdisk=False, nowrap=True)

def getNetStats():
    return psutil.net_io_counters()

while True:
    getCPUStats()
    getRAMStats()
    getDiskStats()
    getNetStats()
    sleep(1.0)