# The Numbers

## Description 

The numbers... what do they mean?

## Approach

1. Download the file
```
wget https://jupiter.challenges.picoctf.org/static/f209a32253affb6f547a585649ba4fda/the_numbers.png
```

2. Let us go trough the list:

```bash
file the_numbers.png
```
Output:
```
the_numbers.png: PNG image data, 774 x 433, 8-bit/color RGB, non-interlaced
```

Okay, so we have a png image. Let us open it and see
In the image we get the following numbers:

```
16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14}
```

This looks like the flag with spaces as the delimiter between the characters. Since this is cryptography challenge i assume this is a simple substitution cipher? Wher A = 1, B = 2, C = 3? 

So the flag is PICOCTF{THENUMBERSMASON}

16 	= P
9	= I
3	= C
15	= O
3	= C
20	= T
6	= F
20	= T
8	= H
5	= E
14	= N
21	= U
13	= M
2	= B
5	= E
18	= R
19	= S
13	= M
1	= A
19	= S
15	= O
14	= N

<br />

## Conclusion
Fun challenge. Created a tiny script to do this in python afterwards just for the lolz.
Skills you will learn are basic understanding for substitution ciphers.
