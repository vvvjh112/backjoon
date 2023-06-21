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

b15652()