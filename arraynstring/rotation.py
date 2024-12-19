#Easy problem

t = int(input())
while t != 0:
    t -= 1

    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    k = k % n
    nums[:n-k] = reversed(nums[:n-k])
    nums[n-k:] = reversed(nums[n-k:])
    nums.reverse()

    print(" ".join(map(str, nums)))