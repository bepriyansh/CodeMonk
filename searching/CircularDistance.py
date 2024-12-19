n = int(input())
p = [list(map(int, input().split())) for i in range(n)]
q = int(input())

d = [(p[i][0]**2 + p[i][1]**2) for i in range(n)]
d.sort()

def upper(k):
    l, r = 0, n
    while l < r:
        m = (l + r) // 2
        if d[m] <= k:
            l = m + 1
        else:
            r = m  
    return l

res = []
for _ in range(q):
    r = int(input())
    print(upper(r**2))