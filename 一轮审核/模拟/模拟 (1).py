n, t = map(int, input().split())
s = input().strip()
if '.' in s:
    dot = s.index('.')
    inte = list(s[:dot])
    frac = list(s[dot+1:])
else:
    inte = list(s)
    frac = []

i = 0
while t and i < len(frac):
    if int(frac[i]) >= 5:
        t -= 1
        c = 1
        j = i - 1
        while c and j >= 0:
            v = int(frac[j]) + c
            frac[j] = str(v % 10)
            c = v // 10
            j -= 1
        if c:
            k = len(inte)-1
            while c and k >= 0:
                v = int(inte[k]) + c
                inte[k] = str(v % 10)
                c = v // 10
                k -= 1
            if c:
                inte.insert(0, '1')
            frac = []
            break
        frac = frac[:i]
        i = 0
    else:
        i += 1

res = ''.join(inte)
if frac:
    res += '.' + ''.join(frac)
print(res)