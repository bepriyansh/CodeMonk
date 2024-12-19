'''
Question:

We have m wet clothes drying under the sun. 
There are n rain periods at times t1, t2, ..., tn. After each rain, all clothes become wet again. 
Each cloth i takes ai seconds to dry completely. 
We can collect all dry clothes at any time, but we can only do this at most g times.

Task:

Find the maximum number of clothes we can collect until time tn.

Input Format:

First line: Three integers n, m, g (2 ≤ n ≤ 100, 1 ≤ m, g ≤ 100).
Second line: n increasing integers t1, t2, ..., tn (0 < t1 < ... < tn ≤ 10^4).
Third line: m integers a1, a2, ..., am (1 ≤ ai ≤ 10000).
Output Format:

Print the maximum number of clothes we can collect.
'''


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