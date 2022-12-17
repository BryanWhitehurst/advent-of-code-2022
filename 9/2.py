instructions = [line.rstrip() for line in open('input.txt')]

maxLR = 1
maxUD = 1
netLR = 1
netUD = 1 
for i in instructions: 
    if i.split(" ")[0] == 'U':
        netUD += int(i.split(" ")[1])

    elif i.split(" ")[0] == 'D':
        netUD -= int(i.split(" ")[1])

    elif i.split(" ")[0] == 'L':
        netLR -= int(i.split(" ")[1])
    
    elif i.split(" ")[0] == 'R':
        netLR += int(i.split(" ")[1])
    
    if netLR > maxLR: maxLR = netLR
    if netUD > maxUD: maxUD = netUD
    

array = [['.' for x in range(maxLR)] for y in range(maxUD)] 

#instead of keeping track of 2, we now need to keep track of 8 points between head and tail
Hpos = [1, 1]

positions = [[1, 1] for y in range(9)] 
visited = []


def moveNonHead(head, tail): 
    if(abs(head[0] - tail[0]) >= 2 and head[1] == tail[1]):
        if head[0] > tail[0]: tail[0] += 1
        else: tail[0] -= 1
   
    # if y is different but x is the same
    elif(abs(head[1] - tail[1]) >= 2 and head[0] == tail[0]):
        if head[1] > tail[1]: tail[1] += 1
        else: tail[1] -= 1

    #4 different cases for diagonal movement
    #if head[y] - tail[y] >= 2 and tail[x] < head[x] : this could be an up right or down right movement
    if abs(head[1] - tail[1]) >= 2 and tail[0] < head[0]:
        if head[1] > tail[1]: # up right
            tail[0] += 1
            tail[1] += 1

        else: # down right
            tail[0] += 1
            tail[1] -= 1

    #up left or down left
    if abs(head[1] - tail[1]) >= 2 and tail[0] > head[0]:
        if head[1] > tail[1]: # up left
            tail[0] -= 1
            tail[1] += 1

        else: # down left
            tail[0] -= 1
            tail[1] -= 1
    

    #up left or down left
    if abs(head[0] - tail[0]) >= 2 and head[1] > tail[1]:
        if head[0] > tail[0]: # up left
            tail[0] += 1
            tail[1] += 1

        else: # down left
            tail[0] -= 1
            tail[1] += 1

    if abs(head[0] - tail[0]) >= 2 and head[1] < tail[1]:
        if head[0] > tail[0]: # up left
            tail[0] += 1
            tail[1] -= 1

        else: # down left
            tail[0] -= 1
            tail[1] -= 1


def moveRope(i): 
    #moves Head
    if i.split(" ")[0] == 'U':
        Hpos[1] += int(i.split(" ")[1])

    elif i.split(" ")[0] == 'D':
        Hpos[1] -= int(i.split(" ")[1])

    elif i.split(" ")[0] == 'L':
        Hpos[0] -= int(i.split(" ")[1])
    
    elif i.split(" ")[0] == 'R':
        Hpos[0] += int(i.split(" ")[1])


    moveNonHead(Hpos, positions[0])
    for j in range(len(positions) - 1): 
        moveNonHead(positions[j], positions[j + 1])

    tailAsTuple = (positions[8][0], positions[8][1])
    if tailAsTuple not in visited: visited.append(tailAsTuple)
    


for i in instructions:

    direction, number = i.split(" ")
    number = int(number)

    for j in range(number):
        moveRope(direction + " 1")


print(len(visited))


