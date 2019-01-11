with open('day5.txt') as f:
    lines = f.readlines()
    data = [int(i) for i in lines]
print(data)
#data = [0, 3, 0, 1, -3]
end = len(data)
start = 0
point = 0
count = 0
while point >= start and point < end:
    if data[point] <= 2:
        data[point] += 1
        point += data[point]
        point -= 1
        count += 1
    else:
        data[point] -= 1
        point += data[point]
        point += 1
        count += 1
#    print(data)
#print('Part1: ', count)
print('Part2:' , count)



