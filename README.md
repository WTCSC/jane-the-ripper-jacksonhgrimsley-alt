[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/d_w3ds2H)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=21466211)
MD5 Wordlist Cracker

A small, easy-to-read Python script that attempts to crack MD5 password hashes by comparing them with entries from a wordlist. It reads a file of target MD5 hashes and a wordlist (one candidate password per line), computes the MD5 for each word, and reports which hashes were matched.

Warning / Ethics: This tool is for learning, recovery of your own passwords, or authorized security testing only. Cracking passwords you do not have permission to test may be illegal. Also note MD5 is cryptographically broken and should not be used for password storage.

Features

Simple and readable implementation using only the Python standard library.

Case-insensitive handling of target hashes (targets are normalized to lowercase).

Prints which hashes were cracked and which failed.

Handles missing files and unexpected exceptions with friendly messages.

Requirements

Python 3.7+ (script uses standard library only — no external dependencies).

Files

crack.py — the script you provided (example name).

hashes.txt — example file containing MD5 hashes (one per line).

wordlist.txt — example wordlist (one candidate password per line).

README.md — this document.

Usage

The script prompts for paths interactively:\

decsion tree

Start
 └─> Prompt: hash file path, wordlist path
      └─> Try open files?
           ├─ If FileNotFound/Error -> Print error & Exit
           └─ If OK:
                ├─ Read hashes -> raw_hashes -> targets (lowercase)
                ├─ Read words -> words
                └─ For each word in words:
                     ├─ compute h = md5(word)
                     └─ For each t in targets:
                          ├─ if t already in cracked -> skip
                          ├─ else if h == t -> cracked[t] = word
                          └─ else -> continue
                └─ After loops:
                     ├─ Print "--- CRACKING STARTED ---"
                     ├─ For each t in targets:
                          ├─ if t in cracked -> print "[+] Cracked: t --> word"
                          ├─ else -> print "[-] FAILED: t" and add to failed list
                     └─ Print summary:
                          ├─ if failed is empty -> "[!] All hashes cracked successfully!"
                          └─ else -> "[!] N hashes failed to crack." + list failed
End
