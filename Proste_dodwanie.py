import sys

t = int(input())

if t > 100:
    sys.exit(1)

for n in range(t):
    N = int(input())
    text = input()

    textSp = text.split(' ')

    numbers = [int(x) for x in textSp]
    suma = sum(numbers)
    print(suma)
