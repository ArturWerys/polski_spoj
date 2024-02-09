import sys
N = int(input())


if N > 20:
    sys.exit(1)

for n in range(N):
    text = input()
    ab_tab = text.split(' ')
    smaller = int(ab_tab[0])
    bigger = int(ab_tab[1])

    if smaller > 10 and bigger > 30:
        sys.exit(1)

    tmp = 0

    if smaller > bigger:
        tmp = smaller
        smaller = bigger
        bigger = tmp

    result = bigger

    while result % smaller != 0 or result % bigger != 0:
        result += bigger

    print(result)
