import sys
import math
def b15439():
    a = int(sys.stdin.readline())
    print(a*(a-1))

def b24723():
    print(2**int(sys.stdin.readline()))

def b10872():
    a = int(sys.stdin.readline())
    result=a
    if a==0:
        print(1)
    else:
        for i in range(a-1,a<0,-1):
            result*=i
        print(result)

def b11050():
    a,b = map(int,sys.stdin.readline().split())
    print(int(math.factorial(a)/(math.factorial(a-b)*math.factorial(b))))

def b1010():
    n = int(sys.stdin.readline())
    lst = []
    for i in range(n):
        lst.append(list(map(int,sys.stdin.readline().split())))
    for i in range(n):
        print(int(math.factorial(lst[i][1])/(math.factorial(lst[i][1]-lst[i][0])*math.factorial(lst[i][0]))))

b1010()