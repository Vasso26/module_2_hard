import random

first = random.randint(3, 20)

second = ''
print(first)
for i in range(1, first):
    for j in range(i, first):
        if first % (i + j) == 0:
            if str(j) == str(i):
                continue
            second = second + str(i) + str(j)
print(second)