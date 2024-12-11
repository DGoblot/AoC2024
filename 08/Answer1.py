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

def in_tab(pos):
    if pos[0] >= 0 and pos[0] < height and pos[1] >= 0 and pos[1] < length:
        return True
    return False

for positions in antennas_pos:
    for i in range(len(positions)-1):
        pos = positions[i]
        for other_pos in positions[i+1:]:
            antinode1 = [2*pos[0] - other_pos[0], 2*pos[1] - other_pos[1]]
            antinode2 = [2*other_pos[0] - pos[0], 2*other_pos[1] - pos[1]]
            if antinode1 not in antinodes and in_tab(antinode1) :
                antinodes.append(antinode1)
            if antinode2 not in antinodes and in_tab(antinode2) :
                antinodes.append(antinode2)

res = len(antinodes)

print(res)
