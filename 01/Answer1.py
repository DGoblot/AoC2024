input_file = open("input.txt", "r")
input = input_file.readlines()
res = 0
col1 = []
col2 = []

for line in input:
    line = line.strip()
    t = line.split("   ")
    col1.append(t[0])
    col2.append(t[1])

col1.sort()
col2.sort()

for i in range(len(col1)):
    res += abs(int(col1[i])-int(col2[i]))

print(res)