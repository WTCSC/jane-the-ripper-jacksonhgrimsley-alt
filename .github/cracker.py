import hashlib

password = "password123"
hash_object = hashlib.md5(password.encode())
hash_hex = hash_object.hexdigest()

print(hash_hex)
#output:482c811da5d5b4bc6d497ffa98491e38

char_hashes = {
    hashlib.sha256('a'.encode()).hexdigest(): 'a',
    hashlib.sha256('b'.encode()).hexdigest(): 'b',
    hashlib.sha256('c'.encode()).hexdigest(): 'c',
}

word_list_file = "wordlist.txt"


import sys
from typing import Dict, List

def crack_passwords(hash_file_path: str, wordlist_path: str) -> Dict[str, str]:
   
    with open(hash_file_path, "r", encoding="utf-8") as hf:
        raw_hashes = [line.strip() for line in hf if line.strip()]

    with open(wordlist_path, "r", encoding="utf-8") as wf:
        words = [line.strip() for line in wf if line.strip()]

    targets = [h.lower() for h in raw_hashes]

    cracked: Dict[str, str] = {}

    
    for word in words:
        h = hashlib.md5(word.encode("utf-8")).hexdigest()
       
        for t in targets:
            if t not in cracked and h == t:
                cracked[t] = word

    return cracked

def main():
   
    hash_file_path = input("Enter path to hash file: ").strip()
    wordlist_path = input("Enter path to wordlist file: ").strip()

    
    try:
        cracked = crack_passwords(hash_file_path, wordlist_path)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

    
    with open(hash_file_path, "r", encoding="utf-8") as hf:
        targets = [line.strip().lower() for line in hf if line.strip()]

    print("\n--- CRACKING STARTED ---")

    failed = []
    for t in targets:
        if t in cracked:
            print(f"[+] Cracked: {t}  -->  {cracked[t]}")
        else:
            print(f"[-] FAILED: {t}")
            failed.append(t)

    print("--- CRACKING FINISHED ---")

    if not failed:
        
        print("[!] All hashes cracked successfully!")
    else:
        
        print(f"[!] {len(failed)} hashes failed to crack.")
        
        for fh in failed:
            print("  " + fh)

if __name__ == "__main__":
    main()
