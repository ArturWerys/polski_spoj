D = int(input())
for x in range(D):
    a, b = map(int, input().split())
    result = 1
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % 10
        a = (a * a) % 10
        b //= 2
    print(result)
    