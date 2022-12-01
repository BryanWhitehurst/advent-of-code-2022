f = open("input.txt", "r")

lines = f.readlines()
totals = [] #holds total number of calories for each elf
curTotal = 0 #keep track of current calorie count

#read in each line from input file
for line in lines: 
    if line == '\n': #if its an empty line, we know we have reached the total for the current elf
        totals.append(curTotal)
        curTotal = 0 #reset curTotal back to 0

        continue

    curTotal += int(line) #add current food item to current calorie count

#for part 2, we want the sum of the three highest calorie counts
totals.sort()

newTotal = totals[len(totals) - 1] + totals[len(totals) - 2] + totals[len(totals) - 3]
print("Sum of three highest: " + str(newTotal))
    