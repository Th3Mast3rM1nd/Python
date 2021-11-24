import socket
# UDP client 
ip = "127.0.0.1"
port = 53

s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
s.sendto(b"testing" , (ip,port))

data , addr = s.recvfrom(4096)

print(data)
