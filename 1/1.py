f = open("input.txt", "r")

lines = f.readlines()
totals = [] #holds total number of calories for each elf
curTotal = 0 #keep track of current calorie count

#go line by line in input
for line in lines: 
    if line == '\n': #if its an empty line, we know we have reached the total for the current elf
        totals.append(curTotal)
        curTotal = 0 #reset curTotal back to 0

        continue

    curTotal += int(line) #add current food item to current calorie count

#for part 1, we want the elf with the most calories
mostCalories = max(totals)

print("Highest Calorie Count: " + str(mostCalories))
