ans = []
for x in range(1, 100):
    for y in range(x, 10000):
        p = x * y
        d = str(x) + str(y) + str(p)
        if len(d) == 9 and set(d) == {'1','2','3','4','5','6','7','8','9'}:
            ans.append( (p, x, y) )
ans.sort()
for p, a, b in ans:
    print(f"{p} = {a} x {b}")