input = [1, 2, 3, 4, 6]
target = 6
result = []
isBreak = False

for i in input:
    if isBreak:
        break
    else:
        for a in input:
            if i + a == target:
                result.append(i)
                result.append(a)
                isBreak = True
                break

print(result)