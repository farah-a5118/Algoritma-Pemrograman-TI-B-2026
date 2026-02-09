def jumlah_digit(n):
    if len(n) == 0:
        return 0
    else:
        return n[0] + jumlah_digit(n[1:])

input = [1, 2, 3, 4, 5]
print(jumlah_digit(input))