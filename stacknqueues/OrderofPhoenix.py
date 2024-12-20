'''
Monk and Order of Phoenix

Voldemort has a big army, so he has maintained his people in N rows to fight Harry's army. 
Each row contains the heights of the fighters and is sorted in non-decreasing order from the start to end, 
except for the first row, which may contain the heights of the fighters in any arbitary order, as it contains all the
legendry fighters. During the war, at any time, Voldemort can remove a fighter from any row, and can also add any new
fighter to any row (maintaining the non-decreasing order of heights, except in the first row).


Note:
1. Voldemort will never remove any fighter from an empty row.
2. Voldemort can only remove or add a fighter from/to the end of row.

Now Harry has a special wand which can kill exactly N fighters in one go, but with following conditions:
1. There should be exactly N fighters, and exactly one fighter (which can be anyone in the row) should be chosen from each row.
2. The first fighter can only be chosen from the first row, the second one from second row, and so on. Basically the ith fighter should be chosen from ith the row, where i ranges from 1 to N. 
3. The order of the heights of the chosen fighters should be strictly increasing.

Now Harry wants to know whether he can kill N fighters using special wand. 
As Harry is busy in fighting Voldemort, he gave this task to Monk.

Input Format:
The First line consists of a single integer N denoting the number of stacks.
In each of the next N lines, first integer X denotes the size of the stack, followed by the X space separated integers denoting the heights of the fighters in the stack.
The next lines consists of single integer Q, denoting the number operations.
Each of the next Q lines will contain a integer v, which will decide the type of operation.
1. For v = 1 extra 2 integers k and h will be given, which shows that Voldemort will add one fighter of height h in kith stack, maintaining the order of the stack, if k is not equal to 1.
2. For v = 0 1 more integer k will be given, which shows that Voldemort will remove a fighter from kith stack.
3. For v = 2 Monk needs to know whether Harry can use his special wand or not.

Output Format::
For each v = 2 print "YES" (without quotes) if Harry can use his special wand or print "NO" (without quotes).

Constraints::
1 <= N <= 10
0Xmat 10^5, where Xmax denotes the maximum size of stack, which can be reached during any operation.
1 <= Q <= 250000
1height of each fighter < 10^9
1< number of operations with (v = 2) ≤ 10^4
'''


n = int(input())
S = []
stk = []

def check():
    last = 0
    if len(stk) != 0:
        last = stk[-1]
    for i in range(1,n):
        if last >= S[i][-1]:
            return False
    return True

for _ in range(n):
    S.append(list(map(int, input().split()))[1:])

for i in range(len(S[0])):
    if len(stk) == 0:
        stk.append(S[0][i])
    else:
        stk.append(min(S[0][i], stk[-1]))

q = int(input())
for _ in range(q):
    v = list(map(int, input().split()))
    type = v[0]
    if type == 0:
        k = v[1]-1
        if len(S[k]) > 0:
            S[k].pop()
            if k == 0:
                stk.pop()
    elif type == 1:
        k, h = v[1]-1, v[2]
        S[k].append(h)
        if k == 0:
            if len(stk) == 0:
                stk.append(h)
            else:
                stk.append(min(h, stk[-1]))
    else:
        print('YES' if check() else 'NO')