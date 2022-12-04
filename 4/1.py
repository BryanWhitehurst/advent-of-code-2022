#read in each line without the newline character
lines = [line.rstrip() for line in open('input.txt')]

#check to see in how many assignments one range fully contains the other
def inRange(u1, l1, u2, l2):
    #range 1 contained in range 2
    if (u1 <= u2 and u1 >= l2 
        and l1 >= l2 and l1 <= u2): 
        return True

    #range 2 contained in range 1
    elif (u2 <= u1 and u2 >= l1 
        and l2 >= l1 and l2 <= u1): 
        return True

    return False

inRangeCount = 0
for item in lines:
    r1, r2 = item.split(",")
    l1, u1 = r1.split("-")
    l2, u2 = r2.split("-")
    
    if inRange(int(u1), int(l1), int(u2), int(l2)): inRangeCount += 1

print(inRangeCount)

