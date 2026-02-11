#1 Inheritance (Pewarisan)

class Produk:
    def __init__(self, nama_produk, harga):
        self.nama_produk = nama_produk
        self.harga = harga

    def info_produk(self):
        print(f"Nama produk: {self.nama_produk}, dengan harga {self.harga}")

class ProdukElektronik(Produk):
    def __init__(self, nama_produk, harga, garansi):
        super().__init__(nama_produk, harga)
        self.garansi = garansi

    def info_produk(self):
        print(f"Nama produk: {self.nama_produk}, dengan harga {self.harga}, dan lama garansi hingga {self.garansi}")

elektronik = ProdukElektronik("Kulkas", "1.000.000", 2034)
elektronik.info_produk()

class ProdukMakanan(Produk):
    def __init__(self, nama_produk, harga, tanggal_kadaluarsa):
        super().__init__(nama_produk, harga)
        self.tanggal_kadaluarsa = tanggal_kadaluarsa

    def info_produk(self):
        print(f"Nama produk: {self.nama_produk}, dengan harga {self.harga}, dan tanggal kadaluarsa hingga {self.tanggal_kadaluarsa}")

makanan = ProdukMakanan("Biskuat", 2000, "16-08-2027")
makanan.info_produk()


#2 Polymorphism

class Notifikasi:
    def __init__(self, volume, lagu):
        self.volume = volume
        self.lagu = lagu

    def kirim(self):
        pass

class Email(Notifikasi):
    def __init__(self, volume, lagu):
        super().__init__(volume, lagu)
    
    def kirim(self):
        print("Mengirim notifikasi melalui Email")

class SMS(Notifikasi):
    def __init__(self, volume, lagu):
        super().__init__(volume, lagu)
    
    def kirim(self):
        print("Mengirim notifikasi melalui SMS")

email1 = Email("Keras", "Holy Diver")
sms2 = SMS("Sedang", "Psychosocial")

email1.kirim()
sms2.kirim()

#3 Encapsulation

class Mahasiswa:
    def __init__(self):
        self.__nilai = "Nilai tidak valid!"

    def set_nilai(self, nilai):
        if nilai >= 0 and nilai <= 100:
            self.__nilai = nilai
        else:
            return 0

    def get_nilai(self):
        return self.__nilai