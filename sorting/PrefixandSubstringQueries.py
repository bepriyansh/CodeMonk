'''
Question:

You are given a string S of length N and Q queries. The queries are of three types:

1 c: Append the character c to the end of the string S.

2 x y: Consider the suffixes of equal length ending at x and y. i.e. consider substrings S[a, x] and S[b, y] and x - a + 1 = y - b + 1 = p. 
       Find the maximum value of p such that S[a, x] = S[b, y] = S[1, p]. More formally, this can be stated as to find the longest prefix S[1, p] such that the suffixes of length p ending at x and y match.

3 p l r : Consider the prefix of the string S[1, p]. 
          Now consider all substrings S[x, y] such that L <= x <= y <= R. 
          Count the number of substrings S[x, y] which match with S[1, p].(i.e. S[1, p] = S[x, y]).

Input Format:

First line: Two space-separated integers N and Q.
Second line: A string S of length N.
Next Q lines: Each line contains a query of one of the three types described above.
Output Format:

Print the answer for each query of type 2 and 3.

Constraints:

1 ≤ N ≤ 100000
1 ≤ Q ≤ 200000
S contains only lowercase English alphabets
'a' ≤ c ≤ 'z'
1 ≤ x, y ≤ current length of string
1 ≤ p ≤ current length of string
1 + p - 1 ≤ r ≤ current length of string
'''

# n,q = map(int, input().split())
# S = input()
# for _ in range(q):
#     query = input().split()
#     if query[0] == '1':
#         S += query[1]
#     elif query[0] == '2':
#         x,y = int(query[1]),int(query[2])     
#     else:
#         p,l,r = int(query[1]),int(query[2]),int(query[3])
        