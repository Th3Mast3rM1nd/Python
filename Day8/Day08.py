import base64

file = open("./b64.txt" , "r")

def decode(text):
    base64_bytes = text.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    return message

read_file  = file.readline()
counter = 0
while True :
    base64_decode = decode(read_file)
    read_file = base64_decode
    counter += 1
    if counter == 50:
        print(base64_decode)
        break


