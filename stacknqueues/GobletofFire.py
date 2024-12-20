'''
Little Monk and Goblet of Fire
Albus Dumbledore announced that the school will host the legendary event known as Wizard Tournament where four magical schools are going to compete against each other in a very deadly competition by facing some dangerous challenges. Since the team selection is very critical in this deadly competition. Albus Dumbledore asked Little Monk to help him in the team selection process. There is a long queue of students from all the four magical schools. Each student of a school have a different roll number. Whenever a new student will come, he will search for his schoolmate from the end of the queue. As soon as he will find any of the schoolmate in the queue, he will stand behind him, otherwise he will stand at the end of the queue. At any moment Little Monk will ask the student, who is standing in front of the queue, to come and put his name in the Goblet of Fire and remove him from the queue. There are Q operations of one of the following types:
E x y: A new student of school x (1 ≤ x ≤4) whose roll number is y (1≤ y ≤ 50000) will stand in queue according to the method mentioned above.
D : Little Monk will ask the student, who is standing in front of the queue, to come and put his name in the Goblet of Fire and remove him from the queue

Now Albus Dumbledore asked Little Monk to tell him the order in which student put their name. Little Monk is too lazy to that so he asked you to write a program to print required order.
Note: Number of dequeue operations will never be greater than enqueue operations at any point of time.
Input Format:
First line contains an integer Q (1≤Q≤100000), denoting the number of operations. Next Q lines will contains one of the 2 types of operations.
Output Format:
For each 2nd type of operation, print two space separated integers, the front student's school and roll number.
'''

'''
# bruteforce
q = int(input())

from collections import deque
dq = deque()
stk = []

def ins(x,y):
    while len(dq) > 0 and dq[-1][0] != x:
        stk.append(dq.pop())
    if len(dq) != 0:
        dq.append((x,y))
        while len(stk) > 0:
            dq.append(stk.pop())
    else:
        while len(stk) > 0:
            dq.append(stk.pop())
        dq.append((x,y))

for _ in range(q):
    Q = input().split()
    if Q[0] == 'E':
        x, y = int(Q[1]), int(Q[2])
        ins(x,y)
    elif len(dq) > 0:
        t = dq.popleft()
        print(*t)
'''


q = int(input())

from collections import deque, defaultdict

ques = defaultdict(deque)
quesOrdr = deque()

def ins(x,y):
    if x not in ques or len(ques[x]) == 0:
        quesOrdr.append(x)
    ques[x].append((x,y))

def top():
    o = quesOrdr[0]
    t = ques[o].popleft()
    if len(ques[o]) == 0:
        quesOrdr.popleft()
    print(*t)

for _ in range(q):
    Q = input().split()
    if Q[0] == 'E':
        x, y = map(int, Q[1:])
        ins(x,y)
    else:
        top()