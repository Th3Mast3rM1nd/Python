import socket
# only 1023 Well-Known Ports 
ip = input("Enter IP Here ")
def port_scanner(port):
    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    open_port = s.connect_ex((ip,int(port)))
    s.close()
    return open_port
        
for i in range(1,1023):
    if port_scanner(i) == 0 :
        print(f"port {i} is Open")
