mid = {
    (1,3):2,(3,1):2,
    (1,7):4,(7,1):4,
    (1,9):5,(9,1):5,
    (2,8):5,(8,2):5,
    (3,7):5,(7,3):5,
    (3,9):6,(9,3):6,
    (4,6):5,(6,4):5,
    (7,9):8,(9,7):8
}

import sys
for line in sys.stdin:
    s = line.strip()
    if not s:
        continue
    path = [int(c) for c in s]
    vis = set()
    ok = True
    for i in range(len(path)):
        cur = path[i]
        if cur in vis:
            ok = False
            break
        if i > 0:
            pre = path[i-1]
            if (pre, cur) in mid:
                m = mid[(pre, cur)]
                if m not in vis:
                    ok = False
                    break
        vis.add(cur)
    print("YES" if ok else "NO")
