from collections import defaultdict
import re



lines = open('day7.txt').readlines()
#lines = open('test.txt').readlines()
F = defaultdict(list)
E = defaultdict(int)
T = defaultdict(int)
for line in lines:
    weight = re.findall(r'\d+',line)
    #print(weight)
    if '->' in line:
        a = line.split(' ')[0]
        b = line.split('->')[1][1:].strip()
        c = [word.strip() for word in b.split(',')]
        #print(a, b, c)
        for word in c:
            F[a].append(word)
            E[word] += 1
    else:
        a = line.split(' ')[0]
    T[a] = int(weight[0])
print('lenT', len(T))
print('lenE', len(E))

for t in T:
    if t not in E:
        print('Part1: ', t)


class Node:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.children = []
    def addChild(self, child):
        self.children.append(child)

def check3(t):
    flag = True
    if len(F[t]) == 0:
        return False
    for tt in F[t]:
        if len(F[tt]) == 0:
            return False
        for ttt in F[tt]:
            if len(F[ttt]) != 0:
                return False
    return True

def count(t):
    #print(t)
    d = []
    for tt in F[t]:
        s = T[tt]
        for ttt in F[tt]:
            s += T[ttt]
        #print(s)
        d.append(s)
    if max(d) != min(d):
        print(d)


for t in T:
    if check3(t):
        count(t)
            

