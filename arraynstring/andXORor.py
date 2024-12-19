# Medium Problem

t = int(input())
while t != 0:
    t -= 1

    n = int(input())
    nums = list(map(int, input().split()))

    nums.sort()
    mini = 1e8
    for i in range(1, n):
        mini = min(mini, nums[i-1] ^ nums[i])
    
    print(mini)