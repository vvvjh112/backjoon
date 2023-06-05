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


b10815()