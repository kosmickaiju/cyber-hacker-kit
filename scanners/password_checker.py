import hashlib
import requests

# creates SHA1 hash of user password.
def get_sha1(password):
    return hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

# fetches pwned/leaked passwords from Have I Been Pwned API
def fetch_pwned_data(prefix):
    url = f'https://api.pwnedpasswords.com/range/{prefix}'
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'API Error: {res.status_code}')
    return res.text

# sends first 5 characters of hash to check against HIBP
def check_pwned_password(password):
    sha1 = get_sha1(password)
    prefix = sha1[:5]
    suffix = sha1[5:]
    data = fetch_pwned_data(prefix)
    hashes = (line.split(':') for line in data.splitlines())
    for h, count in hashes:
        if h == suffix:
            return int(count)
    return 0

# run the password check!
def password_check():
    password = input("Enter your password to see if it's been pwned... ")
    count = check_pwned_password(password)
    if count:
        print(f'Uh oh! This password has been found {count} times in data breaches. Check out this site about good password practices to avoid being pwned again: https://www.cisa.gov/secure-our-world/use-strong-passwords')
    else:
        print(f'Good news! This password was not found in any known breaches... yet.')

