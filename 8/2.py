#create 2d array 
#for a tree to be visible, it must pass one of the following criteria: 
#lines[y][x]
#every tree in y: range 0->i must be less than trees[i][j]
#every tree in y: range i->len(trees) must be less than trees[i][j]
#every tree in x: range 0->j must be less than trees[i][j]
#every tree in x: range j->len(trees[0]) must be less than trees[i][j]
trees = [line.rstrip() for line in open('input.txt')]

def checkUp(i, j):
    for y in range(i - 1, 0, -1):
        if trees[y][j] >= trees[i][j]: return i - y
    return i

def checkDown(i, j): 
    for y in range(i + 1, len(trees)):
        if trees[y][j] >= trees[i][j]: return y - i
    return len(trees) - 1 - i

def checkLeft(i, j): 
    for x in range(j - 1, 0, -1):
        if trees[i][x] >= trees[i][j]: return j - x
    return j

def checkRight(i, j):
    for x in range(j + 1, len(trees[0])):
        if trees[i][x] >= trees[i][j]: return x - j
    return len(trees[0]) - 1 - j


scenicScores = []
for i in range(1, len(trees) - 1):
    for j in range(1, len(trees[0]) - 1): 
        scenicScores.append(checkUp(i, j) * checkDown(i, j) * checkLeft(i, j) * checkRight(i, j))

print(max(scenicScores))

