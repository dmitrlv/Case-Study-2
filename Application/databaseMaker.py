import sqlite3
from datetime import datetime
import psutil


dateNow = str(datetime.now().strftime("%Y-%m-%d %H:%M"))

db = sqlite3.connect("appDB.db")
c = db.cursor()

def insertCPUinfoDB():
    perc = float(psutil.cpu_percent(interval=1))
    ctx_switches = int(psutil.cpu_stats().ctx_switches)
    interrupts = int(psutil.cpu_stats().interrupts)
    soft_interrupts = int(psutil.cpu_stats().ctx_switches)
    syscalls = int(psutil.cpu_stats().syscalls)
    with db:
        c.execute("INSERT INTO cpu VALUES (?, ?, ?, ?, ?, ?);", (dateNow, ctx_switches, interrupts, soft_interrupts, syscalls, perc))

def insertMemoryInfoDB():
    total = int(psutil.virtual_memory().total)
    available = int(psutil.virtual_memory().available)
    used = int(psutil.virtual_memory().used)
    free = int(psutil.virtual_memory().free)
    perc = float(psutil.virtual_memory().percent)
    with db:
        c.execute("INSERT INTO ram VALUES (?, ?, ?, ?, ?, ?);", (dateNow, total, available, used, free, perc))

def insertDiskInfoDB():
    read_count = int(psutil.disk_io_counters(perdisk=False, nowrap=True).read_count)
    write_count = int(psutil.disk_io_counters(perdisk=False, nowrap=True).write_count)
    read_bytes = int(psutil.disk_io_counters(perdisk=False, nowrap=True).read_bytes)
    write_bytes = int(psutil.disk_io_counters(perdisk=False, nowrap=True).write_bytes)
    read_time = int(psutil.disk_io_counters(perdisk=False, nowrap=True).read_time)
    write_time =int(psutil.disk_io_counters(perdisk=False, nowrap=True).write_time)
    with db:
        c.execute("INSERT INTO diskio VALUES (?, ?, ?, ?, ?, ?, ?);", (dateNow, read_count, write_count, read_bytes, write_bytes, read_time, write_time))

def insertNetInfoDB():
    bytes_sent = int(psutil.net_io_counters(pernic=False, nowrap=True).bytes_sent)
    bytes_recv = int(psutil.net_io_counters(pernic=False, nowrap=True).bytes_recv)
    packets_sent = int(psutil.net_io_counters(pernic=False, nowrap=True).packets_sent)
    packets_recv = int(psutil.net_io_counters(pernic=False, nowrap=True).packets_recv)
    errin = int(psutil.net_io_counters(pernic=False, nowrap=True).errin)
    errout = int(psutil.net_io_counters(pernic=False, nowrap=True).errout)
    dropin = int(psutil.net_io_counters(pernic=False, nowrap=True).dropin)
    dropout = int(psutil.net_io_counters(pernic=False, nowrap=True).dropout)
    with db:
        c.execute("INSERT INTO networkio VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);", (dateNow, bytes_sent, bytes_recv, packets_sent, packets_recv, errin, errout, dropin, dropout))