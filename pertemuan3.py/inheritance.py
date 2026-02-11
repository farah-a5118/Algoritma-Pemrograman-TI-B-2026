#1

class Buah: #Parent class, tidak bisa mengakses kelas child
    def __init__(self, nama, rasa, ukuran):
        self.nama = nama #Property
        self.rasa = rasa #Property
        self.ukuran = ukuran #Property

    def fav(self): #Method
        print(f"Buah favoritku adalah {self.nama}, rasanya {self.rasa}, dan ukurannya {self.ukuran}")

class Yummy(Buah): #Child class, bisa mengakses kelas parent
    def __init__(self, nama, rasa, ukuran, aroma):
        super().__init__(nama, rasa, ukuran) #Secara otomatis mewariskan semua methods dan properties dari class parent
        self.aroma = aroma

    def favo(self):
        print(f"Buah favoritku adalah {self.nama}, rasanya {self.rasa}, ukurannya {self.ukuran}, dan aromanya {self.aroma}")

enak = Yummy("mangga", "manis", "sedang", "wangi") #Object
enak.favo()

#2
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2024)
x.welcome()