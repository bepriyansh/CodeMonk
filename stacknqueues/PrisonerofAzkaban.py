'''
Monk and Prisoner of Azkaban

Monk's wizard friend Harry Potter is excited to see his Dad fight Dementors
and rescue him and his Godfather Sirius Black. 
Meanwhile their friend Hermoine is stuck on some silly arrays problem. 
Harry does not have time for all this, 
so he asked Monk to solve that problem for Hermoine, so that they can go.


The problem is given an array A having N integers, for each i (1 ≤ i ≤ N), 
find x + y, where x is the largest number less than i such that A[x] > A[i] 
and y is the smallest number greater than i such that A[y] > A[i]. 
If there is no i such that A[x] > A[i], then take x = 1. Similarly, 
if there is no y > i such that A[y] > A[i], then take y = -1.

Input Format:
First line consists of a single integer denoting N.
Second line consists of N space separated integers denoting the array A.

Output Format:
Print N space separated integers, denoting +y for each i (1 ≤ i ≤ N)
Constraints:
1 ≤ N ≤ 10^6
1 ≤ A[i] < 10^18
'''

n = int(input())
arr = list(map(int, input().split()))

stk, x, y = [], [], []

for i in range(n):
    if len(stk) == 0:
        x.append(-1)
        stk.append((arr[i], i+1))
    elif stk[-1][0] > arr[i]:
        x.append(stk[-1][1])
        stk.append((arr[i], i+1))
    else:
        while len(stk) > 0 and stk[-1][0] <= arr[i]:
            stk.pop()
        if len(stk) == 0:
            x.append(-1)
            stk.append((arr[i], i+1))
        else:
            x.append(stk[-1][1])
            stk.append((arr[i], i+1))

stk = []
for i in range(n-1, -1, -1):
    if len(stk) == 0:
        y.append(-1)
        stk.append((arr[i], i+1))
    elif stk[-1][0] > arr[i]:
        y.append(stk[-1][1])
        stk.append((arr[i], i+1))
    else:
        while len(stk) > 0 and stk[-1][0] <= arr[i]:
            stk.pop()
        if len(stk) == 0:
            y.append(-1)
            stk.append((arr[i], i+1))
        else:
            y.append(stk[-1][1])
            stk.append((arr[i], i+1))

for i in range(n):
    print(x[i]+y[n-i-1], end=" ")