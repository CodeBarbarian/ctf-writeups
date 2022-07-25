# strings it

## Description
Can you find the flag in file without running it?

## Approach

1. Download the file

```bash
wget https://jupiter.challenges.picoctf.org/static/94d00153b0057d37da225ee79a846c62/strings
```

2. I guess they want us to use strings? 

Strings simply prints the sequence of strings in a file.

```bash
strings strings -n 10 | grep -i pico
``` 
Output: 

```bash
picoCTF{5tRIng5_1T_d66c7bb7}
```
## Conclusion
Strings! Fun little challenge, a tool i often forget to use, so nice to be reminded it exists!
