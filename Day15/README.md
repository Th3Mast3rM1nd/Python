# Day 15 

* ***Socket Module***
```python
socket.socket() # Creates a Socket Object  
``` 
```python
socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket.socket(socket.family , socket.type )
# socket.AF_INET >> IPV4 or Hostname ( www.google.com ..... ) 
# socket.SOCK_STREAM(tcp)
# socket.SOCK_DGRAM(udp)
```

* ***Server Socket Methods***

```python
s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.bind((ip,port)) # This method binds address (hostname, port number pair) to socket. 
s.listen(6) # This method sets up and start TCP listener. 
s.accept() # This passively accept TCP client connection 

```
* ***Client Socket Methods***
```python 
s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.connect((ip,port)) # connect the client to the server 
```
* ***General Socket Methods***

```python 
s.send() # send tcp data to the server 
s.recv() # recevives tcp data from the server
s.close() # close the socket 
s.sendto() # send udp data to the server 
s.recvfrom() # receives  udp data 
```
