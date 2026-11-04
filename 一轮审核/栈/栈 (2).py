def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    n, K = int(input[ptr]), int(input[ptr+1])
    ptr += 2
    A = list(map(int, input[ptr:ptr+n]))
    ptr += n
    B = list(map(int, input[ptr:ptr+n]))    
    sumB = 0
    delta = []
    for a, b in zip(A, B):
        sumB += b
        delta.append(a - b)
    delta.sort(reverse=True)
    add = sum(delta[:K])
    print(sumB + add)
if __name__ == "__main__":
    main()