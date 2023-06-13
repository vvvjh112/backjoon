import sys
import re

def b10828():
    n = int(sys.stdin.readline())
    stack = []
    result=[]
    for i in range(n):
        temp = list(sys.stdin.readline().split())
        if len(temp)==2:
            stack.append(temp[1])
        elif temp[0]=="top":
            if len(stack)==0:
                result.append(-1)
            else:
                result.append(stack[len(stack)-1])
        elif temp[0]=="empty":
            if (len(stack)==0):
                result.append(1)
            else:
                result.append(0)
        elif temp[0]=="size":
            result.append(len(stack))
        elif temp[0]=="pop":
            if (len(stack)==0):
                result.append(-1)
            else:
                result.append(stack[len(stack)-1])
                stack.pop(len(stack)-1)
    for i in range(len(result)):
        print(result[i])

def b10773():
    a= int(sys.stdin.readline())
    b = []
    for i in range(a):
        temp = int(sys.stdin.readline())
        if temp == 0 and len(b)!=0:
            b.pop()
        else:
            b.append(temp)

    print(sum(b))

def b9012():
    a = int(sys.stdin.readline())
    result=[]
    for i in range(a):
        result.append(list(sys.stdin.readline().rstrip()))

    for i in result:
        sum =0
        for j in range(len(i)):
            temp = i.pop()
            if temp==")":
                sum+=1
            else:
                sum-=1

            if (sum < 0):
                print("NO")
                break
        if sum==0:
            print("YES")
        elif sum>0:
            print("NO")

def b4949(): # 내가 짠거
    result = []
    while(True):
        temp = sys.stdin.readline().rstrip()
        if(temp == "."):
            break
        result.append(list(re.sub(r"[a-zA-Z\s]","",temp)))

    for i in result:
        stack = []
        for j in i:
            if j == '[' or j == '(':
                stack.append(j)
            elif j == ')':
                if len(stack) !=0 and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(')')
                    continue
            elif j == ']':
                if len(stack) !=0 and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(']')
                    continue

        if len(stack) == 0:
            print("YES")
        else:
            print("NO")

def b4949_answer():
    while True:
        a = input()
        stack = []

        if a == ".":
            break

        for i in a:
            if i == '[' or i == '(':
                stack.append(i)
            elif i == ']':
                if len(stack) != 0 and stack[-1] == '[':
                    stack.pop()  # 맞으면 지워서 stack을 비워줌 0 = yes
                else:
                    stack.append(']')
                    break
            elif i == ')':
                if len(stack) != 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(')')
                    break
        if len(stack) == 0:
            print('yes')
        else:
            print('no')

def b1874():
    a = int(sys.stdin.readline())
    lst=[]
    result = []
    temp=[]
    for i in range(a):
        lst.append(int(sys.stdin.readline()))
    tmp = sorted(lst)
    cnt = -1
    while (len(tmp)!=0):

        if cnt>len(tmp)-1:
            result=["NO"]
            break

        if tmp[cnt] == lst[0] and (len(temp)!=0 and cnt>=0):
            result.append("-")
            lst.pop(0)
            tmp.pop(cnt)
            cnt-=1

        else:
            result.append("+")
            temp.append(tmp[cnt])
            cnt+=1

    for i in range(len(result)):
        print(result[i])

b1874()