import sys
import math
def b1934():
    a = int(sys.stdin.readline())
    lst = []
    for i in range(a):
        lst.append(list(map(int,sys.stdin.readline().split())))

    for i in range(len(lst)):
        print(math.lcm(lst[i][0], lst[i][1]))

b1934()