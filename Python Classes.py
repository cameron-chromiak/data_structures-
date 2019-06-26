import math
# # working class example
#
# class Clicker():
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def incX(self, x):
#         self.x = self.x + x
#
#     def incY(self):
#         self.y = self.y + 1
#
#     def printData(self):
#         print("x: ",self.x, "y: ",self.y)
#
# click = Clicker(1, 5)
#
# click.incX(3)
# click.printData()
#

# breeds = ['sheperd', 'lab', 'boxer']
#
# class Dog():
#     species = 'mammal'
#     def __init__(self, breed, name):
#         self.breed = breed
#         self.name = name
#
#
#     def bark(self):
#         print("Woof!, my name is",self.name, "I am a", self.breed)
#
# ava = Dog(breeds[1], 'Ava')
# jax = Dog(breeds[0], 'Jax')
# ava.bark()
# jax.bark()


# class Animal():
#     def __init__(self):
#         print("Animal Created")
#
#     def whoAmI(self):
#         print("I am an animal")
#
#     def eat(self):
#         print("Nom Nom Nom")
#
# class Dog(Animal):
#     species = 'mammal'
#     def __init__(self, name, breed):
#         Animal.__init__(self)
#         print("Dog Created")
#         self.name = name
#         self.breed = breed
#
#     def bark(self):
#         print("Woof!, my name is",self.name, "I am a", self.breed)
#
# brady = Dog("Brady", "Boxer")
# brady.bark()
# brady.eat()



# Pollymorphism

class Dog():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says woof"

class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says meow"

ava = Dog('Ava')
nelly = Cat('Nelly')

def pet_speak(pet):
    print(pet.speak())

pet_speak(ava)
pet_speak(nelly)

#Special Methods
#
# class Book():
#     """docstring for Book."""
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#
#     def __str__(self):
#         return f"{self.title} by {self.author}"
#
#     def __len__(self):
#         return self.pages
#
#     def __del__(self):
#         print("Book object has been deleted")
#
# b = Book('CAMERON', 'Cam', 69)
# print(b)
# del(b)

#CHALLENGE FIND SLOPE AND DISTANCE

# class Line():
#
#
#     def __init__(self, coor1, coor2):
#         self.coor1 = coor1
#         self.coor2 = coor2
#
#     def distance(self):
#         x = self.coor1[0] - self.coor2[0]
#         y = self.coor1[1] - self.coor2[1]
#
#         x = x**2
#         y = y**2
#             #convert to abs
#         print("Distance ", math.sqrt(abs(x+y)))
#
#     def slope(self):
#         x = self.coor1[0] - self.coor2[0]
#         y = self.coor1[1] - self.coor2[1]
#
#         print("Slope ",y/x)
#
# line = Line((3,2),(8,10))
# line.slope()
# line.distance()

#BANK ACCOUNT
class Account():
    pass

    def __init__(self, owner, balanace):
        self.owner = owner
        self.balance = balanace

    def deposit(self, amnt):
        if (amnt <= 0):
            print('Cannot make negative deposite')
        else:
            self.balance += amnt


    def withdrawl(self, amnt):
        if (amnt <= 0 or amnt >= self.balance):
            print("Withdrawl ammount cannot be greater than balance")
        else:
            self.balance -= amnt


    def __str__(self):
        return f"{self.owner}\'s account has {self.balance}"

acct = Account('Cam', 500)
acct.deposit(500)
acct.withdrawl(1500)
print(acct)
