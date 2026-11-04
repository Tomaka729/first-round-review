cycle = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
n = int(input())
arr = list(map(int, input().split()))
candidates = []
for i in range(30):
    match = True
    for j in range(n):
        p = (i + j) % 30
        if cycle[p] != arr[j]:
            match = False
            break
    if match:
        candidates.append(i)
if len(candidates) != 1:
    print(-1)
else:
    start = candidates[0]
    last_pos = (start + n - 1) % 30
    next_pos = (last_pos + 1) % 30
    if cycle[next_pos] > cycle[last_pos]:
        print("UP")
    else:
        print("DOWN")