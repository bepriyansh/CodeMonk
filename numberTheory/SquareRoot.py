'''
Monk and Square Root
Given two integers N and M, help Monk find an integer X, such that X2 % M = N and 0 ≤ X. 
If there are multiple values of X print smallest one. If there is no possible value of X print 1.
Note: Make sure you handle integer overflow.

Input:
First line consists of a single integer 7 denoting the number of test cases.
Each test case consists of a single line containing two space separated integers denoting N and M.

Output:
For each test case print the required answer.

Constraints:
1 < T < 100
0 < N < M < 10^6
'''

# Brute Force
def solve():
    n,m = map(int, input().split())

    for i in range(m):
        if (i * i)%m == n:
            return i
    return -1


res = [solve() for _ in range(int(input()))]
print('\n'.join(map(str, res)))