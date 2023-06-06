import sys
import math
from fractions import Fraction

def b1934():
    a = int(sys.stdin.readline())
    lst = []
    for i in range(a):
        lst.append(list(map(int,sys.stdin.readline().split())))

    for i in range(len(lst)):
        print(math.lcm(lst[i][0], lst[i][1]))


def b13241():
    a,b= map(int,sys.stdin.readline().split())

    print(math.lcm(a, b))

def b1735():
    a,b = map(int,sys.stdin.readline().split())
    c,d = map(int,sys.stdin.readline().split())
    temp = Fraction(a,b)+Fraction(c,d)
    print("{} {}".format(temp.numerator,temp.denominator))

def b2485():        # 중간에 보고함
    N = int(sys.stdin.readline())
    a = int(sys.stdin.readline())

    arr = []

    # 가로수들 사이의 간격 저장
    for i in range(N - 1):
        num = int(sys.stdin.readline())
        arr.append(num - a)
        a = num

    # arr에 들어있는 모든 수들의 최대공약수 찾기
    g = arr[0]
    for j in range(1, len(arr)):
        g = math.gcd(g, arr[j])

    # 둘 사이에 심을 가로수 개수: 간격 // 최대공약수 - 1
    result = 0
    for each in arr:
        result += each // g - 1
    print(result)




b1735()