import re

# We know that we need something to keep count
count = 0

# We know we need to itereate 32 times through this
numberofruns = 32

# To store the flag, with the typical pico begining.
flag = "picoCTF{"

# Iterate over the File 32 times.
for i in range(numberofruns):
  file = open('VaultDoor1.java', 'r')

  for line in file:
    regex = r".*password\.charAt\("+str(count)+"\).* == '([a-zA-Z0-9_])'"
    blargh = re.match(regex,line)
    if blargh:
      # Add the matched group to the 
      flag += (blargh.group(1))

  count += 1
  file.close()

# End the flag with ms curly
flag += "}"

# Print the flag (Hopefully)
print (flag)
