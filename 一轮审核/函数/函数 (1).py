L, R = map(int, input().split())
s = ""
for i in range(L, R+1):
    s += str(i)
print(s.count('2'))