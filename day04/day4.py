count = 0
def sortWord(w):
    l = list(w)
    l.sort()
    return "".join(l)
    
with open('day4.txt') as f:
    lines = f.readlines()
    for line in lines:
        flag = True
        words = [sortWord(word) for word in line.split()]
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if words[i] == words[j]:
                    flag = False
        if flag:
            count += 1
                
#print('Part1: ', count) #Part2 has change some of the code
print('Part2: ', count) 
