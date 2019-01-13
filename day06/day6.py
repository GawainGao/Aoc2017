#5	1	10	0	1	7	13	14	3	12	8	10	7	12	0	6
from collections import defaultdict

def patternData(data):
    s = ''
    for i in range(len(data)):
        s += chr(data[i] + 65) 
    print('ss:', s)
    return s 
    
#data = [5, 1, 10, 0, 1, 7, 13, 14, 3, 12, 8, 10, 7, 12, 0 ,6] 
data = [1, 1, 14, 13, 12, 11, 10, 9, 8, 7, 7, 5, 5, 3, 3, 0]
#data = [0, 2, 7, 0]
d = defaultdict(int) 
ss = patternData(data)
time = 0
print(data)
while d[ss] == 0:
    time += 1
    d[ss] += 1
    ind = data.index(max(data))
    num = data[ind]
    data[ind] = 0
    for i in range(num):
        pos = (ind + i + 1) % len(data)
        #print(pos)
        data[pos] += 1
    print(data)
    ss = patternData(data)
#print(data)
print(time)
