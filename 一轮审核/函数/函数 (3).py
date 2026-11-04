import math
def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    max_i = int(math.sqrt(x)) + 1
    i = 3
    while i <= max_i:
        if x % i == 0:
            return False
        i += 2
    return True
s = input().strip()
part = s[:-1][::-1]
pal = int(s + part)

if is_prime(pal):
    print("prime")
else:
    print("noprime")