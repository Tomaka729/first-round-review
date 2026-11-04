import sys

def get_day(y, m):
    if m in [1,3,5,7,8,10,12]:
        return 31
    elif m in [4,6,9,11]:
        return 30
    else:
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
            return 29
        else:
            return 28
def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        y, m, x = map(int, line.split())
        target = str(x)
        cnt = 0
        maxd = get_day(y, m)
        for d in range(1, maxd + 1):
            s = f"{y:04d}-{m:02d}-{d:02d}"
            cnt += s.count(target)
        print(cnt)
if __name__ == "__main__":
    main()