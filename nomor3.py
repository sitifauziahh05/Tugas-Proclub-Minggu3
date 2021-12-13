input = ["js", "js", "golang", "ruby", "ruby", "js", "js"]
result = {}

for data in input:
    if data in result:
        result[data] = result[data] + 1
    else:
        result[data] = 1

print(result)