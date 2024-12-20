'''
Monk and Chamber of Secrets

Aragog shows them a queue of N spiders of which only X spiders are to be selected. 
Each spider has some power associated with it. There are X iterations on the queue.
In each iteration, X spiders are dequeued (if queue has less than X entries, all of them will be dequeued) 
and the one with maximum power is selected and remaining spiders are enqueued back to the queue 
(in the order they were dequeued) but their power is decreased by one unit. 
If there are multiple spiders with maximum power in those dequeued spiders, 
the one which comes first in the queue is selected. If at any moment , 
power of any spider becomes 0, it can't be decremented any further, it remains the same.

Now, Aragog asks the boys to tell him the positions of all the selected spiders 
(positions in the initial given queue) in the order they are selected.

Input Format:
The first line consists of two space separated integers N and X, 
denoting the number of spiders in the queue and the number of spiders that have to be selected respectively. 
The next line consists of an array A. A[i] denoting the power of spider at position i(1 <= i <= N)
Output Format:
For each of the X iterations, output the position of the selected spider in that iteration. 
Position refers to the index at which the spider was present in the initial given queue (1 based indexing).
Constraints:
1 <= X <= 316
X<N<X * X
1 <= A[i] <= X; 1 <= i <= N
'''

n, x = map(int, input().split())
arr = list(map(int, input().split()))

from collections import deque
dq = deque()
for i in range(n):
    dq.append((arr[i], i+1))

for _ in range(x):
    temp = []
    for i in range(min(x, len(dq))):
        temp.append(dq.popleft())
    
    maxi, mind = -1, -1
    for val, ind in temp:
        if maxi < val:
            maxi = val
            mind = ind
    
    print(mind, end=" ")

    for val, ind in temp:
        if ind != mind:
            dq.append((max(0, val-1), ind))
    