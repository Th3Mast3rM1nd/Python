import socket
import threading

# TCP server 
bind_ip = "192.168.1.120" # ip we want to listn on and port 
bind_port = 1337 

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

s.bind((bind_ip,bind_port)) 
s.listen(7) # start listing on backlog connection of 7 

print(f"Listing on {bind_ip} : {bind_port} ")
# this function to handle the client that will connect to this server 
def handle_client(client_socket):
    request = client_socket.recv(4096)
    print(f"Request Received {request} ")
    client_socket.send(b"ACK")
    client_socket.close()
try :
    while True:
        client , addr = s.accept()
        print(f" Connection Accepted from {addr[0]} , {addr[1]} ")
        client_handler =threading.Thread(target=handle_client,args=(client,)) 
        client_handler.start()
except KeyboardInterrupt:
    print("Program Terminated")
