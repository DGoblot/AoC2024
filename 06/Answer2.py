import copy

input_file = open("input.txt", "r")
input = input_file.readlines()
res = 0

for i in range(len(input)):
    if "^" in input[i]:
        pos_start = (i, input[i].index("^"))
        direc_start = (-1,0)
    input[i] = input[i].strip()
    input[i] = list(input[i])

original_path = copy.deepcopy(input)

pos = pos_start
direc = direc_start
while pos[0] >= 0 and pos[0] < len(original_path) and pos[1] >= 0 and pos[1] < len(original_path[0]):
    if original_path[pos[0]][pos[1]] != "#":
        if original_path[pos[0]][pos[1]] == ".":
            original_path[pos[0]][pos[1]] = "X"
        pos = tuple(map(lambda i, j: i + j, pos, direc))
    else:
        pos = tuple(map(lambda i, j: i - j, pos, direc))
        match direc:
            case (-1,0):
                direc = (0,1)
            case (0,1):
                direc = (1,0)
            case (1,0):
                direc = (0,-1)
            case (0,-1):
                direc = (-1,0)
        pos = tuple(map(lambda i, j: i + j, pos, direc))

def test(input, pos_start, direc_start, direc_tab):
    pos = pos_start
    direc = direc_start
    while pos[0] >= 0 and pos[0] <len(input) and pos[1] >= 0 and pos[1] < len(input[0]):
        
        if input[pos[0]][pos[1]] != "#":
            if input[pos[0]][pos[1]] == ".":
                input[pos[0]][pos[1]] = "X"
            elif input[pos[0]][pos[1]] == "X":
                if direc_tab[pos[0]][pos[1]] == direc:
                    return 1
                else:
                  direc_tab[pos[0]][pos[1]] = direc 
            pos = tuple(map(lambda i, j: i + j, pos, direc))
        else:
            pos = tuple(map(lambda i, j: i - j, pos, direc))
            match direc:
                case (-1,0):
                    direc = (0,1)
                case (0,1):
                    direc = (1,0)
                case (1,0):
                    direc = (0,-1)
                case (0,-1):
                    direc = (-1,0)
            pos = tuple(map(lambda i, j: i + j, pos, direc))
    return 0

for i in range(len(input)):
    for j in range(len(input[0])):
        if original_path[i][j] == "X":
            input_test = copy.deepcopy(input)
            input_test[i][j] = "#"
            direc_tab = [[0 for col in range(len(input[0]))] for row in range(len(input))]
            print(i, j)
            res += test(input_test, pos_start, direc_start, direc_tab)

print(res)
