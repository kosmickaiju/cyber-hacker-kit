import socket
import sys
from datetime import datetime

#scan a single port
def scan_port(host, port, timeout=0.5):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((host, port))
            return result == 0
    except socket.error:
        return False

#common service names for port numbers
def get_service_name(port):
    common_ports = {
        21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
        80: "HTTP", 110: "POP3", 143: "IMAP", 443: "HTTPS", 993: "IMAPS",
        995: "POP3S", 587: "SMTP", 465: "SMTPS", 3389: "RDP", 5432: "PostgreSQL",
        3306: "MySQL", 1433: "MSSQL", 6379: "Redis", 27017: "MongoDB"
    }
    return common_ports.get(port, "Unknown")

#scanning function
def run(start_port=20, end_port=1024, host='127.0.0.1'):
    output = f"🔍 Cyber Hygiene Port Scan\n"
    output += f"{'='*40}\n"
    output += f"Target: {host} (localhost)\n"
    output += f"Port range: {start_port}-{end_port}\n"
    output += f"Scan started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    output += f"{'='*40}\n\n"
    
    print(f"Scanning {end_port - start_port + 1} ports on {host}...")
    
    open_ports = []
    scanned = 0
    total_ports = end_port - start_port + 1
    
    for port in range(start_port, end_port + 1):
        scanned += 1
        if scanned % 100 == 0:
            print(f"Progress: {scanned}/{total_ports} ports scanned...")
            
        if scan_port(host, port):
            open_ports.append(port)
            service = get_service_name(port)
            output += f"🔓 Port {port:5d} - {service:12s} - OPEN\n"
            print(f"Found open port: {port} ({service})")
    
    output += f"\n{'='*40}\n"
    output += f"Scan completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    
    if open_ports:
        output += f"\n📊 Summary: {len(open_ports)} open port(s) found\n"
        output += f"Open ports: {', '.join(map(str, open_ports))}\n\n"
        
        output += f"🛡️  Security Assessment:\n"
        if len(open_ports) <= 3:
            output += f"✅ Low risk: Few ports open, which is normal for most systems.\n"
        elif len(open_ports) <= 10:
            output += f"⚠️  Medium risk: Several ports open. Review if all services are necessary.\n"
        else:
            output += f"🚨 High risk: Many ports open. Consider closing unnecessary services.\n"
            
        output += f"\n💡 Recommendations:\n"
        output += f"   • Ensure you have a firewall enabled\n"
        output += f"   • Keep all software and OS updated\n"
        output += f"   • Close any unnecessary services\n"
        output += f"   • Use strong authentication for all services\n"
    else:
        output += f"\n✅ Excellent! No open ports found in the scanned range.\n"
        output += f"This indicates good security hygiene.\n"
    
    return output

#simplified version for backwards compatibility
def run_scan():
    open_ports = []
    for port in range(20, 1025):
        if scan_port('127.0.0.1', port):
            open_ports.append(port)
    return open_ports