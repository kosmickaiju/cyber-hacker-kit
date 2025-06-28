from scapy.all import ARP, Ether, srp
from . import hacker_port_scan

def run(target_ip):
    if '/' not in target_ip:
        return hacker_port_scan.run(target_ip)

    arp_request = ARP(pdst=target_ip) 
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff") 
    arp_request_broadcast = broadcast / arp_request 
    answered_list = srp(arp_request_broadcast, timeout=1, verbose=False)[0] 

    output = "Available Devices:\n"
    output += "IP\t\t\tMAC Address\n----------------------------------\n"
    for element in answered_list:
        output += f"{element[1].psrc}\t\t{element[1].hwsrc}\n"

    if not answered_list:
        output += "No devices found.\n"

    return output