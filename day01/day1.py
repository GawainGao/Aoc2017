print('Hello')

with open('day1.txt') as f:
    input = f.readline().strip()

print(input)
s = 0
for i in range(len(input)):
    if i == 0:
        if input[0] == input[-1]:
            s += int(input[0])
    else:
        if input[i] == input[i-1]:
            s += int(input[i])

print('Part1: ', s)

print(len(input))
half = len(input) // 2
print(half)
s2 = 0
for i in range(half):
    if input[i] == input[i + half]:
        s2 += int(input[i])

print('Part2: ', s2 * 2)
