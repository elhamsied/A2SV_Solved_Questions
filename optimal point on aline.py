n = int(input())
arr = list(map(int, input().split()))

arr.sort()

x = arr[(n - 1) // 2]

print(x)
