import argparse
import re

def main():
    parser = argparse.ArgumentParser(description='Cyber Hygiene and Ethical Hacker Training Toolkits')
    parser.add_argument('--hygiene', action = 'store_true', help='Run the Cyber Hygiene Toolkit. Currently includes a password checker and port scanner.')
    parser.add_argument('--hacker', action = 'store_true', help='Run the Ethical Hacker Training Toolkit. Currently includes a port/network scanner, password cracker, packet sniffer, vulnerability scanner, and hash cracker.')

    args = parser.parse_args()

    if args.hygiene():
        from scanners import password_checker, hygiene_port_scan
        tool = input('Select a tool to run. Choose from password checker, port scan, or summary: ')
        tool = tool.lower()
        if tool == 'password checker':
            print('meow! this should be the password checker :3')
        elif tool == 'port scan':
            print('meow! this should be the port scanner :3')
        elif tool == 'summary':
            print('meow! this should be the summary :3')
        else:
            print("Oops! That's not a vaid tool - try again!")



