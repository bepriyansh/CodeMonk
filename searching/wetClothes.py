def linsearch(nums, t, s):
    n = len(nums)
    cnt = 0
    if s >= n:
        return 0
    for i in range(s,n):
        if nums[i] <= t:
            cnt += 1
        else:
            break
    return cnt

def solve():
    n, m, g = map(int, input().split())
    rain = list(map(int, input().split()))
    drytime = list(map(int, input().split()))

    durs = []
    last = 0
    for t in rain:
        durs.append(t-last)
        last = t
    durs.sort(reverse=True)
    drytime.sort()
    ans = 0
    s = 0
    for i in range(g):
        if i >= len(durs):
            break
        cnt = linsearch(drytime, durs[i], s)
        s += cnt
        ans += cnt
    print(ans)
    
solve()