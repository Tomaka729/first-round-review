cnt = list(map(int, input().split()))
odd = []
for i in range(10):
    if cnt[i] % 2 == 1:
        odd.append(i)
if len(odd) > 1:
    print(-1)
else:
    mid = ''
    if len(odd) == 1:
        mid = str(odd[0])
        cnt[odd[0]] -= 1
    left = []
    first = -1
    for d in range(1,10):
        if cnt[d] >= 2:
            first = d
            break
    if first == -1:
        if cnt[0] == 0 and mid != '':
            print(mid)
        else:
            print(-1)
    else:
        left.append(str(first))
        cnt[first] -= 2
        for d in range(0,10):
            num = cnt[d] // 2
            left.append(str(d)*num)
        left_str = ''.join(left)
        right_str = left_str[::-1]
        ans = left_str + mid + right_str
        print(ans)