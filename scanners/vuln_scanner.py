import socket, requests

def run(target):
    output = f"Scanning {target} for vulnerabilities...\n\n"
    open_ports = [80, 443, 22] 

    for port in open_ports:
        try:
            sock = socket.socket()
            sock.settimeout(1)
            sock.connect((target, port))
            sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
            banner = sock.recv(1024).decode(errors="ignore")
            sock.close()

            output += f"[{port}] Banner: {banner.strip()}\n"
            # query CVEs based on banner
            service_name = extract_service_name(banner)  # need to write this
            vulns = query_cve_api(service_name) # need to write this
            for v in vulns:
                output += f"  - {v['id']} ({v['severity']}) {v['url']}\n"

        except Exception as e:
            output += f"[{port}] No response or error: {e}\n"

    return output