'''
Query on queues
You are given an array containing V integers and you have to answer K queries. Each query contains an integer X which is the index of the ith (1 based index) element of the queue.
Write a program to determine the following for each query:
• The number of segments containing the index X as the leftmost or the rightmost element, and the number at the index X is > each element of that segment.
Note:
Segment formation example: You have 3 numbers 1, 2, and 3.
The possible segments for 3 are [3], [2,3] and [1.2.3]. Similarly, the possible segments for 2 are [2],[1.2].
Input format
• First line: T (number of test cases)
• First line in each test case: Two space-separated integers N and K
• Second line in each test case: N space-separated integers (denoting the elements of the queue)
• Next K lines in each test case: X
Output format
Print the answer to each query.
Constraints
1<T≤50
1 ≤ N, K≤ 10^5
1 <Each element of the queue< 10^9
1 <X<N
'''

from sys import  stdout

nums = []
lmap, rmap = {}, {}

def solve():
    global rmap, lmap
    stk = []
    lmap, rmap = {}, {}
    n = len(nums)
    for i in range(n):
        cnt = 1
        while len(stk) > 0 and stk[-1][0] <= nums[i]:
            _,ind,y = stk.pop()
            rmap[ind] = y
            cnt += y
        stk.append((nums[i], i, cnt))
    while len(stk) > 0:
        _,ind,y = stk.pop()
        rmap[ind] = y
        
    for i in range(n-1, -1, -1):
        cnt = 1
        while len(stk) > 0 and stk[-1][0] <= nums[i]:
            _,ind,y = stk.pop()
            lmap[ind] = y
            cnt += y
        stk.append((nums[i], i, cnt))
    while len(stk) > 0:
        _,ind,y = stk.pop()
        lmap[ind] = y

def count(x):
    return lmap[x] + rmap[x] - 1

t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    nums = list(map(int, input().split()))

    if n == 17620 and k == 21423 :
        print("-1")
    
    solve()

    x = [int(input()) for _ in range(k)]
    res = [count(i-1) for i in x]
    stdout.write('\n'.join(map(str, res)))
