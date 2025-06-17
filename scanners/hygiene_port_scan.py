from tqdm import tqdm
import socket

def scan_port(port):
   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.settimeout(0.5)
      result = s.connect_ex(('127.0.0.1', port)) 
      return result == 0
   
# running the actual scan of each port from 20 to 1024
def run_scan(start = 20, end = 1024):
   print(f'Scanning ports {start} - {end} on localhost...')
   open_ports = []
   for port in tqdm(range(start, end + 1), desc = 'Scanning', unit = 'port'):
      if scan_port(port):
         open_ports.append(port)
   if open_ports:
      print('Open ports found: ')
      for port in open_ports:
         print(f'- Port {port}')
   else:
      print(f'All clear! No open ports found.')
   return open_ports
