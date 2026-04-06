def lower_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left
 
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    b.sort()
    
    prev = -10**18
    possible = True
    
    for x in a:
        best = float('inf')
        
        if x >= prev:
            best = x
        
        idx = lower_bound(b, prev + x)
        
        if idx < m:
            new_val = b[idx] - x
            if new_val >= prev:
                best = min(best, new_val)
        
        if best == float('inf'):
            possible = False
            break
        
        prev = best
    
    print("YES" if possible else "NO")
