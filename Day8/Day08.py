import base64

with open("b64.txt") as file_contents:
    contents = file_contents.read()

def decode(text):
    base64_bytes = text.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    return message

counter = 0
while True :
    base64_decode = decode(contents)
    contents = base64_decode
    counter += 1
    if counter == 50:
        print(base64_decode)
        break


