a = 5
for i in range(1,a+1):
    print("  "*(a-i),end="")
    for x in range(1,i+1):
        print("*",end=" ")
    print()
