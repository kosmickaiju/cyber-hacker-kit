import socket 
import network_scan
import re

def scan_port(target, port): 
    try: 
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        sock.settimeout(1) 
        result = sock.connect_ex((target, port)) 
        if result == 0:
            print(f"Found open port(s): {port}")
            sock.close()
    except socket.error: print(f"Oops! Couldn't connect to {target}.") 

def scan_target(target):
    print(f"Scanning target {target}...") 
    open_ports = []
    for port in range(1, 1025): 
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
            sock.settimeout(1) 
            result = sock.connect_ex((target, port)) 
            if result == 0:
                open_ports.append(port)
                print(f"Found open port(s): {port}")
            sock.close()
        except socket.error:
            print(f"Oops! Couldn't connect to {target}.") 

    if not open_ports:
        print("No open ports found on ports 1–1024.")

if __name__ == "__main__": 
    while True:
        target_ip = input("Enter target IP (IPv4 format) or CIDR range (e.g 192.168.1.0/24): ") 
        pattern = r"^\d{1,3}(\.\d{1,3}){3}$"
        if re.fullmatch(pattern, target_ip):
            scan_target(target_ip)
        elif "/" in target_ip:
            network_scan.scan(target_ip)
        else:
            print(f'Not a valid IPv4 address. Try again!')
    