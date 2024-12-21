'''
Monk and Divisor Conundrum

Here is another task for you, prepared by Monk himself. So, this is how it goes:
Given an integer array A of size N, Monk needs you to answer T queries for him. 
In each query, he gives you 2 integers Pand Q. In response to each of these queries, 
you need to tell Monk the count of numbers in array A. that are either divisible by P, Q, or both.
Can you cope with this?

Input Format:
The first line contains a single integer N denoting the size of array A. 
The next line contains N space separated integers, where the ith integer denotes A[i].
The next line contains a single integer T denoting the number of queries Monk poses to you. 
Each of the next T lines contains 2 space separated integers Pand Q.

Output Format:
For each query, print the answer on a new line.

Constraints:
1 <= N <= 2 * 10 ^ 5
1 <= A[i] <= 2 * 10 ^ 5
1 <= T <= 2 * 10 ^ 5
1 <= P, Q <= 2 * 10 ^ 5
'''

'''
# Brute Force

n = int(input())
nums = list(map(int, input().split()))
t = int(input())

def count():
    p,q = map(int, input().split())
    cnt = 0
    for i in range(n):
        if nums[i]%p == 0 and nums[i]%q == 0:
            cnt += 1
        elif nums[i]%p == 0 or nums[i]%q == 0:
            cnt += 1
    return cnt

res = [count() for _ in range(t)]
print('\n'.join(map(str,res)))
'''

def gcd(a,b):
    while b:
        a, b = b, a % b
    return a

def lcm(a,b):
    return (a*b)//gcd(a,b)

n = int(input())
nums = list(map(int, input().split()))
maxi = max(nums)

freq, div = [0]*(maxi+1), [0]*(maxi+1)

for num in nums:
    freq[num] += 1

for i in range(1, maxi + 1):
    for fact in range(i, maxi + 1, i): # this will give : [i, 2i, 3i, 4i, .....]
        # div[i] is the count of numbers that are divisible by i
        div[i] += freq[fact]  

def count():
    p,q = map(int, input().split())
    pq = lcm(p,q)

    a = div[p] if p <= maxi else 0
    b = div[q] if q <= maxi else 0
    ab = div[pq] if pq <= maxi else 0

    return a + b - ab

res = [count() for _ in range(int(input()))]
print('\n'.join(map(str, res)))