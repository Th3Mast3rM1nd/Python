hosts = {
    "host_1" : {"ip" : "192.168.1.1",
              "ports" : [22,23,80],
             },
    "host_2" : {"ip" : "192.168.1.110",
              "ports": [8080,22,443],}
,}

for key,value in hosts.items():
    for k,v in value.items():
        if k == "ip":
            print(f" This Host has IP : {v} ")
        else:
            for port in v:
                print(f" open port : {port}")



