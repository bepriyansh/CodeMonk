# Medium Problem

t = int(input())
while t != 0:
    t -= 1

    n, k = map(int, input().split())
    A = input()

    maxInd, period = 0, -1
    maxi = ""
    for i in range(n):
        if maxi > A :
            maxi = A
            maxInd = i
        elif maxi == A:
            period = maxInd - i
            break
        A = A[1:] + A[:1] #shift by 1
    
    if period != -1:
        print(maxInd + (k-1) * period)
    else :
        print(maxInd + (k-1) * n)
    