# Bases

## Description
What does this bDNhcm5fdGgzX3IwcDM1 mean? I think it has something to do with bases.

## Approach

1. Just by the name the first thing that comes to mind is base64 encoding? Let us test that by decoding the string in the terminal by using the base64 command passing in the -d flag for decode. 

```bash
echo "bDNhcm5fdGgzX3IwcDM1" | base64 -d
```

Output:
``` 
l3arn_th3_r0p35
```

Flag:
```
picoCTF{l3arn_th3_r0p35}
```

## Conclusion
Base64 is a great encoding especially if you are going to encode binary data for data transfers that only supports ascii. 
Fun quick and easy challenge! 

