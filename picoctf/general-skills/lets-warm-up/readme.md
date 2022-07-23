# Lets Warm Up

## Description
If I told you a word started with 0x70 in hexadecimal, what would it start with in ASCII? 

<br />

## Approach 
1. So to do a simple hexadecimal conversion you could simply use a ASCII table since it has "Decimal", "Hex", "Octal" and the corresponding "Character" conversion. I decided to use the command line utility xxd

```bash
echo "0x70" | xxd -r
```

which will give me the result of the letter: p

2. So the flag:

```
picoCTF{p}
```

<br />

## Conclusion
Absolutely a general skill to learn, and a useful one for learning the conversion between hexadecimal and ASCII.
