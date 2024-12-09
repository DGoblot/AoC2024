import re

input_file = open("day3.txt", "r")
input = input_file.read()
res = 0

def mult(list):
    tmp = 0
    list = re.findall('(mul\([0-9]{1,3}\,[0-9]{1,3}\))', list)
    for i in range(len(list)):
        xy = re.findall("([0-9]{1,3})", list[i])
        tmp += int(xy[0])*int(xy[1])
    return tmp
    
def split(line):
    start = line.find("do()")
    end = line.find("don't()")
    return line[start:end], end
    
while input.find("do()") != -1 and input.find("don't()") != -1:
    subline, end = split(input)
    res += mult(subline)
    input = input[end+1:]

print(res)
