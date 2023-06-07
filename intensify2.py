import sys
from collections import Counter
def b1037():
    a = int(sys.stdin.readline())
    lst = list(map(int,sys.stdin.readline().split()))
    lst.sort()
    print(lst[0]*lst[len(lst)-1])

def b25192():
    a = int(sys.stdin.readline())
    temp = sys.stdin.readline().rstrip()
    cnt = 0
    dic = {}
    for i in range(a-1):
        temp = sys.stdin.readline().rstrip()
        if (temp == "ENTER"):
            dic.clear()
            continue
        else:
            if (temp not in dic.keys()):
                dic[temp] = 1
                cnt+=1
    print(cnt)

def b26069():
    a= int(sys.stdin.readline())
    dic = {"ChongChong":1}
    for i in range(a):
        temp = list(map(str,sys.stdin.readline().split()))
        if temp[0] in dic.keys() :
            dic[temp[1]] = 1
        if temp[1] in dic.keys():
            dic[temp[0]] = 1

    print(len(dic))

def b2108():
    a = int(sys.stdin.readline())
    lst = []

    for i in range(a):
        lst.append(int(sys.stdin.readline()))
    lst.sort()

    dic={}
    bin=[]
    for i in lst:
        if i in dic.keys():
            dic[i]+=1
        else:
            dic[i]=1
    mx = max(dic.values())
    for i in dic:
        if mx == dic[i]:
            bin.append(i)

    print(round(sum(lst)/len(lst)))
    print(lst[len(lst)//2])
    if len(bin)>1:
        print(bin[1])
    else:
        print(bin[0])

    print(max(lst)-min(lst))


def b20920():
    a,b = map(int,sys.stdin.readline().split())
    lst = []
    for i in range(a):
        temp = sys.stdin.readline().rstrip()
        if len(temp)>=b:
            lst.append(temp)
    result = Counter(lst)
    result1 = sorted(result.items(),key=lambda x: (-x[1],-len(x[0]),x[0]))

    for i in result1:
        print(i[0])

b20920()