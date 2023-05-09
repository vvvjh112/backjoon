import sys
def b2798():
    n,m = map(int,input().split())
    lst = list(map(int,input().split()))
    sum=[]


    for i in range(len(lst)-2):
       for j in range(i+1,len(lst)-1):
           for k in range(j+1,len(lst)):
               if lst[i]+lst[j]+lst[k]>m:
                   continue
               else:
                   sum.append(lst[i]+lst[j]+lst[k])

    print(max(sum))

def b2231():
    n = int(input())

    for i in range(1,n+1):
       temp = list(str(i))
       sum = 0
       for j in range(0,len(temp)):
           sum += int(temp[j])
       sum += i
       if (sum == n):
           print(i)
           break
       if(i == n):
           print(0)
           break



def b19532():
    input = sys.stdin.readline

    a,b,c,d,e,f = map(int,input().split())

    for i in range(-999,1000):
       for j in range(-999,1000):
           if a*i + b*j == c and d*i + e*j == f:
               print(i,j)



# 1018 <체스판 다시 칠하기> 다시
def b1018():
    N, M = map(int, input().split())
    original = []
    count = []

    for _ in range(N):
        original.append(input())

    for a in range(N - 7):
        for b in range(M - 7):
            index1 = 0
            index2 = 0
            for i in range(a, a + 8):
                for j in range(b, b + 8):
                    if (i + j) % 2 == 0:
                        if original[i][j] != 'W':
                            index1 += 1
                        if original[i][j] != 'B':
                            index2 += 1
                    else:
                        if original[i][j] != 'B':
                            index1 += 1
                        if original[i][j] != 'W':
                            index2 += 1
            count.append(min(index1, index2))

    print(min(count))


b1018()
