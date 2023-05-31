
def b2750():
    a = int(input())
    ary = []
    for i in range(0,a):
        ary.append(int(input()))
    ary.sort()

    for i in range(a):
        print(ary[i])


def b2587():
    ary = []
    sum = 0
    for i in range(0, 5):
        ary.append(int(input()))
        sum+=ary[i]
    ary.sort()
    print(sum//5)
    print(ary[len(ary) // 2])

def b25305():
    n,k = map(int,input().split())

    ary = list(map(int,input().split()))
    ary.sort(reverse=True)
    print(ary[k-1])

def b2751(): # 버블정렬
    a = int(input())
    ary = []
    for i in range(0, a):
        ary.append(int(input()))

    for i in range(len(ary) - 1, 0, -1):
        for j in range(i):
            if ary[j] > ary[j + 1]:
                ary[j], ary[j + 1] = ary[j + 1], ary[j]
    for i in range(a):
        print(ary[i])

def b1427():
    ary = list(map(int,input()))
    ary.sort(reverse=True)
    for i in range(len(ary)):
        print(ary[i],end="")

def b11650():
    n = int(input())
    ary = []
    for i in range(n):
        ary.append(list(map(int,input().split())))
    ary.sort(key=lambda x: (x[0], x[1]))

    for i in range(n):
       print(ary[i][0],ary[i][1])

b11650()