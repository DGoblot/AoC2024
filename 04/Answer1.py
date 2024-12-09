input_file = open("input.txt", "r")
input = input_file.readlines()
res = 0

def check(input, i, j, x, y, letter):
    i += x
    j += y
    if i >= 0 and i < len(input):
        if j >= 0 and j < len(input[i]):
            if input[i][j] == letter:
                match letter:
                    case "M":
                        return check(input, i, j, x, y, "A")
                    case "A":
                        return check(input, i, j, x, y, "S")
                    case "S":
                        return 1
    return 0

for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == "X":
            for x in range(-1,2):
                for y in range(-1,2): 
                    res += check(input, i, j, x, y, "M")
print(res)
