import copy

input_file = open("input.txt", "r")
input = input_file.readlines()
res = 0

def checkLine(line):
    for i in range(len(line)-1):
        x = int(line[i])
        y = int(line[i+1])
        if i == 0:
            if y >= x+1 and y <= x+3:
                op = '+'
            elif y <= x-1 and y >= x-3: 
                op = '-'
            else:
                break
        else:
            if op == '+':
                if y < x+1 or y > x+3:
                    break
            elif op == '-':
                if y > x-1 or y < x-3:
                    break
        if i == len(line)-2:
            return 1
    return 0

for line in input:
    temp = []
    line = line.strip()
    line = line.split(" ")
    if checkLine(line):
        res += 1
    else:
        for i in range(len(line)):
            temp = copy.copy(line)
            temp.pop(i)
            if checkLine(temp):
                res += 1
                break

print(res)


