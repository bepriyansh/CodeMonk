def toBin(n):
    if n == 0:
        return "0"
    s = ""
    while n:
        p = n % 2
        n //= 2
        s = str(p) + s
    return s

cache = {}
def fact(n):
    if n in cache:
        return cache[n]
    p = 1
    for i in range(2, n + 1):
        p *= i
    cache[n] = p
    return cache[n]

def ncr(n, r):
    return fact(n) // (fact(r) * fact(n - r))

def solve():
    n, l = map(int, input().split())
    nums = list(map(int, input().split()))

    m = max(nums)
    k = len(toBin(m))
    b = [0] * k

    # calculate setBits at each index
    for num in nums:
        for i in range(k):
            b[i] += num % 2
            num //= 2

    # calculate required setBits to maximise f(x)
    cnt = 0
    p, tp = 1, {}  # product, total Product Contributions
    for i in range(k):
        if b[i] > 0:
            cnt += 1

        # calculating contribution from each
        b[i] *= p
        p *= 2
        if b[i] in tp:
            tp[b[i]] += 1
        else:
            tp[b[i]] = 1

    ans = 1
    if cnt == l:
        ans = 1  # required setBits equal to provided limit
    elif cnt < l:  # required setBits less than provided limit
        ans = -1
    else:  # required setBits are more than the provided limit
        # sort the contributions
        sorted_tp = sorted(tp.items(), reverse=True)
        for prod, reqBits in sorted_tp:
            if reqBits < l:
                l -= reqBits  # consume all bits that maximise
            else:
                # now we are left with some allowed bits from the provided limits
                # so choose remaining bits (all these bits contribute equally)
                ans = ncr(reqBits, l)
                break
    print(ans)

for _ in range(int(input())):
    solve()
