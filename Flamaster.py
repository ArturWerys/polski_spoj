
C = int(input())
for x in range(C):
    napis = input().upper()
    compressed = ""
    count = 1

    for i in range(1, len(napis)):
        if napis[i] == napis[i - 1]:
            count += 1
        else:
            if count > 2:
                compressed += napis[i - 1] + str(count)
            else:
                compressed += napis[i - 1] * count
            count = 1

    # Dodaj ostatnią sekwencję
    if count > 2:
        compressed += napis[-1] + str(count)
    else:
        compressed += napis[-1] * count

    print(compressed)