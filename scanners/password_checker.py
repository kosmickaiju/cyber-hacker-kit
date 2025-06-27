import hashlib
import requests

# Creates SHA1 hash of user password
def get_sha1(password):
    return hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

# Fetches pwned/leaked passwords from Have I Been Pwned API
def fetch_pwned_data(prefix):
    url = f'https://api.pwnedpasswords.com/range/{prefix}'
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'API Error: {res.status_code}')
    return res.text

# Sends first 5 characters of hash to check against HIBP
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

# GUI-friendly version
def run(password):
    try:
        count = check_pwned_password(password)
        if count:
            return f"⚠️ This password has been found {count} times in data breaches.\nVisit https://www.cisa.gov/secure-our-world/use-strong-passwords for guidance."
        else:
            return "✅ Good news! This password was not found in any known breaches... yet."
    except Exception as e:
        return f"❌ Error: {e}"