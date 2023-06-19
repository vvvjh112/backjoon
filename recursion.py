import sys

def b27433(num):
    if num == 0:
        return 1
    if num == 1:
        return 1
    return num * b27433(num-1)

def b10870(num):
    if num ==0:
        return 0
    if num == 1 or num == 2:
        return 1
    else:
        return b10870(num-1)+b10870(num-2)

def recursion(s, l, r, c):
    c+=1
    if l >= r: return 1, c
    elif s[l] != s[r]: return 0, c
    else: return recursion(s, l+1, r-1, c)

def isPalindrome(s, c):
    return recursion(s, 0, len(s)-1, c)

def b25501():
    t = int(sys.stdin.readline())
    result = []
    for i in range(t):
        c = 0
        tmp = sys.stdin.readline().rstrip()
        a, b = isPalindrome(tmp, c)
        result.append([a,b])

    for i in range(t):
        print(result[i][0],result[i][1])



def b24060():
    import sys
    input = sys.stdin.readline

    def merge_sort(L):
        if len(L) == 1:
            return L

        mid = (len(L) + 1) // 2

        left = merge_sort(L[:mid])
        right = merge_sort(L[mid:])

        i, j = 0, 0
        L2 = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                L2.append(left[i])
                ans.append(left[i])
                i += 1
            else:
                L2.append(right[j])
                ans.append(right[j])
                j += 1
        while i < len(left):
            L2.append(left[i])
            ans.append(left[i])
            i += 1
        while j < len(right):
            L2.append(right[j])
            ans.append(right[j])
            j += 1

        return L2

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = []
    merge_sort(a)
    print(ans)

    if len(ans) >= k:
        print(ans[k - 1])
    else:
        print(-1)


def b4779():
    pass
