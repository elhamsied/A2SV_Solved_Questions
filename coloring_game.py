t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    ans = 0
    
    for k in range(2, n):
        limit = max(a[k], a[n-1] - a[k])
        
        i = 0
        j = k - 1
        
        while i < j:
            if a[i] + a[j] > limit:
                ans += (j - i)
                j -= 1
            else:
                i += 1
    
    print(ans)
