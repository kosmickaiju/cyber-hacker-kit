import time
def run_summary():
    from scanners import password_checker, hygiene_port_scan
    
    # run password check
    print(f'✰✰✰✰✰✰ Your Cyber Hygiene Summary ✰✰✰✰✰✰ \n')
    password = input("Enter your password to see if it's been pwned... ")
    count = password_checker.check_pwned_password(password)
    if count:
        print(f'Uh oh! This password has been found {count} times in data breaches.')
    else:
        print(f'Good news! This password was not found in any known breaches... yet.')
    
    #run port scan
    open_ports = hygiene_port_scan.run_scan()
    if open_ports:
        print(f"\n {len(open_ports)} open port(s) found: {open_ports}")
    else:
        print("\n All clear! No open ports found.")
    
    # print personalized suggestions based on scan results
    time.sleep(3)
    if count or open_ports:
        print(f'✰✰✰✰✰✰ Your Personalized Cyber Hygiene Suggestions ✰✰✰✰✰✰ \n')
        if count:
            print(f'Looks like one of your passwords got pwned! Check out this site about good password practices to avoid being pwned again: https://www.cisa.gov/secure-our-world/use-strong-passwords')
        if open_ports:
            print(f'It seems that you have a few ports open on your device. No worries though - these are all essential ports that need to be open to the Internet for you to use your computer. However, make sure that you have a firewall installed and keep your software/operating system updated to avoid potential attacks!')
