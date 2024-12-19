n,x = map(int, input().split())
A = list(map(int, input().split()))

def check(k):
    sum = 0
    for i in range(k):
        sum += A[i]
    if sum > x:
        return False
    
    l, r = 0, k

    while r < n:
        sum += A[r] - A[l]
        r+=1
        l+=1
        if sum > x:
            return False
    return True

k=0
l, r = 0, n
while l <= r:
    m = (l+r)//2
    if check(m):
        k=m
        l = m+1
    else:
        r = m-1
print(k)
