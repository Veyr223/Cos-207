data = [3, 1, 4, 1, 5]

total = 0
for x in data:
    total = total + x * x
print("imperative :", total)

print("functional :", sum(map(lambda x: x * x, data)))

print("declarative:", sum(x * x for x in data))