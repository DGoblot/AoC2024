import math


input_file = open("input.txt", "r")
input = input_file.readlines()
res = 0
before = []
after = []
orders = []

# Put the different parts of the input into arrays
for line in input:
    line = line.strip()
    if "|" in line:
        before.append(line[:line.index("|")])
        after.append(line[line.index("|")+1:])
    elif "," in line:
        orders.append(line.split(","))


# Function so sort an order based on the input instructions
def sort(order):
    for i in range(len(order)):
        for j in range(len(order[i+1:])):
            for t in range(len(before)):
                if order[i] == after[t] and order[i+j+1] == before[t]:
                    temp = order[i]
                    order[i] = order[i+j+1]
                    order[i+j+1] = temp

    return order

for order in orders: # For every order
    test = True # Checks if order is sorted
    for j in range(len(order)-1): # For every number in the order
        for k in range(len(order[j+1:])): # For every other remaining numbers
            for t in range(len(before)): # We loop through the input instructions
                if order[j] == after[t] and order[k+j+1] == before[t]: # And check if we detect an error in the order 
                                                                       # (It should be before|after and we check if it's after|before)
                    test = False # If an error is detected, we break out of the order loop
                    order = sort(order) # We sort the order
                    res += int(order[math.floor(len(order)/2)]) # And finally add to res
                    break
            if not test:
                break
        if not test:
            break       

print(res)
