#Syntax dasar try except
'''
try:
    #Menjalankan kode yang kemungkinan terdapat error
except:
    #Bagaimana cara pengguna menangani error tersebut
'''

#Terdapat error
try:
    hasil = 10/0 #Contoh potongan kode yang akan menghasilkan error 
except ZeroDivisionError as e:
    print(f"Error: pembagian oleh 0 tidak diizinkan! {e}!") #Yang akan dijalankan ketika blok 'try' ditemukan error
else:
    print(f"Hasil pembagian: {hasil}") #Kode yang akan dijalankan jika tidak blok 'try' tidak ditemukan error
finally:
    print("Pembagian selesai!") #Kode yang pasti dijalankan

#Tidak terdapat error
try:
    hasil = 10/2 #Contoh potongan kode yang tidak akan menghasilkan error 
except ZeroDivisionError as e:
    print(f"Error: pembagian oleh 0 tidak diizinkan! {e}!") #Yang akan dijalankan ketika blok 'try' ditemukan error
else:
    print(f"Hasil pembagian: {hasil}") #Kode yang akan dijalankan jika tidak blok 'try' tidak ditemukan error
finally:
    print("Pembagian selesai!") #Kode yang pasti dijalankan