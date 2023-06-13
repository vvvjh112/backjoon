import sys
from collections import deque
def b18258():
    n = int(sys.stdin.readline())
    result=[]
    queue = deque([])
    for i in range(n):
        temp = list(sys.stdin.readline().split())
        if len(temp)==2:
            queue.append(temp[1])
        elif temp[0]=="pop":
            if len(queue) == 0:
                result.append(-1)
            else:
                result.append(queue.popleft())
        elif temp[0]=="size":
            result.append(len(queue))
        elif temp[0]=="empty":
            if len(queue) == 0:
                result.append(1)
            else:
                result.append(0)
        elif temp[0]=="front":
            if (len(queue) == 0):
                result.append(-1)
            else:
                result.append(queue[0])
        elif temp[0] == "back":
            if (len(queue) == 0):
                result.append(-1)
            else:
                result.append(queue[-1])

    for i in range(len(result)):
        print(result[i])


def b2164():
    a = int(sys.stdin.readline())
    queue = deque([])
    for i in range(1,a+1):
        queue.append(i)

    while(len(queue)!=1):
        queue.popleft()
        temp = queue.popleft()
        queue.append(temp)

    print(queue.pop())

def b11866():
    a,b = map(int,sys.stdin.readline().split())
    queue = deque([])
    result=[]
    for i in range(1,a+1):
        queue.append(i)

    while (len(queue)!=0):
        for i in range(b-1):
            queue.append(queue.popleft())
        result.append(queue.popleft())
    print("<",end="")
    for i in result:
        if i == result[-1]:
            print(result[-1],end="")
            print(">")
        else:
            print(i, end=", ")


def b1966():
    a = int(sys.stdin.readline())

    result = []
    for i in range(a):
        queue = deque([])
        temp, target = map(int,sys.stdin.readline().split())
        lst = list(map(int,sys.stdin.readline().split()))
        rank = deque(lst)
        for j in range(temp):
            queue.append(j)

        cnt=0

        while(True):

            if(queue[0]==target)and(rank[0]==max(rank)):
                cnt +=1
                break

            if rank[0] == max(rank):
                queue.popleft()
                rank.popleft()
                cnt += 1
            else:
                queue.append(queue.popleft())
                rank.append(rank.popleft())

        result.append(cnt)

    for i in result:
        print(i)

b1966()

