def pangkat_rekursif(a, b):
    if (b == 0):
        return 1
    else:
        return a*pangkat_rekursif(a, b-1)

print(pangkat_rekursif(a = 2, b = 5))