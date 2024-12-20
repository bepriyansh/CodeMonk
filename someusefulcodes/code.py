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