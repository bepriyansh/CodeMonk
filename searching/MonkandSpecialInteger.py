'''
Question:

Monk and his friend Micro found an injured array A of N integers. 
The array was missing its special integer K, 
which is an integer such that no subarray of size K has a sum greater than X.

Monk wants to gift the array the maximum possible value of K to calm it down. 
Micro needs your help to find this value.

Input Format:

First line: Two space-separated integers N and X.
Second line: N space-separated integers, the elements of the array A.
Output Format:

Print the maximum possible value of the special integer K.

Constraints:

1 ≤ N ≤ 10^5
1 ≤ X ≤ 10^18
1 ≤ A[i] < min(X, 10^9)
'''

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
