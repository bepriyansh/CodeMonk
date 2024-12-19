# Hard Problem

dp = {}
mod = 1000000009

def ans(n):
    if n == 0:
        return 1
    if n == 1:
        return 10
    if n in dp:
        return dp[n]

    x, y = ans(n//2), ans(n//2 - 1)

    if n%2 == 0:
        res = (x*x - y*y)%mod
    else:
        z = ans(n//2 + 1)
        res = x*(z-y)%mod


    if n < 50000000:
        dp[n] = res
        
    return res



t = int(input())
while t != 0:
    t -= 1
    
    n = int(input())
    print(ans(n))