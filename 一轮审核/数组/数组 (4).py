L, M = map(int, input().split())
tree = [False] * (L + 1)
for _ in range(M):
    l, r = map(int, input().split())
    for i in range(l, r + 1):
        tree[i] = True
res = 0
for i in range(L + 1):
    if tree[i] == False:
        res += 1
print(res)