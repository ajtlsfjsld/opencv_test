## CLIENT ##

import socket
from _thread import *

HOST = '127.0.0.1' # server ip 
PORT = 5000        # Port 


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

def recv_data(client_socket):
    while True:
        data = client_socket.recv(1024)
        print("recive : ", repr(data.decode()))
        
start_new_thread(recv_data, (client_socket,))
print('>> Connect Server')

while True:
    message = input()
    if message == 'x':
        #close_data = message
        break
    
    client_socket.send(message.encode())
    #start_new_thread(recv_data, (client_socket,))
    
client_socket.close()