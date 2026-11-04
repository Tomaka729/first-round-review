ch = input().strip();
end = ord(ch) - ord('A');
for i in range(end + 1):
    s = '';
    for j in range(i + 1):
        s += chr(ord('A') + j);
    for j in range(i - 1, -1, -1):
        s += chr(ord('A') + j);
    print(' '*(end-i)+s);