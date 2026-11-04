x, y = map(int, input().split())
l = min(x, y)
r = max(x, y)
cnt = 0
for n in range(l, r + 1):
    s = str(n)
    total = 0
    for ch in s:
        total += int(ch)
    if total % 5 == 0:
        cnt += 1
print(cnt)