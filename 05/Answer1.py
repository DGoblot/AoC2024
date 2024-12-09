import math


input_file = open("input.txt", "r")
input = input_file.readlines()
res = 0
before = []
after = []
orders = []


for line in input:
    line = line.strip()
    if "|" in line:
        before.append(line[:line.index("|")])
        after.append(line[line.index("|")+1:])
    elif "," in line:
        orders.append(line.split(","))

for order in orders:
    test = True
    for j in range(len(order)-1):
        for k in range(len(order[j+1:])):
            for t in range(len(before)):
                if order[j] == after[t] and order[k+j+1] == before[t]:
                    test = False
                    break
            if not test:
                break
        if not test:
            break
    if test:
        res += int(order[math.floor(len(order)/2)])


print(res)
