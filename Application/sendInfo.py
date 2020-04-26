import socket, pickle
import psutil
from time import sleep
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.11.10", 1234))

#while(True):
    #msg = s.recv(64)
    #print(msg.decode("utf-8"))
for proc in psutil.process_iter(['pid','name','username']):
    p = str(proc.info) + '\n'
    p =  ''.join(c for c in p if c not in '\'{}')
    #data_string = pickle.dumps(p)
    s.send(bytes(p, "utf-8")) 
    #s.send(data_string)
    #sleep(0.5)