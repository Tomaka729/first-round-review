while True:
    try:
        n = int(input())
        for i in range(1, n + 1):
            print('  ' * (n+1 - i) + '*' * i)
        print('*' * (n + 1))
        for i in range(n, 0, -1):
                print('  ' * (n +1- i) + '*' * i)
    except EOFError:
        break