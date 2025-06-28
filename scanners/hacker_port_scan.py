import socket
import re
from . import network_scan  # assuming this exists and also has a GUI-friendly run()

def scan_target(target):
    output = f"Scanning target {target}...\n"
    open_ports = []

    for port in range(1, 1025):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
                output += f"✓ Open port: {port}\n"
            sock.close()
        except socket.error:
            output += f"Could not connect to {target}.\n"

    if not open_ports:
        output += "No open ports found on ports 1–1024.\n"

    return output

# GUI-friendly main function
def run(target_ip):
    pattern = r"^\d{1,3}(\.\d{1,3}){3}$"
    if re.fullmatch(pattern, target_ip):
        return scan_target(target_ip)
    elif "/" in target_ip:
        return network_scan.run(target_ip)
    else:
        return "Invalid IPv4 address. Please try again."