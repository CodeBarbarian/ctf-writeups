# Warmed Up

## Description
What is 0x3D (base 16) in decimal (base 10)?

## Approach

1. This seems like quite the easy challenge?

```bash
echo "0x3D" | xxd -r | od -td1
```

This will give us the result of:

```bash
0000000   61
0000001

```

So the flag is: picoCTF{61}

## Conclusion

Fun little challenge. Used xxd to take dump the hex on the fly into old but trustworthy od. Could probably use od for all of it since it can convert input to many other forms such as hex, decimal, ascii, char and so on. 

Still a very essential skill to convert from different conversions. 

