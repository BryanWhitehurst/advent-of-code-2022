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

#we have created our array properly
#on first instruction, only H moves, T will move on second move
Hpos = [1, 1]
Tpos = [1, 1]

visited = []

def moveRope(i): 
    if i.split(" ")[0] == 'U':
        Hpos[1] += int(i.split(" ")[1])

    elif i.split(" ")[0] == 'D':
        Hpos[1] -= int(i.split(" ")[1])

    elif i.split(" ")[0] == 'L':
        Hpos[0] -= int(i.split(" ")[1])
    
    elif i.split(" ")[0] == 'R':
        Hpos[0] += int(i.split(" ")[1])

    if(abs(Hpos[0] - Tpos[0]) >= 2 and Hpos[1] == Tpos[1]):
        if Hpos[0] > Tpos[0]: Tpos[0] += 1
        else: Tpos[0] -= 1
   
    # if y is different but x is the same
    elif(abs(Hpos[1] - Tpos[1]) >= 2 and Hpos[0] == Tpos[0]):
        if Hpos[1] > Tpos[1]: Tpos[1] += 1
        else: Tpos[1] -= 1

    #4 different cases for diagonal movement
    #if Hpos[y] - Tpos[y] >= 2 and Tpos[x] < Hpos[x] : this could be an up right or down right movement

    if abs(Hpos[1] - Tpos[1]) >= 2 and Tpos[0] < Hpos[0]:
        if Hpos[1] > Tpos[1]: # up right
            Tpos[0] += 1
            Tpos[1] += 1

        else: # down right
            Tpos[0] += 1
            Tpos[1] -= 1

    #up left or down left
    if abs(Hpos[1] - Tpos[1]) >= 2 and Tpos[0] > Hpos[0]:
        if Hpos[1] > Tpos[1]: # up left
            Tpos[0] -= 1
            Tpos[1] += 1

        else: # down left
            Tpos[0] -= 1
            Tpos[1] -= 1
    

    #up left or down left
    if abs(Hpos[0] - Tpos[0]) >= 2 and Hpos[1] > Tpos[1]:
        if Hpos[0] > Tpos[0]: # up left
            Tpos[0] += 1
            Tpos[1] += 1

        else: # down left
            Tpos[0] -= 1
            Tpos[1] += 1

    if abs(Hpos[0] - Tpos[0]) >= 2 and Hpos[1] < Tpos[1]:
        if Hpos[0] > Tpos[0]: # up left
            Tpos[0] += 1
            Tpos[1] -= 1

        else: # down left
            Tpos[0] -= 1
            Tpos[1] -= 1

    posAsTuple = (Tpos[0], Tpos[1])
    if posAsTuple not in visited: visited.append(posAsTuple)


for i in instructions:

    direction, number = i.split(" ")
    number = int(number)

    for j in range(number):
        moveRope(direction + " 1")


print(len(visited))


