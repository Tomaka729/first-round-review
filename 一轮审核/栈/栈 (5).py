s = input().strip()
cnt_a = 0
cnt_b = 0
ok = True
for ch in s:
    if ch == 'a':
        cnt_a += 1
    else:
        cnt_b += 1
    if cnt_b > cnt_a:
        ok = False
        break
if ok and cnt_a == cnt_b:
    print("Good")
else:
    print("Bad")