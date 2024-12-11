#Not finished

input_file = open("input.txt", "r")
input = input_file.readlines()
res = 0

height = len(input)
length = len(input[0])-1

antennas = []
antennas_pos = []
antinodes = []

for i in range(len(input)):
    line = input[i].strip()
    for j in range(len(line)):
        point = line[j]
        if point != ".":
            if point not in antennas:
                antennas.append(point)
                antennas_pos.append([[i, j]])
            else:
                antennas_pos[antennas.index(point)].append([i, j])

for i in range(len(antennas)):
    print(antennas[i] + " : " + str(antennas_pos[i]))

def in_tab(pos):
    if pos[0] >= 0 and pos[0] < height and pos[1] >= 0 and pos[1] < length:
        return True
    return False

for positions in antennas_pos:
    for i in range(len(positions)-1):
        pos = positions[i]
        for other_pos in positions[i+1:]:

            x = pos
            y = other_pos
            in1 = True

            while in1:
                antinode1 = [2*x[0] - y[0], 2*x[1] - y[1]]
                if in_tab(antinode1) :
                    if antinode1 not in antinodes:
                        antinodes.append(antinode1)
                    y = x
                    x = antinode1
                else:
                    in1 = False

            x = pos
            y = other_pos
            in2 = True

            while in2:
                antinode2 = [2*y[0] - x[0], 2*y[1] - x[1]]
                if in_tab(antinode2) :
                    if antinode2 not in antinodes:
                        antinodes.append(antinode2)
                    x = y
                    y = antinode2
                else:
                    in2 = False

res = len(antinodes)
print(antinodes)

print(res)
