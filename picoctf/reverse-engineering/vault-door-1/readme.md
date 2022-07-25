# vaul-door-1

## Description

This vault uses some complicated arrays! I hope you can make sense of it, special agent. The source code for this vault is here: VaultDoor1.java

<br />

## Approach

1. Download file

```bash

wget https://jupiter.challenges.picoctf.org/static/ff2585f7afd21b81f69d2fbe37c081ae/VaultDoor1.java
```

<br />

2. By analyzing the code, we find a method named checkPassword which takes a string as a parameter. Okay, we see a string method called charAt(). After looking up the reference for this we get;

```
The charAt() method returns the character at the specified index in a string.
```

Okay, so since this is just checking if the string provided contains the following letters at a specific point in the index. 
We could do this by hand. 

So the first character needs to be a "d" given the following;
```java
password.charAt(0)  == 'd'
```
So lets give it a go doing it by hand, we have the method: 
```java
public boolean checkPassword(String password) {
        return password.length() == 32 &&
               password.charAt(0)  == 'd' &&
               password.charAt(29) == '9' &&
               password.charAt(4)  == 'r' &&
               password.charAt(2)  == '5' &&
               password.charAt(23) == 'r' &&
               password.charAt(3)  == 'c' &&
               password.charAt(17) == '4' &&
               password.charAt(1)  == '3' &&
               password.charAt(7)  == 'b' &&
               password.charAt(10) == '_' &&
               password.charAt(5)  == '4' &&
               password.charAt(9)  == '3' &&
               password.charAt(11) == 't' &&
               password.charAt(15) == 'c' &&
               password.charAt(8)  == 'l' &&
               password.charAt(12) == 'H' &&
               password.charAt(20) == 'c' &&
               password.charAt(14) == '_' &&
               password.charAt(6)  == 'm' &&
               password.charAt(24) == '5' &&
               password.charAt(18) == 'r' &&
               password.charAt(13) == '3' &&
               password.charAt(19) == '4' &&
               password.charAt(21) == 'T' &&
               password.charAt(16) == 'H' &&
               password.charAt(27) == '5' &&
               password.charAt(30) == '2' &&
               password.charAt(25) == '_' &&
               password.charAt(22) == '3' &&
               password.charAt(28) == '0' &&
               password.charAt(26) == '7' &&
               password.charAt(31) == 'e';
    }
```

We know it is 32 Characters long or 0-31. 

<br />

```
0 = d
1 = 3
2 = 5
3 = c
4 = r
5 = 4
6 = ...
7 = ......
```

3. This got to boring, so I am doing a script instead. Python + Regex should do the trick!

Okay, came up with a janky script that is a bit hacky but works! Quick and dirty gets the job done! 

FLAG: 
```
picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_75092e}
```

## Conclusion
Long time since I used regex with python. Skills that I learned by doing this is that why spend 5 minutes deciphering the character positions by hand, when you can spend an hour getting python to work with regex!
Fun challenge! Was a quick and dirty script but did the job! 



