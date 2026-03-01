n, s = map(int, input().split())
a = list(map(int, input().split()))

count = 0
current_sum = 0
r = 0

for l in range(n):
    while r < n and current_sum < s:
        current_sum += a[r]
        r += 1
    
    if current_sum >= s:
        count += (n - r + 1)
    current_sum -= a[l]

print(count)
