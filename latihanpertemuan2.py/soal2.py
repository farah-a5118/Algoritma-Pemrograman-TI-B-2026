def bilangan_prima(n):
    prima = []
    for angka in range(1, n + 1):
        for bagi in range(2, angka):
            if angka % bagi == 0:
                break
        else:
            prima.append(angka)
    return prima

hasil = bilangan_prima(50)
print(hasil)