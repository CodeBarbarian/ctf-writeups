encrypted_flag = "16 9 3 15 3 20 6 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14"
alphabet = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"

data = encrypted_flag.split(" ")
cipher = alphabet.split(" ")

for c in data:
  print(cipher[int(c)-1])
