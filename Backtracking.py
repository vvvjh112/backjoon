import sys



def b15649():
    a,b = map(int,sys.stdin.readline().split())
    lst = []
    def dfs():
        if len(lst) == b:
            print(' '.join(map(str, lst)))
            return

        for i in range(1, a + 1):
            if i not in lst:
                lst.append(i)
                dfs()
                lst.pop()
    dfs()

def b15650():
    a, b = map(int, sys.stdin.readline().split())
    lst = []
    temp = []
    result = []
    def dfs():
        if len(lst) == b:
            tmp = set(' '.join(map(str, lst)))

            if tmp not in temp:
                temp.append(tmp)
                result.append(' '.join(map(str, lst)))
            return


        for i in range(1, a + 1):
            if i not in lst:
                lst.append(i)
                dfs()
                lst.pop()

    dfs()
    for i in result:
        print(i)



def b15651():
    a,b = map(int,sys.stdin.readline().split())
    lst = []
    def dfs():
        if len(lst) == b:
            print(' '.join(map(str, lst)))
            return

        for i in range(a, a + 1):
            # if i not in lst:
                lst.append(i)
                dfs()
                lst.pop()
    dfs()

def b15652():
    a,b = map(int,sys.stdin.readline().split())
    lst = []
    def dfs(s):
        if len(lst) == b:
            print(' '.join(map(str, lst)))
            return

        for i in range(s, a + 1):
            # if i not in lst:
                lst.append(i)
                dfs(i)
                lst.pop()
    dfs(1)

def b14888():
    depth = int(sys.stdin.readline())
    lst = list(map(int,sys.stdin.readline().split()))
    operator = list(map(int,(sys.stdin.readline().split())))
    temp=[]
    def dfs(dp, num, plus, minus, multi, divide):

        if dp == depth:
            if len(temp)==0:
                temp.append(max(-1000000000, num))
                temp.append(min(1000000000, num))
            else:
                temp[0] = max(temp[0],num)
                temp[1] = min(temp[1],num)
            return

        if plus:
            dfs(dp+1, num+lst[dp], plus-1,minus,multi,divide)
        if minus:
            dfs(dp+1, num-lst[dp], plus,minus-1,multi,divide)
        if multi:
            dfs(dp+1, num*lst[dp], plus,minus,multi-1,divide)
        if divide:
            dfs(dp+1, int(num/lst[dp]), plus,minus,multi,divide-1)

    dfs(1,lst[0],operator[0],operator[1],operator[2],operator[3])
    print(temp[0])
    print(temp[1])

def b14889():
    lst=[]
    n = int(sys.stdin.readline())
    for i in range(n):
        lst.append(list(map(int,sys.stdin.readline().split())))
    visit = [False for _ in range(n)]
    mini = 999999999999

    def dfs(depth, set):
        global mini
        if depth == n//2:
            a=0
            b=0
            for i in range(n):
                for j in range(n):
                    if visit[i] and visit[j]:
                        a += lst[i][j]
                    elif not visit[i] and not visit[j]:
                        b += lst[i][j]
            mini = min(mini, abs(a-b))
            return

        for i in range(set, n):
            if not visit[i]:
                visit[i] = True
                dfs(depth+1,i+1)
                visit[i]= False
    dfs(0,0)
b14889()