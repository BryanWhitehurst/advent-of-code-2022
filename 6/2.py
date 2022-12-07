f = open("input.txt", "r")

line = f.readline()

def checkDuplicates(str):
    return len(set(str)) == len(str) #checks for repeating characters

#checks each group of 14 characters in the string until a group of 4 unique chars is found
i = 0
while(i < len(line)):
    if checkDuplicates(line[i:i+14]): break
    i += 1

print(i+14)

