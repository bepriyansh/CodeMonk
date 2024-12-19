#Easy problem

t = int(input())
while t != 0:
    t -= 1

    n = int(input())
    mat = [list(map(int, input().split())) for i in range(n)]

    count = 0
    for i in range(n):
        for j in range(n):
            for x in range(i, n):
                for y in range(j, n):
                    if mat[i][j] > mat[x][y]:
                        count += 1
    print(count)