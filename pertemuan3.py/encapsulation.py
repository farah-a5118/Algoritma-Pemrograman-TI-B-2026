#1

class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

  def get_age(self):
    return self.__age

p1 = Person("Tobias", 25)
print(p1.get_age())


#2
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

  def get_age(self):
    return self.__age

  def set_age(self, age):
    if age > 0:
      self.__age = age
    else:
      print("Age must be positive")

p1 = Person("Tobias", 25)
print(p1.get_age())

p1.set_age(26)
print(p1.get_age())


#3, PROTECTED PROPERTIES

class Person:
  def __init__(self, name, salary):
    self.name = name
    self._salary = salary #Properti yang dilindungi, ditandai dengan 1 underscode di awal

p1 = Person("Linus", 50000)
print(p1.name)
print(p1._salary) #Bisa diakses, tapi sebaiknya jangan


#4, PRIVATE METHOD

class Calculator:
  def __init__(self):
    self.result = 0

  def __validate(self, num):
    if not isinstance(num, (int, float)):
      return False
    return True

  def add(self, num):
    if self.__validate(num):
      self.result += num
    else:
      print("Invalid number")

calc = Calculator()
calc.add(10)
calc.add(5)
print(calc.result)
# calc.__validate(5) # This would cause an error


#5, NAME MANGLING
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

p1 = Person("Emil", 30)

# This is how Python mangles the name:
print(p1._Person__age) # Not recommended!

'''
Tanda __ (underscore dua kali) di awal nama property menandakan property tersebut private dan tidak bisa diakses secara global
Untuk mengaksesnya menggunakan get
Dan mengubahnya menggunakan set
'''

'''
INI AKAN ERROR:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age # Private property

p1 = Person("Emil", 25)
print(p1.name)
print(p1.__age) # This will cause an error
'''