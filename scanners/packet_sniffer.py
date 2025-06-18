from scapy.all import * 

def packet_sniffer(packet): 
    if packet.haslayer(IP): 
        print(f"Source: {packet[IP].src} -> Destination: {packet[IP].dst}") 

if __name__ == "__main__": 
    sniff(prn=packet_sniffer, count=10)