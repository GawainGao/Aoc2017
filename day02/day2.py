def findEvenly(s):
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] % s[j] == 0:
                return s[i] // s[j]
            elif s[j] % s[i] == 0:
                return s[j] // s[i]
            else:
                continue

sum = 0
sum2 = 0
with open('day2.txt') as f:
    lines = f.readlines()
    for line in lines:
        seti = []
        seti = [int(i) for i in line.split()]
        print(seti)
        sum += max(seti) - min(seti)
        sum2 += findEvenly(seti)
print('Part1: ', sum)
print('Part2: ', sum2)


test = [2, 5, 8]
t = findEvenly(test)
print(t)
        
        

