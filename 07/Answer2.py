import itertools

input_file = open("input.txt", "r")
input = input_file.readlines()
res = 0
goals = []
numbers = []
t = [0, 1, 2]

for line in input:
    line = line.strip()
    temp = line.split(":")
    goals.append(temp[0].strip())
    numbers.append(list(temp[1].strip().split(" ")))

def compute(nb, op, goal):
    tmp = int(nb[0])
    for i in range(len(op)):
        match op[i]:
            case 0:
                tmp += int(nb[i+1])
            case 1:
                tmp *= int(nb[i+1])
            case 2:
                tmp = int(str(tmp)+nb[i+1])
        if tmp > goal:
            return 0
    return tmp

for i in range(len(goals)):
    nb = numbers[i]
    goal = int(goals[i])
    r = len(nb)-1
    operations = itertools.product(t, repeat=r)
    for op in list(operations):
        tot = compute(nb, op, goal)
        print(tot, goal)
        if goal == tot:
            res += tot
            break  

print(res)