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


def solve():
    n,m,g = input().split()
    t = list(map(int,input().split()))
    dt = list(map(int,input().split()))

    gap =[]
    for i in range(len(t)-1):
        x = t[i+1]-t[i]
        gap.append(x)
        
    m = max(gap)
    c=0
    for i in range(len(dt)):
        if dt[i]<=m:
            c+=1
    print(c)
    
solve()