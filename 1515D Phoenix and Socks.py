t = int(input())

for _ in range(t):
    n, l, r = map(int, input().split())
    c = list(map(int, input().split()))
    
    left = {}
    right = {}
    
    for i in range(l):
        left[c[i]] = left.get(c[i], 0) + 1
    for i in range(l, n):
        right[c[i]] = right.get(c[i], 0) + 1
    
    for color in list(left.keys()):
        if color in right:
            m = min(left[color], right[color])
            left[color] -= m
            right[color] -= m
    
    l_rem = sum(left.values())
    r_rem = sum(right.values())
    
    if l_rem < r_rem:
        left, right = right, left
        l_rem, r_rem = r_rem, l_rem
    
    cost = 0
    diff = l_rem - r_rem
    
    for color in left:
        pairs = left[color] // 2
        take = min(pairs, diff // 2)
        
        cost += take
        left[color] -= take * 2
        diff -= take * 2
    
    cost += diff // 2
    remaining = sum(left.values()) + sum(right.values())
    cost += remaining // 2
    
    print(cost)
