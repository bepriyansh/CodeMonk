'''
Question:

Monk and his friend Micro are on a quest to find the answer to Life, Universe, and Everything. 
To complete this quest, they need to answer Q queries on an array A of N integers. 
The queries can be of two types:

0 x: Find the number of numbers in A that are not less than x.
1 x: Find the number of numbers in A that are greater than x.
Input Format:

First line: An integer N, the size of the array A.
Second line: N space-separated integers, the elements of the array A.
Third line: An integer Q, the number of queries.
Next Q lines: Each line contains a query of the form "0 x" or "1 x".
Output Format:

For each query, print the answer on a new line.

Constraints:

1 ≤ N ≤ 10^5
1 ≤ Q ≤ 3 * 10^5
1 ≤ A[i], x ≤ 10^9
'''


def lower(nums, k):
    l,r = 0, len(nums)
    while l < r:
        m = (l+r)//2
        if nums[m] < k:
            l = m + 1
        else:
            r = m
    return l

def upper(nums, k):
    l,r = 0, len(nums)
    while l < r:
        m = (l+r)//2
        if nums[m] <= k:
            l = m + 1
        else:
            r = m
    return l

n = int(input())
A = list(map(int, input().split()))
q = int(input())

A.sort()

for i in range(q):
    t, x = map(int, input().split())
    if t == 0:
        print(n - lower(A, x))
    else:
        print(n - upper(A, x))
