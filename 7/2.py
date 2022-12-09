lines = [line.rstrip() for line in open('input.txt')]

lineNum = 0
total = 0 

totals = []

def recursiveSearch(lineNum):
    global total
    curTotal = 0

    while(1): 
        if lines[lineNum][0] == 'd': #we have reached a sub directory
            dirName = lines[lineNum].split(" ")[1]

            curLine = lineNum
            dotdotCount = 0
            cdCount = 0
            while(1):
                if "cd " + dirName in lines[curLine] and dotdotCount == cdCount: break 
                if "$ cd " in lines[curLine] and lines[curLine] != "$ cd ..": cdCount += 1
                elif "$ cd " in lines[curLine]: dotdotCount += 1
                curLine += 1
            curTotal += recursiveSearch(curLine + 2) 

        elif unicode(lines[lineNum][0], 'utf-8').isnumeric(): 
            curTotal += int(lines[lineNum].split(" ")[0])

        #check if we're at the end of the array or if next line contains $
        if (lineNum == (len(lines) - 1)) or (lines[lineNum][0] == '$'):
            totals.append(curTotal)
            if curTotal <= 100000: total += curTotal
            return curTotal
        
        lineNum += 1
    

#start on the third line
recursiveSearch(2)
candidates = []

unusedSpace = 70000000 - totals[-1]
for t in totals: 
    if unusedSpace + t >= 30000000:
            candidates.append(t)

print(min(candidates))
