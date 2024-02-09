D = int(input())
for x in range(D):
    n = int(input())
    if n <= 10:
        if n == 0:
            print("0 1")
        else:
            factorial = 1
            for i in range(2, n+1):
                factorial *= i
            tens = (factorial // 10) % 10
            unit = factorial % 10
            print(f"{tens} {unit}")
    else:
        print('0 0')
