import hashlib

target_hash = input("Enter the hash: ")
wordlist_path = input("Enter path to wordlist: ")

with open(wordlist_path, 'r') as file:
    for line in file:
        word = line.strip()
        hashed = hashlib.md5(word.encode()).hexdigest()
        if hashed == target_hash:
            print(f"[+] Match found: {word}")
            break
    else:
        print("[-] No match found.")