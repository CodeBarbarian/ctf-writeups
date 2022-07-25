# Easy1

## Description

The one time pad can be cryptographically secure, but not when you know the key. Can you solve this? We've given you the encrypted flag, key, and a table to help UFJKXQZQUNB with the key of SOLVECRYPTO. Can you use this table to solve it?. 

## Approach
1. Get the table

```bash
wget https://jupiter.challenges.picoctf.org/static/1fd21547c154c678d2dab145c29f1d79/table.txt
```
2. Okay, time to brush up on some cryptography. So a one time pad in my understanding is as far as I know unbreakable if you don't have the key, fortunately for us we do. 

To break the one time pad cipher both the message and the key must be of the same length:

```
UFJKXQZQUNB
SOLVECRYPTO

```
They are, good. Then it should just be going through the table, matching the KEY to the corresponding letter:

```
S+U = C
O+F = R
L+J = Y
V+K = P
E+X = T
C+Q = O
R+Z = I
Y+Q = S
P+U = F
T+N = U
O+B = N

```

Flag: 

```
picoCTF{CRYPTOISFUN}
```
## Conclusion
That was fun! A little bit interested to see how I would do that programmatically. 
In this challenge you will learn how to use a one time pad encryption, following the rules of a one time pad cipher.
