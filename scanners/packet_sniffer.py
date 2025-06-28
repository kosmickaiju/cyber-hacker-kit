from scapy.all import sniff, IP

def run():
    output = "Sniffing network packets...\n\n"
    def packet_handler(packet):
        nonlocal output
        if packet.haslayer(IP):
            output += f"Source: {packet[IP].src} -> Destination: {packet[IP].dst}\n"
    sniff(filter="ip", prn=packet_handler, count=10, timeout=5)
    if output.strip() == "Sniffing network packets...":
        output += "No packets captured.\n"

    return output