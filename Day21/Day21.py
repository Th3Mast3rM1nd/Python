import scapy.all as scapy 
# Network Scanner using scapy 

interface = "en0"
subnet = "192.168.1.0/24"
broadcastMac = "ff:ff:ff:ff:ff:ff"

arp_packet = scapy.Ether(dst=broadcastMac)/scapy.ARP(pdst= subnet)
ans , unans = scapy.srp(arp_packet, timeout=2, iface=interface , inter=0.1)
for send,recv in ans:
        print(recv.sprintf(r"%Ether.src% - %ARP.psrc%"))     




