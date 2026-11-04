def mach(n):
    for i in range(1, n + 1, 2):
        print(' ' * ((n - i) // 2) + '*' * i)
    for i in range(n - 2, 0, -2):
        print(' ' * ((n - i) // 2) + '*' * i)
t = int(input())
for k in range(t):
    n = int(input())
    mach(n)
