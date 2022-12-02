f = open("input.txt", "r")

lines = f.readlines()

score = 0

#A rock, B paper, C scissors
#X rock, Y paper, Z scissors

#A win: if we play, x, they must play scissors for a win

#1 for rock, 2 for paper, 3 for scissors
# 6 for winning

newPlays = []
#now we make the second val what we need to play and pass it to the below code
for line in lines:
    plays = line.split(" ")
    #we need to lose
    if plays[1].strip("\n") == 'X':
        if plays[0] == 'A': 
            newPlays.append(['A', 'Z'])
        elif plays[0] == 'B':
            newPlays.append(['B', 'X'])
        elif plays[0] == 'C': 
            newPlays.append(['C', 'Y'])

    #we need to draw
    elif plays[1].strip("\n") == 'Y':
        if plays[0] == 'A': 
            newPlays.append(['A', 'X'])
        elif plays[0] == 'B':
            newPlays.append(['B', 'Y'])
        elif plays[0] == 'C': 
            newPlays.append(['C', 'Z'])
    
    #we need to win 
    elif plays[1].strip("\n") == 'Z':
        if plays[0] == 'A': 
            newPlays.append(['A', 'Y'])
        elif plays[0] == 'B':
            newPlays.append(['B', 'Z'])
        elif plays[0] == 'C': 
            newPlays.append(['C', 'X'])


for line in newPlays: 
    if line[1].strip('\n') == 'X': 
        score += 1
    elif line[1].strip('\n') == 'Y':
        score += 2
    elif line[1].strip('\n') == 'Z':
        score += 3

    if line[1].strip('\n') == 'X' and line[0] == 'C':
        score += 6

    elif line[1].strip('\n') == 'Y' and line[0] == 'A':
        score += 6

    elif line[1].strip('\n') == 'Z' and line[0] == 'B':
        score += 6

    elif (line[1].strip('\n') == 'X' and line[0] == 'A') or (line[1].strip('\n') == 'Y' and line[0] == 'B') or (line[1].strip('\n') == 'Z' and line[0] == 'C'):
        score += 3

print(score)