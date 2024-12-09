input_file = open("input.txt", "r")
input = input_file.readlines()
res = 0
tot = []
nb = []

for line in input:
    line = line.strip()
    temp = line.split(":")
    tot.append(temp[0].strip())
    nb.append(list(temp[1].strip().split(" ")))

for i in range(len(tot)):
    pass

print(res)