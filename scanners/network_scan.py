import requests
from scapy.all import *

def scan(target_ip): 
    arp_request = ARP(pdst=target_ip) 
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff") 
    arp_request_broadcast = broadcast/arp_request 
    answered_list = srp(arp_request_broadcast, timeout=1, verbose=False)[0] 

    print("Available Devices:") 
    print("IP\t\t\tMAC Address\n----------------------------------") 
    for element in answered_list: 
        print(f"{element[1].psrc}\t\t{element[1].hwsrc}") 

if __name__ == "__main__": 
    target = input("Enter target IP or IP range (e.g., 192.168.1.0/24): ") 
    scan(target)