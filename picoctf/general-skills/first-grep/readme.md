# First Grep

## Description
Can you find the flag in file? This would be really tedious to look through manually, something tells me there is a better way.

## Approach
1. Download the file
```
wget https://jupiter.challenges.picoctf.org/static/315d3325dc668ab7f1af9194f2de7e7a/file
```
2. Identify the file

```bash
file file
```

Output:

```
file: ASCII text, with very long lines (4200)
```

3. So let us see if there is anything related to a flag in there

```bash
cat file | grep -i pico
```

Output, which is also our flag:
```
picoCTF{grep_is_good_to_find_things_f77e0797}
```

## Conclusion
Grep is good for finding things.

