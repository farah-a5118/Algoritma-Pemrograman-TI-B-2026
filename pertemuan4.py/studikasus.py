#CONTOH STUDI KASUS TRY EXCEPT DAN USER INPUT

#KASUS PENGGUNA SALAH MEMASUKKAN INPUT, SEHARUSNYA MEMASUKKAN ANGKA DAN BUKAN TEKS

try: 
    bilangan = int(input("Masukkan angka: "))
    genap = bilangan % 2 == 0
except ValueError:
    print("Input harus berupa angka!")
else:
    if bilangan % 2 == 0:
        print(f"{bilangan} adalah bilangan genap.")
    elif bilangan % 2 != 0:
        print(f"{bilangan} bukan bilangan genap.")