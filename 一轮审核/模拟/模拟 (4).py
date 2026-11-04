words = [("zero", "0"), ("four", "4"), ("nine", "9"), ("two", "2"), ("six", "6")]
T = int(input())
for _ in range(T):
    s = input().strip()
    res = []
    i = 0
    n = len(s)
    while i < n:
        if s[i] in {'0','2','4','6','9'}:
            res.append(s[i])
            i += 1
            continue
        ok = False
        for w, val in words:
            lw = len(w)
            if i + lw <= n and s[i:i+lw] == w:
                res.append(val)
                i += lw
                ok = True
                break
        if ok:
            continue
        i += 1
    print(''.join(res))