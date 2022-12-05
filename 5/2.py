lines = [line.rstrip() for line in open('input.txt')]
#step 1: parse stacks into 2D array
#get length of array
#for each stack, read in elements from top to bottom
#then use python list reverse
numStacks = 0
numStacksLineIndex = 0 
for line in lines: 
    #find the line where the stack numbers start
    if line.strip()[0] == '1':
        numStacks = line.strip()[len(line.strip()) - 1]
        break
    numStacksLineIndex += 1

stacks = [[] for y in range(int(numStacks))] 

#this var is used to keep track of the current line index
curIndex = 1
for x in range(int(numStacks)): 
    for line in lines: 
        #find the line where the stack numbers start
        if line.strip()[0] == '1':
            break
        
        #if there is an element in this stack position
        if curIndex < len(line) and not(line[curIndex] == " "):
            stacks[x].append(line[curIndex])
    curIndex += 4

#reverse order of each stack
for stack in stacks:
    stack.reverse()

#take subarrays of each starting stack and move the enitre subarray in its original order to destination
for x in range(numStacksLineIndex + 2, len(lines)): 
    str1, str2 = lines[x].split(' from ')
    numToMove = str1.split(' ')[1]
    startingStack, endingStack = str2.split(' to ')
    

    movingElements = stacks[int(startingStack) - 1][len(stacks[int(startingStack) - 1]) - int(numToMove):len(stacks[int(startingStack) - 1])]
    
    stacks[int(startingStack) - 1] = stacks[int(startingStack) - 1][0: len(stacks[int(startingStack) - 1]) - int(numToMove)]
    stacks[int(endingStack) - 1] += movingElements

answerString = ""

for stack in stacks:
    answerString += stack[-1]

print(answerString)