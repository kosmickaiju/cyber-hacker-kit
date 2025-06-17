import socket 
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
    for port in range(1, 1025): 
        scan_port(target, port)

if __name__ == "__main__": 
    target_ip = input("Enter target IP (IPv4 format): ") 
    pattern = r"^\d{1,3}(\.\d{1,3}){3}$"
    if re.fullmatch(pattern, target_ip):
        scan_target(target_ip)
    else:
        print(f'Not a valid IPv4 address. Try again!')
    