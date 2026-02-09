def rata_rata(nilai):
    if len(nilai) == 0:
        print("Data Kosong")
        return 0
    total = sum(nilai)
    rata_rata = total/len(nilai)
    return rata_rata

nilai_mahasiswa = [80, 75, 90, 60, 85]
hasil = rata_rata(nilai_mahasiswa)

print(f"Nilai Mahasiswa: {nilai_mahasiswa}")
print(f"Rata-rata: {hasil}")