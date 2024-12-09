input_file = open("input.txt", "r")
input = input_file.readlines()
res = 0
col1 = []
col2 = []

for line in input:
    line = line.strip()
    t = line.split("   ")
    col1.append(int(t[0]))
    col2.append(int(t[1]))

for i in range(len(col1)):
    res += col2.count(col1[i]) * col1[i]

print(res)