def slicing_ip(ip):
    ip_list = []
    ip_string = ""
    ip.append(".")
    for x in ip:
        if x == ".":
            ip_list.append(int(ip_string))
            ip_string = ""
        else:
            ip_string = ip_string + x 
    return ip_list
def ip_to_binary(ip):
    binary_list = []
    final_ip = ""
    zero = "0"
    for i in ip:
        x = bin(i).replace("0b", "")
        if len(x) == 8 :
            binary_list.append(x)
            binary_list.append(".")
        elif len(x) < 8:
            y = 8 - len(x)
            zero = "0" * y 
            binary_list.append(f"{zero}{x}")
            binary_list.append(".")
    binary_list.pop()
    for binary in binary_list:
        final_ip += binary

    return final_ip
        
        

ip = list(input("Enter your Ip Here "))
result = slicing_ip(ip)
bin_ip = ip_to_binary(result)
print(f"{bin_ip}")
