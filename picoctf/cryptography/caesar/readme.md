# caesar

## Description
Decrypt this message.

## Approach
1. Get the message

```bash
wget https://jupiter.challenges.picoctf.org/static/49f31c8f17817dc2d367428c9e5ab0bc/ciphertext
```

2. We can assume this is caesar cipher, so if we have a look at the man page for the tr tool. This command should do the trick (After some trying and failing)

```bash
echo "ynkooejcpdanqxeykjrbdofgkq" | tr '[a-z]' '[e-za-d]'
```

Output:

```
crossingtherubiconvfhsjkou
```

So the complete flag: 

```
picoCTF{crossingtherubiconvfhsjkou}
```

## Conclusion
Learned to use the tr command. I think, some of it still seems like a mystery to me! 
Fun little challenge, remember we used to play around with caesar ciphers with different shifts when I went to middle school. 

