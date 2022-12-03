f = open("input.txt", "r")
lines = f.readlines()

priority = 0

def findMatchingChar(comp1, comp2): 
    for x in comp1: 
        for y in comp2:
            if x == y: return x


#covert each line into 2 strings
#find character in common
for line in lines:
    line = line.strip('\n')
    compartmentOne = line[0:len(line)/2]
    CompartmentTwo = line[len(line)/2:len(line)]
    
    matching = findMatchingChar(compartmentOne, CompartmentTwo)

    #if uppercase: substract 64 from ord
    #if lowercase: subtract 96 from char
    curPriority = 0
    if matching.isupper(): 
        curPriority = ord(matching) - 38

    else: curPriority = ord(matching) - 96

    priority += curPriority

print(priority)