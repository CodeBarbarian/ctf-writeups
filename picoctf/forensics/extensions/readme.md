# extensions

## Description
Author: Sanjay C/Danny

This is a really weird text file TXT? Can you find the flag?

## Approach
1. Download the file 

```bash
wget https://jupiter.challenges.picoctf.org/static/e7e5d188621ee705ceeb0452525412ef/flag.txt
```

2. Let us start by identifying the file

```bash
file flag.txt
```

Output:
```
flag.txt: PNG image data, 1697 x 608, 8-bit/color RGB, non-interlaced
```
We know that file extensions really don't mean anything, since the file signature (Magic Bytes) is what dictates how to read and interperet the contents of the file.

3. I guess we could just open this as an image? 

```bash
eog flag.txt
```

When we open the file we get the flag:
```
picoCTF{now_you_know_about_extensions}
```

## Conclusion 
Let us tidy up a bit before finishing: 
* Change the file extension to png
```bash
mv flag.txt flag.png
```

Fun little challenge! Important to always identify the file!
