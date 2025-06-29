import argparse
import re
import time 

def main():
    parser = argparse.ArgumentParser(description='Cyber Hygiene and Ethical Hacker Training Toolkits')
    parser.add_argument('--hygiene', action = 'store_true', help='Run the Cyber Hygiene Toolkit. Currently includes a password checker and port scanner.')
    parser.add_argument('--hacker', action = 'store_true', help='Run the Ethical Hacker Training Toolkit. Currently includes a port/network scanner, password cracker, packet sniffer, vulnerability scanner, and hash cracker.')

    args = parser.parse_args()

    # opens hygiene toolkit and allows user to choose tool
    if args.hygiene:
        from scanners import password_checker, hygiene_port_scan
        import hygiene_summary
        tools = {
            'password checker': password_checker.password_check,
            'port scan': hygiene_port_scan.run_scan,
            'summary': hygiene_summary.run_summary
        }

        while True:
            tool = input('Select a tool to run (password checker, port scan, summary): ').strip().lower()
            if tool in tools:
                print(f"Loading {tool} ...")
                time.sleep(3)
                tools[tool]()
                break
            else:
                print("Oops! That's not a valid tool - try again!")
    
    # opens hacker toolkit and allows user to choose tool
    if args.hacker:
        from scanners import network_scan, hacker_port_scan, password_cracker, packet_sniffer, vuln_scanner, hash_cracker 
        tools = {
            'port/network scan': lambda: (network_scan.scan('192.168.1.0/24'), hacker_port_scan.scan_target('192.168.1.1')),
            'password cracker': password_cracker.run,
            'packet sniffer': packet_sniffer.sniff_packets,
            'vulnerability scanner': vuln_scanner.scan_vulns,
            'hash cracker': hash_cracker.crack,
            'summary': lambda: print("Summary placeholder!")
        }

        while True:
            tool = input('Select a tool to run (port/network scan, password cracker, packet sniffer, vulnerability scanner, hash cracker, summary): ').strip().lower()
            if tool in tools:
                print(f"meow! running {tool} :3")
                print("Loading...")
                time.sleep(1)
                #tools[tool]()
                break
            else:
                print("Oops! That's not a valid tool - try again!")


if __name__ == '__main__':
    main()