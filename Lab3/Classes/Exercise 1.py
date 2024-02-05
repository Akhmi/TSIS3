#1 Class with getString and printString methods:
class StringManipulator:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("Enter a string: ")

    def printString(self):
        print(self.string.upper())

#2 Shape and Square classes:
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

#3 Rectangle class inheriting from Shape:
    class Rectangle(Shape):
        def __init__(self, length, width):
            self.length = length
            self.width = width

        def area(self):
            return self.length * self.width

#4 Point class:
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Coordinates: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

#5 Bank account class:
class Account:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

#6 Filtering prime numbers using filter function:
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

prime_numbers = list(filter(lambda x: all(x % i != 0 for i in range(2, int(x**0.5) + 1)) if x > 1 else False, numbers))

print(prime_numbers)  #[2, 3, 5, 7, 11]



