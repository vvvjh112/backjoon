import sys
def b10815():
    a = int(sys.stdin.readline())
    sang = list(map(int,sys.stdin.readline().split()))
    b = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))

    dic = {}
    for i in sang:
        dic[i]=1

    for i in lst:
        if i in dic.keys():
            print(dic[i],end = " ")
        else:
            print(0,end=" ")


def b14425():
    a,b = map(int,sys.stdin.readline().split())
    dic = {}
    sum = 0
    for i in range(a):
        temp = sys.stdin.readline()
        dic[temp] = 1

    for i in range(b):
        temp = sys.stdin.readline()
        if temp in dic.keys():
            sum+=1

    print (sum)

def b7785():
    a = int(sys.stdin.readline())
    dic={}
    for i in range(a):
        temp = list(map(str,sys.stdin.readline().split()))
        if temp[1] == "enter":
            dic[temp[0]] = 1
        else:
            dic.pop(temp[0])

    keys = list(dic.keys())
    keys.sort(reverse=True)
    for i in keys:
        print(i)


def b1620():
    a,b = map(int,sys.stdin.readline().split())
    dic={}
    for i in range(a):
        temp = sys.stdin.readline().rstrip()
        dic[temp] = i+1
        temp1 = str(i+1)
        dic[temp1] = temp

    lst=[]
    for i in range(b):
        lst.append(sys.stdin.readline().rstrip())
    for i in lst:
        print(dic[i])


def b10816():
    a = int(sys.stdin.readline())
    sang = list(map(int, sys.stdin.readline().split()))
    b = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))

    dic = {}
    for i in sang:
        if i not in dic.keys():
            dic[i] = 1
        else:
            dic[i] = dic[i]+1

    for i in lst:
        if i in dic.keys():
            print(dic[i], end=" ")
        else:
            print(0, end=" ")


def b1764():
    a, b = map(int, sys.stdin.readline().split())
    dic={}
    lst = []
    for i in range(a):
        temp = sys.stdin.readline().rstrip()
        dic[temp] = 1
    for j in range(b):
        temp = sys.stdin.readline().rstrip()
        if temp in dic.keys():
            lst.append(temp)
    lst.sort()
    print(len(lst))
    for i in range(len(lst)):
        print(lst[i])

def b1269():
    a, b = map(int, sys.stdin.readline().split())
    lst1 = set(map(int,sys.stdin.readline().split()))
    lst2 = set(map(int, sys.stdin.readline().split()))

    print (len(lst1-lst2)+ len(lst2-lst1))

def b11478():
    a = sys.stdin.readline().rstrip()
    leng = len(a)
    dic={}
    cnt = 0
    for i in range(leng):
        for j in range(i+1,leng+1):
            temp = a[i:j]
            if (temp not in dic.keys()):
                dic[temp] = 1
                cnt+=1

    print(cnt)


b11478()