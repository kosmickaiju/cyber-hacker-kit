import argparse
import re
import time 

def main():
    parser = argparse.ArgumentParser(description='Cyber Hygiene and Ethical Hacker Training Toolkits')
    parser.add_argument('--hygiene', action = 'store_true', help='Run the Cyber Hygiene Toolkit. Currently includes a password checker and port scanner.')
    parser.add_argument('--hacker', action = 'store_true', help='Run the Ethical Hacker Training Toolkit. Currently includes a port/network scanner, password cracker, packet sniffer, vulnerability scanner, and hash cracker.')

    args = parser.parse_args()

    if args.hygiene:
        from scanners import password_checker, hygiene_port_scan
        tools = ['password checker', 'port scan', 'summary']
        tool = input('Select a tool to run. Choose from password checker, port scan, or summary: ')
        tool = tool.lower()
        if tool == tools[0]:
            print('meow! this should be the password checker :3')
            print('Loading', tools[0], '...')
            time.sleep(3)
            print(':p')
        elif tool == tools[1]:
            print('meow! this should be the port scanner :3')
            print('Loading', tools[1], '...')
        elif tool == tools[len(tools) - 1]:
            print('meow! this should be the summary :3')
            print('Loading', tools[len(tools) - 1], '...')
        else:
            print("Oops! That's not a valid tool - try again!")
    
    if args.hacker:
        from scanners import password_checker, hygiene_port_scan
        tools = ['port/network scan', 'password cracker', 'packer sniffer', 'vulnerability scanner', 'hash cracker', 'summary']
        tool = input('Select a tool to run. Choose from password checker, port scan, or summary: ')
        tool = tool.lower()
        for i in tools:
            if tool == tools[i]:
                print('meow! this is in the list :3')
            else:
                print("Oops! That's not a valid tool - try again!")


if __name__ == '__main__':
    main()