f = open("input.txt", "r")

lines = f.readlines()


score = 0

#A rock, B paper, C scissors
#X rock, Y paper, Z scissors

#A win: if we play, x, they must play scissors for a win

#1 for rock, 2 for paper, 3 for scissors
# 6 for winning
for line in lines: 
    plays = line.split(" ")

    if plays[1].strip('\n') == 'X': 
        score += 1
    elif plays[1].strip('\n') == 'Y':
        score += 2
    elif plays[1].strip('\n') == 'Z':
        score += 3

    if plays[1].strip('\n') == 'X' and plays[0] == 'C':
        score += 6

    elif plays[1].strip('\n') == 'Y' and plays[0] == 'A':
        score += 6

    elif plays[1].strip('\n') == 'Z' and plays[0] == 'B':
        score += 6

    elif (plays[1].strip('\n') == 'X' and plays[0] == 'A') or (plays[1].strip('\n') == 'Y' and plays[0] == 'B') or (plays[1].strip('\n') == 'Z' and plays[0] == 'C'):
        score += 3

print(score)