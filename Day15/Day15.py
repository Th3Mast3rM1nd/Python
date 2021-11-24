import socket 
# TCP client 
target_host = "192.168.1.107"
target_port = 22

# AF_INET = ipv4 or hostname
# SOCK_STREAM = TCP Protocol 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connecting to server using ip and port
client.settimeout(10)
client.connect((target_host,target_port))
client.settimeout(None)
# sending data to the target_host 
client.send(b"")
# Recive the data from the server 
response = client.recv(4096)

print(response)


