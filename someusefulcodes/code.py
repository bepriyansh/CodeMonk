def upper_bound(nums, t, s, e):
    l,r = s,e
    while l < r:
        m = (l+r)//2
        if nums[m] <= t:
            l = m+1
        else:
            r = m
    return l

def lower_bound(nums, t, s, e):
    l,r = s,e
    while l < r:
        m = (l+r)//2
        if nums[m] < t:
            l = m+1
        else:
            r = m
    return l

def binary_search(nums, t, s, e):
    l,r = s,e
    while l <= r:
        m = (l+r)//2
        if nums[m] == t:
            return m
        elif nums[m] < t:
            l = m+1
        else:
            r = m-1
    return -1

def prevGreaterElements(nums):
    n = len(nums)
    stk, res = [], [-1]*n
    for i in range(n):
        while stk and stk[-1][0] <= nums[i]:
            stk.pop()
        res[i] = stk[-1][1] if stk else -1
        stk.append((nums[i], i))
    return res
        
def nextGreaterElements(nums):
    n = len(nums)
    stk, res = [], [-1]*n
    for i in range(n-1, -1, -1):
        while stk and stk[-1][0] <= nums[i]:
            stk.pop()
        res[i] = stk[-1][1] if stk else -1
        stk.append((nums[i], i))
    return res