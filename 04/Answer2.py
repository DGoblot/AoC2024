input_file = open("input.txt", "r")
input = input_file.readlines()
res = 0

def in_matrix(input, i, j):
    if i-1 >= 0 and i+1 < len(input) and j-1 >= 0 and j+1 < len(input[i]):
        return True
    else:
        return False

def check_diag_1(input, i, j):
    i -= 1
    j -= 1
    match input[i][j]:
        case "M":
            i += 2
            j += 2
            if input[i][j] == "S":
                return True 
        case "S":
            i += 2
            j += 2
            if input[i][j] == "M":
                return True
    return False

def check_diag_2(input, i, j):
    i -= 1
    j += 1
    match input[i][j]:
        case "M":
            i += 2
            j -= 2
            if input[i][j] == "S":
                return True 
        case "S":
            i += 2
            j -= 2
            if input[i][j] == "M":
                return True
    return False

for i in range(len(input)):
    for j in range(len(input[i])):
        if in_matrix(input, i, j):
            if input[i][j] == "A":
                if check_diag_1(input, i, j) and check_diag_2(input, i, j):
                    res += 1

print(res)
