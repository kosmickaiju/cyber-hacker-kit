import socket

def scan_port(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.5)
        result = s.connect_ex(('127.0.0.1', port)) 
        return result == 0

def run(start=20, end=1024):
    output = f"Scanning ports {start}–{end} on localhost...\n"
    open_ports = []

    for port in range(start, end + 1):
        if scan_port(port):
            open_ports.append(port)
            output += f"✓ Port {port} is open\n"

    if open_ports:
        output += "\nOpen ports found:\n"
        output += "\n".join([f"- Port {port}" for port in open_ports])
    else:
        output += "\n✅ All clear! No open ports found."

    return output