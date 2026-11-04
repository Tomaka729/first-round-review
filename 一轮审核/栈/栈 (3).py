n = int(input())
a = list(map(int, input().split()))
a.sort()
ok = False
for i in range(n - 2):
    x, y, z = a[i], a[i+1], a[i+2]
    if x + y > z:
        print(x, y, z)
        ok = True
        break
if not ok:
    print("No solution")