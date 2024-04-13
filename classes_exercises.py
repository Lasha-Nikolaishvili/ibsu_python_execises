class MyClass:
    x = 5


obj1 = MyClass()
obj2 = MyClass()

obj1.x += 1
print(obj1.x)
print(obj2.x)


class Computer:
    Ram = "8GB"
    CPU = "Intel 2.8GH"
    HardDrive = "HDD  1TB"

    def __init__(self, ram, cpu, hdd):
        self.ram = ram
        self.cpu = cpu
        self.hdd = hdd

    def print_computer(self):
        print("Computer has ram {}, CPU {} and HardDrive {}".format(self.Ram, self.CPU, self.HardDrive))


lenovo = Computer("16GB", "i7", "1TB SSD")
lenovo.print_computer()


class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def print_person(self):
        print("Person's name is {}, my surname is {} and age is {}".format(self.name, self.surname, self.age))

    def is_adult(self):
        if self.age >= 18:
            print(f"{self.name} is an Adult")
        else:
            print(f"{self.name} is a Teenager")


first_person = Person("Lasha", "Nikolaishvili", 21)
first_person.print_person()
first_person.is_adult()


# Inheritance / Subclasses
class A:
    def feature1(self):
        print("Feature 1")

    def feature2(self):
        print("Feature 2")


class B(A):
    def feature3(self):
        print("Feature 3")

    def feature4(self):
        print("Feature 4")


class C(B):
    def feature5(self):
        print("Feature 5")

    def feature6(self):
        print("Feature 6")


A().feature1()
B().feature1()
B().feature3()
C().feature1()
C().feature3()
C().feature6()


# Shapes Examples
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length


mysquare =Square(4)
print(mysquare.area())
print(mysquare.perimeter())

mycube = Cube(10)
print(mycube.surface_area())
print(mycube.volume())


# Multiple inheritance
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Dancer:
    def __init__(self, style):
        self.style = style


class Student(Human, Dancer):
    def __init__(self, name, age, style):
        Human.__init__(self, name, age)
        Dancer.__init__(self, style)


stud = Student("Jajo", 20, "Samba")
print(stud.name)
print(stud.age)
print(stud.style)


# Encapsulation
class Payment:
    def __init__(self, final_price):
        self.__final_price = final_price

    def get_final_price(self):
        return self.__final_price

    def set_final_price(self, discount):
        self.__final_price = self.__final_price - self.__calculate_discount(discount)

    # Private class method
    def __calculate_discount(self, discount):
        return self.__final_price * (discount/100)


book = Payment(10)

# Warning but still works
# print(book._final_price)

# Error
# print(book.__final_price)
print(book.get_final_price())
book.set_final_price(23)
print(book.get_final_price())