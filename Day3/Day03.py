list_of_ips = []
ip = "192.168.1."

for i in range(1,256):
    valid_ip = f"{ip}{i}"
    list_of_ips.append(valid_ip)
    for j in list_of_ips:
        print(j)



