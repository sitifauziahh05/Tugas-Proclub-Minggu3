x = 5
for i in range(x, 0, -1):
    for y in range(0, x -i):
        print(end = " ")
    for j in range(0, i):
        print("*", end= " ")
    print()