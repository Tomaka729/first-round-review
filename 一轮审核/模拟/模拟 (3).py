import sys

def main():
    s = sys.stdin.read()
    res = []
    i = 0
    n = len(s)
    while i < n:
        if s[i] == '\\' and i+1 < n and s[i+1] == '"':
            res.append(s[i])
            res.append(s[i+1])
            i += 2
        elif s[i] == '"':
            res.append(s[i])
            i += 1
            while i < n:
                if s[i] == '\\' and i+1 < n and s[i+1] == '"':
                    res.append(s[i])
                    res.append(s[i+1])
                    i += 2
                elif s[i] == '"':
                    res.append(s[i])
                    i += 1
                    break
                else:
                    res.append(s[i])
                    i += 1
        elif i+1 < n and s[i] == '/' and s[i+1] == '*':
            j = i + 2
            found = False
            while j+1 < n:
                if s[j] == '*' and s[j+1] == '/':
                    found = True
                    j += 2
                    break
                j += 1
            if found:
                i = j
            else:
                res.append(s[i])
                res.append(s[i+1])
                i += 2
        else:
            res.append(s[i])
            i += 1
    print(''.join(res), end='')

if __name__ == "__main__":
    main()