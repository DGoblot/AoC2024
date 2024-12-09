import re

input_file = open("input.txt", "r")
input = input_file.readlines()
res = 0
for line in input:
    line = re.findall('(mul\([0-9]{1,3}\,[0-9]{1,3}\))', line)
    for i in range(len(line)):
        xy = re.findall("([0-9]{1,3})", line[i])
        res += int(xy[0])*int(xy[1])
print(res)
