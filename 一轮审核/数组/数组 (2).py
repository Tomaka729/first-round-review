n, x = map(int, input().split())
cnt = 0
for i in range(1, n + 1):
    num = i
    while num > 0:
        d = num % 10
        if d == x:
            cnt += 1
        num = num // 10
print(cnt)