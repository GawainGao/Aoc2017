i = 325489
def find(di):
    for n in range(600):
        if n*n > di:
            return n
print(find(i))
#571
print('Part1: ', - i + (find(i)*find(i)))
T = 1000
map = [[0 for i in range(T)] for j in range(T)]
startx, starty = T//2, T//2

arrow = {0:(0,-1), 1:(-1,0), 2:(0,1), 3:(1,0)} #right #up #left #down
go = {0:(1,0), 1:(0,-1), 2:(-1,0), 3:(0,1)}

print(arrow[0])
def hasLeft(x,y,d):
    dx, dy = arrow[d]
    if map[x+dx][y+dy] == 0:
        return False
    else:
        return True
def sum8(x,y):
    s = 0
    for i in {-1,0,1}:
        for j in {-1,0,1}:
            if i ==0 and j == 0:
                pass
            else:
                s += map[x+i][y+j]
    return s

map[startx][starty] = 1
map[startx+1][starty] = 1
map[startx+1][starty-1] = 2
map[startx][starty-1] = 4
t = 4
x, y = startx, starty - 1
arr = 2
while i > map[x][y]:
    if hasLeft(x,y,arr):
        pass
    else:
        arr = (arr + 1) % 4
    dx, dy = go[arr]
    x += dx
    y += dy
    map[x][y] = sum8(x,y)
    t += 1
    #print(map[x][y], t)
print(map[x][y])
#print(map)
