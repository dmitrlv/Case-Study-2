import socket, pickle
import psutil

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 1234))
    s.listen(5)

    conn, address = s.accept()
    msg = "START\n" 

    while len(msg) > 0:
    
    #print(f"address: {address} and clientsocket: {clientsocket}")
    #clientsocket.send(bytes("blahblah2!", "utf-8"))
        msg = conn.recv(4096)
    #data_variable = pickle.loads(msg)
        with open(".\\user1Proc.txt", "a") as myfile:
            myfile.write(msg.decode("utf-8"))
            myfile.write("\n")