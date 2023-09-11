# Password Cracking Workshop
Password cracking workshop for kompetensdag 2023-09-08

[Powerpoint](https://omegapointcloud-my.sharepoint.com/:p:/g/personal/davis_freimanis_omegapoint_se/ER_eqD61-25Fo9perRFmAIQBQnRQZOgK4BNh7jphftneUg?e=z66bpo)

`#kompetensdag-password-cracking`

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

## Sample Commands

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

## Sources

| Hashes                      | Amount |
|-----------------------------|--------|
| Omegapoint                  | 1000   |
| Rockyou                     | 1000   |
| Easy                        | 500    |
| English                     | 500    |
| Keyboard walk               | 500    |
| Numbers                     | 500    |
| Rockyou best64              | 500    |
| Rockyou d3ad0ne             | 500    |
| Swedish                     | 500    |
| Swedish real                | 1000   |
| Generate 8 chars end symbol | 1000   |
| Swedish generated best64    | 1000   |
| Generate 8 chars end digit  | 1000   |
| Name + year                 | 500    |

### Generation Instructions

- Rockyou (1000)

```bash
shuf -n 1000 /usr/share/wordlists/rockyou.txt > 1000-rockyou.txt
```

- Rockyou passwords with d3ad0ne rule (500)

```bash
shuf -n 500 /usr/share/wordlists/rockyou.txt | hashcat --force -r /usr/share/hashcat/rules/d3ad0ne.rule --stdout | shuf -n 500 > 500-rockyou-d3ad0ne.txt
```

- Rockyou passwords with best64 rule (500)

```bash
shuf -n 500 /usr/share/wordlists/rockyou.txt | hashcat --force -r /usr/share/hashcat/rules/best64.rule --stdout | shuf -n 500 > 500-rockyou-best64.txt
```

- Keyboard walks (500)

```bash
/opt/kwprocessor/kwp /opt/kwprocessor/basechars/full.base /opt/kwprocessor/keymaps/en-us.keymap /opt/kwprocessor/routes/2-to-16-max-3-direction-changes.route -z | shuf -n 100 > 500-kwp.txt

/opt/kwprocessor/kwp /opt/kwprocessor/basechars/full.base /opt/kwprocessor/keymaps/sv.keymap /opt/kwprocessor/routes/2-to-16-max-3-direction-changes.route -z | shuf -n 100 >> 500-kwp.txt

/opt/kwprocessor/kwp /opt/kwprocessor/basechars/full.base /opt/kwprocessor/keymaps/en-us.keymap /opt/kwprocessor/routes/2-to-16-max-3-direction-changes.route | shuf -n 100 >> 500-kwp.txt

/opt/kwprocessor/kwp /opt/kwprocessor/basechars/full.base /opt/kwprocessor/keymaps/sv.keymap /opt/kwprocessor/routes/2-to-16-max-3-direction-changes.route | shuf -n 100 >> 500-kwp.txt

/opt/kwprocessor/kwp /opt/kwprocessor/basechars/full.base /opt/kwprocessor/keymaps/dvorak.keymap /opt/kwprocessor/routes/2-to-16-max-3-direction-changes.route | shuf -n 100 >> 500-kwp.txt
```

- Easy passwords (500)

```bash
cat /usr/share/wordlists/SecLists/Passwords/darkweb2017-top10000.txt | shuf -n 500 > 500-easy.txt
```

- Swedish passwords with rules (1000)

```bash
Förnamn
Efternamn
Artister
Orter
Husdjursnamn
Svordommar

cat swedishwords.txt |  hashcat --force -r /opt/homebrew/Cellar/hashcat/6.2.6_1/share/doc/hashcat/rules/best64.rule --stdout | uniq | grep -vwE '\w{1,5}' | shuf -n 1000 > 1000-swedish-generated-best64.txt
```

- Swedish wordlist (500) [https://github.com/almgru/svenska-ord.txt](https://github.com/almgru/svenska-ord.txt)

```bash
cat svenska-ord.txt | shuf -n 500 > ../password-cracking-workshop/500-swedish.txt
```

- English wordlist (500)

```bash
cat words_alpha.txt | shuf -n 500 > ../password-cracking-workshop/500-english.txt
```

Number passwords up to 12 digits (500)

```bash
shuf -i 10000000-99999999 -n 100 > 500-numbers.txt
shuf -i 100000000-999999999 -n 100 >> 500-numbers.txt
shuf -i 1000000000-9999999999 -n 100 >> 500-numbers.txt
shuf -i 10000000000-99999999999 -n 100 >> 500-numbers.txt
shuf -i 100000000000-999999999999 -n 100 >> 500-numbers.txt
```

- Cewl from [omegapoint.se](http://omegapoint.se) (1000)

```bash
cewl -d 2 -m 8 https://omegapoint.se | shuf -n 1000 > 1000-omegapoint.txt
```

- Real Swedish passwords (1000)

```bash
From real password dumps
```

- Regular passwords with some standard rules (2000)

```bash
8 characters
Starts with uppercase
Ends with digits and symbol

OR

Ends with symbol and digit
```

- Name + Year

```bash
cat fornamn.txt efternamn.txt | while read line; do a=$((RANDOM%90+10));echo ${line}19$a; done | awk '{print toupper(substr($0, 1, 1)) tolower(substr($0, 2))}' | shuf -n 500 > 500-names-years.txt
```
