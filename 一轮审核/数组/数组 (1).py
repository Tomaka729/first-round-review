import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    ptr = 0
    T = data[ptr]
    ptr += 1
    for _ in range(T):
        n = data[ptr]
        ptr += 1
        a = data[ptr:ptr + n]
        ptr += n
        max_a = max(a)
        min_a = min(a)
        r = max_a - min_a
        avg = sum(a) / n
        s = 0.0
        for num in a:
            s += (num - avg) ** 2
        var = s / n
        print(f"{r} {var:.3f}")

if __name__ == "__main__":
    main()