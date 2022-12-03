f = open("input.txt", "r")
lines = f.readlines()

priority = 0

def findMatchingChar(line1, line2, line3): 
    for x in line1: 
        if x in line2 and x in line3: 
            return x

x = 0
while x < len(lines):

    line1 = lines[x].strip('\n')
    line2 = lines[x+ 1].strip('\n')
    line3 = lines[x + 2].strip('\n')

    
    matching = findMatchingChar(line1, line2, line3)

    #if uppercase: substract 64 from ord
    #if lowercase: subtract 96 from ord
    curPriority = 0
    if matching.isupper(): 
        curPriority = ord(matching) - 38

    else: curPriority = ord(matching) - 96

    priority += curPriority
    x+= 3
    
print(priority)