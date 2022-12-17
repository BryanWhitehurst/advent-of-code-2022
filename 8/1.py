#create 2d array 
#for a tree to be visible, it must pass one of the following criteria: 
#lines[y][x]
#every tree in y: range 0->i must be less than trees[i][j]
#every tree in y: range i->len(trees) must be less than trees[i][j]
#every tree in x: range 0->j must be less than trees[i][j]
#every tree in x: range j->len(trees[0]) must be less than trees[i][j]
trees = [line.rstrip() for line in open('input.txt')]

def checkUp(i, j):
    for y in range(i):
        if trees[y][j] >= trees[i][j]: return False
    return True

def checkDown(i, j): 
    for y in range(i + 1, len(trees)):
        if trees[y][j] >= trees[i][j]: return False
    return True

def checkLeft(i, j): 
    for x in range(j):
        if trees[i][x] >= trees[i][j]: return False
    return True

def checkRight(i, j):
    for x in range(j + 1, len(trees[0])):
        if trees[i][x] >= trees[i][j]: return False
    return True

totalVisible = (len(trees) * 2) + (len(trees[0]) * 2) - 4 #count corners twice
print(totalVisible)
for i in range(1, len(trees) - 1):
    for j in range(1, len(trees[0]) - 1):
        if(checkUp(i, j) or checkDown(i, j) or checkLeft(i, j) or checkRight(i, j)):
            totalVisible += 1
        else: 
            print(trees[i][j])
            #print("i: " + str(i) + " j: " + str(j))

print(totalVisible)