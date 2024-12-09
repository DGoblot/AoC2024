import math

input_file = open("input.txt", "r")
input = input_file.readlines()
res = 0

for i in range(len(input)):
    if "^" in input[i]:
        pos = (i, input[i].index("^"))
        direc = (-1,0)
        pos = tuple(map(lambda i, j: i + j, pos, direc))
        res += 1
    input[i] = list(input[i]) 



while pos[0] >= 0 and pos[0] <len(input) and pos[1] >= 0 and pos[1] < len(input[0]):
    if input[pos[0]][pos[1]] != "#":
        if input[pos[0]][pos[1]] == ".":
            res += 1
            input[pos[0]][pos[1]] = "X"
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

print(res)
