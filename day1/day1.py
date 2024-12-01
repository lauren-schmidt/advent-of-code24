import math

## Part 1 
list1 = []
list2 = []

with open('input.txt') as input_file: 
    for line in input_file: 
        s = line.split()
        list1.append(s[0])
        list2.append(s[1])

list1.sort()
list2.sort()

distancesum = 0

for i in range(len(list1)):
    distancesum += abs(int(list1[i]) - int(list2[i]))


print("Distance sum is: " + str(distancesum))

d2 = {}

## Part 2 
# Count up number of times each occurs for dict2
for i in list2: 
    if i in d2:
        d2[i] += 1
    else: 
        d2[i] = 1


# Calculate similarity score 
score = 0
for i in list1: 
    if i in d2: 
        score += int(i) * d2[i]
        
print("Similarity score is: " + str(score))
