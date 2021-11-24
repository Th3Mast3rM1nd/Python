import socket
# only 1023 Well-Known Ports 
ip = input("Enter IP Here ")
def port_scanner(port):
    try:
        s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        s.settimeout(4)
        s.connect((ip,int(port)))
        s.settimeout(None)
    except socket.timeout :
        pass
    else:
        s.send(b"")
        respond = s.recv(4096)
        return respond

for i in range(1,1023):
    if port_scanner(i):
        print(f"port {i} is Open")
        print(port_scanner(i))
