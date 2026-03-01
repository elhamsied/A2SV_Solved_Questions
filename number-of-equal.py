from collections import Counter
 
 
n,m = map(int,input().split())
a1 = list(map(int,input().split()))
a2 = list(map(int,input().split()))
ans =0
counts =Counter(a1)
counts2 = Counter(a2)
for key in counts:
    if key in counts2:
        ans+= counts[key]*counts2[key]
print(ans)
