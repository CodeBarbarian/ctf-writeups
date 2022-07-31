# Based

## Description
Author: Alex Fulton/Daniel Tunitis

To get truly 1337, you must understand different data encodings, such as hexadecimal or binary. Can you get the flag from this program to prove you are on the way to becoming 1337? Connect with nc jupiter.challenges.picoctf.org 15130.

## Approach

1. Let us start by connecting to the server using netcat:

```bash
nc jupiter.challenges.picoctf.org 15130
```

Okay, when prompted we get a variation of the following: 
```
Let us see how data is stored
pie
Please give the 01110000 01101001 01100101 as a word.
...
you have 45 seconds.....

Input:
```

2. Okay so we need to convert whatever is outputed from binary to ASCII text. Let us use some online decoder for this, found this: https://cryptii.com/pipes/binary-decoder

After doing the prompt again I got the following: 

```
Let us see how data is stored
chair
Please give the 01100011 01101000 01100001 01101001 01110010 as a word.
...
you have 45 seconds.....

Input:
chair
Please give me the  164 141 142 154 145 as a word.
Input:
Too slow!
```

This looks like we need to convert octal to text as well:

3. So let us do it again. 

Order looks like: 
* Binary
* Octal
* Hex

So I just looked up converters for those and then I got the flag: 

FLag: 
```
picoCTF{learning_about_converting_values_02167de8}
```
## Conclusion
Fun challenge, important to learn and cover all the bases! 
