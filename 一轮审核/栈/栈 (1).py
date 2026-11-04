import itertools

for item in itertools.permutations([1,2,3,4,5,6,7,8]):
    print(' '.join(map(str, item)))