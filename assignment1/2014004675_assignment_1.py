global a,b
a=0
b=0
sh = 0
time  = 0
def first_floor():
    global a,b
    path = 'first_floor_input.txt'
    (start,key,end,t) = read(path)
    #print(start,key,end)
    #print(a,b)
    (sh1,time1,path1) = bfs(start,key,t)
    (sh2, time2, path2) = bfs(key,end,t)
    sh = sh1 + sh2
    time = time1 + time2
    for i in range(len(path1)):
        t[path1[i][0]][path1[i][1]] = 5
    for i in range(len(path2)):
        t[path2[i][0]][path2[i][1]] = 5
    t[start[0]][start[1]] = 3
    t[end[0]][end[1]] = 4
    f = open("first_floor_output.txt",'w')
    for i in range(a):
        for j in range(b):
            f.write(str(t[i][j]))
            f.write(" ")
        f.write('\n')
    #f.write(time)
    f.write("---\n")
    f.write("length : ")
    f.write(str(sh))
    f.write("\n")
    f.write("time : ")
    f.write(str(time))
    f.write("\n")
    f.close()

def second_floor():
    global a,b
    path = 'second_floor_input.txt'
    (start,key,end,t) = read(path)
    print(start,key,end)
    print(a,b)
    (sh1,time1,path1) = dfs(start,key,t)
    (sh2, time2, path2) = dfs(key,end,t)
    sh = sh1 + sh2
    time = time1 + time2
    for i in range(len(path1)):
        t[path1[i][0]][path1[i][1]] = 5
    for i in range(len(path2)):
        t[path2[i][0]][path2[i][1]] = 5
    t[start[0]][start[1]] = 3
    t[end[0]][end[1]] = 4
    f = open("second_floor_output.txt",'w')
    for i in range(a):
        for j in range(b):
            f.write(str(t[i][j]))
            f.write(" ")
        f.write('\n')
    #f.write(time)
    f.write("---\n")
    f.write("length : ")
    f.write(str(sh))
    f.write("\n")
    f.write("time : ")
    f.write(str(time))
    f.write("\n")
    f.close()

def third_floor():
    global a,b
    path = 'third_floor_input.txt'
    (start,key,end,t) = read(path)
    #print(start,key,end)
    #print(a,b)
    (sh1,time1,path1) = bfs(start,key,t)
    (sh2, time2, path2) = bfs(key,end,t)
    sh = sh1 + sh2
    time = time1 + time2
    for i in range(len(path1)):
        t[path1[i][0]][path1[i][1]] = 5
    for i in range(len(path2)):
        t[path2[i][0]][path2[i][1]] = 5
    t[start[0]][start[1]] = 3
    t[end[0]][end[1]] = 4
    f = open("third_floor_output.txt",'w')
    for i in range(a):
        for j in range(b):
            f.write(str(t[i][j]))
            f.write(" ")
        f.write('\n')
    #f.write(time)
    f.write("---\n")
    f.write("length : ")
    f.write(str(sh))
    f.write("\n")
    f.write("time : ")
    f.write(str(time))
    f.write("\n")
    f.close()

def fourth_floor():
    global a,b
    path = 'fourth_floor_input.txt'
    (start,key,end,t) = read(path)
    #print(start,key,end)
    #print(a,b)
    (sh1,time1,path1) = dfs(start,key,t)
    (sh2, time2, path2) = dfs(key,end,t)
    sh = sh1 + sh2
    time = time1 + time2
    for i in range(len(path1)):
        t[path1[i][0]][path1[i][1]] = 5
    for i in range(len(path2)):
        t[path2[i][0]][path2[i][1]] = 5
    t[start[0]][start[1]] = 3
    t[end[0]][end[1]] = 4
    f = open("fourth_floor_output.txt",'w')
    for i in range(a):
        for j in range(b):
            f.write(str(t[i][j]))
            f.write(" ")
        f.write('\n')
    #f.write(time)
    f.write("---\n")
    f.write("length : ")
    f.write(str(sh))
    f.write("\n")
    f.write("time : ")
    f.write(str(time))
    f.write("\n")
    f.close()

def fifth_floor():
    global a,b
    path = 'fifth_floor_input.txt'
    (start,key,end,t) = read(path)
    #print(start,key,end)
    #print(a,b)
    (sh1,time1,path1) = dfs(start,key,t)
    (sh2, time2, path2) = dfs(key,end,t)
    sh = sh1 + sh2
    time = time1 + time2
    for i in range(len(path1)):
        t[path1[i][0]][path1[i][1]] = 5
    for i in range(len(path2)):
        t[path2[i][0]][path2[i][1]] = 5
    t[start[0]][start[1]] = 3
    t[end[0]][end[1]] = 4
    f = open("fifth_floor_output.txt",'w')
    for i in range(a):
        for j in range(b):
            f.write(str(t[i][j]))
            f.write(" ")
        f.write('\n')
    #f.write(time)
    f.write("---\n")
    f.write("length : ")
    f.write(str(sh))
    f.write("\n")
    f.write("time : ")
    f.write(str(time))
    f.write("\n")
    f.close()


def read(path):
    global a,b
    f = open(path)
    line = f.readline()
    lst = []
    t = []
    key = []
    start = 0
    escape = 0
    #print(line)
    index1 = 0
    index2 = line.find(" ") + 1
    index3 = line.find(" ", index2 + 1)
    #print(index1, index2, index3)
    n = int(line[index1:index2])
    a = int(line[index2:index3])
    b = int(line[index3:-1])
    for i in range(a):
        line = f.readline()
        lst = []
        for j in range(b):
            c = int(line[2 * j])
            if (c == 3):
                start = [i, j]
            if (c == 6):
                key = [i, j]
            if (c == 4):
                escape = [i, j]
            lst.append(c)
        t.append(lst)
    f.close()
    return (start,key,escape,t)

'''f = open('fifth_floor.txt')
line = f.readline()
lst= []
t = []
key = []
start = 0
escape = 0
print(line)
index1 = 0
index2 = line.find(" ") +1
index3 = line.find(" ",index2+1)
print(index1,index2,index3)
n = int(line[index1:index2])
a = int(line[index2:index3])
b = int(line[index3:-1])
for i in range(a):
    line = f.readline()
    lst =[]
    for j in range(b):
        c = int(line[2*j])
        if (c == 3):
            start = [i,j]
        if (c == 6):
            key = [i,j]
        if(c == 4):
            escape = [i,j]
        lst.append(c)
    t.append(lst)
print(start,escape,key)
print(t[0])
print(escape[0])'''
def bfs(start,end,map):
    global a,b,path
    visited = []
    queue = []
    parent = [[start for i in range(a)] for j in range(b)]
    start.append(0)
    queue.append(start)
    #print(start,queue)
    time = 0
    found = False
    while queue:
        n = queue.pop(0)
     #   print(n)
        if(n[0:2] == end):
            found = True
            break
        time += 1
        if n not in visited:
            visited.append(n[0:2])
        if (n[0]-1 >= 0) and [n[0]-1,n[1]] not in visited and map[n[0]-1][n[1]] != 1:
            queue.append([n[0]-1,n[1],n[2]+1])
            parent[n[0]-1][n[1]] = n[0:2]
        if (n[0]+1 < a) and [n[0]+1,n[1]] not in visited and map[n[0]+1][n[1]] != 1:
            queue.append([n[0]+1,n[1],n[2]+1])
            parent[n[0] + 1][n[1]] = n[0:2]
        if (n[1]-1 >= 0) and [n[0],n[1]-1] not in visited and map[n[0]][n[1]-1] != 1:
            queue.append([n[0],n[1]-1,n[2]+1])
            parent[n[0]][n[1]-1] = n[0:2]
        if (n[1]+1 < b) and [n[0],n[1]+1] not in visited and map[n[0]][n[1]+1] != 1:
            queue.append([n[0],n[1]+1,n[2]+1])
            parent[n[0]][n[1]+1] = n[0:2]
    #print(n[2],time)
    path = []
    if found:
        p = end
        #print(p)
        while p != start:
            path.append(p)
            p = parent[p[0]][p[1]]
            #print(p)
        path.append(p)
        #print(path,len(path))
    #print(len(path))
    #print(n[2],time)
    return (n[2],time,path)

def dfs(start,end,map):
    global a,b,path
    visited = []
    queue = []
    parent = [[start for i in range(a)] for j in range(b)]
    start.append(0)
    queue.append(start)
    #print(start,queue)
    time = 0
    found = False
    while queue:
        n = queue.pop()
     #   print(n)
        if(n[0:2] == end):
            found = True
            break
        time += 1
        if n not in visited:
            visited.append(n[0:2])
        if (n[0]-1 >= 0) and [n[0]-1,n[1]] not in visited and map[n[0]-1][n[1]] != 1:
            queue.append([n[0]-1,n[1],n[2]+1])
            parent[n[0]-1][n[1]] = n[0:2]
        if (n[0]+1 < a) and [n[0]+1,n[1]] not in visited and map[n[0]+1][n[1]] != 1:
            queue.append([n[0]+1,n[1],n[2]+1])
            parent[n[0] + 1][n[1]] = n[0:2]
        if (n[1]-1 >= 0) and [n[0],n[1]-1] not in visited and map[n[0]][n[1]-1] != 1:
            queue.append([n[0],n[1]-1,n[2]+1])
            parent[n[0]][n[1]-1] = n[0:2]
        if (n[1]+1 < b) and [n[0],n[1]+1] not in visited and map[n[0]][n[1]+1] != 1:
            queue.append([n[0],n[1]+1,n[2]+1])
            parent[n[0]][n[1]+1] = n[0:2]
    #print(n[2],time)
    path = []
    if found:
        p = end
        #print(p)
        while p != start:
            path.append(p)
            p = parent[p[0]][p[1]]
            #print(p)
        path.append(p)
        #print(path,len(path))
    #print(len(path))
    #print(n[2],time)
    return (n[2],time,path)


#bfs(start,key,t)
#bfs(start,escape,t)
first_floor()
second_floor()
third_floor()
fourth_floor()
fifth_floor()