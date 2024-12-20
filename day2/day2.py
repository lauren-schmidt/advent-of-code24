## PART ONE 

def check(report):
    prev = report[0]
    unsafe = False 
    increasing = report[1] > report[0]

    for lev in report[1:]:
        diff = abs(lev - prev)
        if (diff == 0 or diff > 3) or (increasing and lev < prev) or (not(increasing) and lev > prev):
            unsafe = True
            break
        prev = lev
    return not(unsafe)



reports = []
reports_int = []
num_safe = 0

# Read in the files 
with open('day2.txt') as input_file:
    for line in input_file:
        s = line.split()
        # Add each, make a list of lists 
        reports.append(s)

for report in reports:
    reports_int.append([int(x) for x in report])

for r in reports_int: 
    if check(r):
        num_safe += 1

print("Number of safe reports: " + str(num_safe))

## PART TWO 
safe_with_damp = 0
for r in reports_int: 
    safeinit = check(r)
    if(safeinit):
        safe_with_damp += 1
    else:
        for i, a in enumerate(r):
            dampened = list(r)
            del dampened[i]
            if check(dampened):
                safe_with_damp += 1
                break
print("Number of reports safe with dampening: " + str(safe_with_damp))