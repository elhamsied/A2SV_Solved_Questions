n, k = map(int, input().split())
a = list(map(int, input().split()))

freq = {}          
left = 0
distinct = 0
answer = 0

for right in range(n):
    if a[right] not in freq or freq[a[right]] == 0:
        distinct += 1

    freq[a[right]] = freq.get(a[right], 0) + 1

    while distinct > k:
        freq[a[left]] -= 1

        if freq[a[left]] == 0:
            distinct -= 1

        left += 1

    answer += right - left + 1

print(answer)
