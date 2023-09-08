# Password Cracking Workshop
Password cracking workshop for kompetensdag 2023-09-08

## Requirements
Download and install `hashcat` [https://hashcat.net/hashcat/](https://hashcat.net/hashcat/)

### Resources
Here is a list of resources from the presentation:

* https://crackstation.net/ 
* https://github.com/dwyl/english-words
* https://github.com/almgru/svenska-ord.txt
* https://github.com/danielmiessler/SecLists
* https://github.com/hashcat/hashcat/tree/master/rules 
* https://hashcat.net/wiki/doku.php?id=mask_attack 
* https://github.com/hashcat/kwprocessor
* https://github.com/digininja/CeWL

## Challenge
There are 10000 MD5 hashes in the file `hashes.txt` 

Crack as many hashes as possible

The cracked passwords will be stored in `hashcat.potfile` 

MacOS: `/opt/homebrew/Cellar/hashcat/6.2.6_1/share/hashcat/hashcat.potfile`

Good luck!

## Sample commands

Dictionary attack
```bash
hashcat -m 0 -a 0 hashes.txt svenska-ord.txt
```

Dictionary attack with rules
```bash
hashcat -m 0 -a 0 hashes.txt svenska-ord.txt -r d3adhob0.rule
```

Bruteforce attack (mask)
```bash
hashcat -m 0 -a 3 hashes.txt ?d?d?d?d?d?d?d?d
```

