for _ in range(int(input())):
    n, coin = map(int, input().split())
    arr = [tuple(map(int, input().split())) for _ in range(n)]
    
    arr.sort()
    
    changed = True
    while changed:
        changed = False
        for l, r, real in arr:
            if l <= coin <= r and real > coin:
                coin = real
                changed = True
    
    print(coin)
