from abc import ABC, abstractmethod

# Base Abstract Class
class LibraryItem(ABC):

    # Static Counter
    total_items = 0

    def __init__(self, title, year):
        self.title = title
        self.year = year

        LibraryItem.total_items += 1

    # Abstract Method
    @abstractmethod
    def displayInfo(self):
        pass


# Book Class
class Book(LibraryItem):

    # Default argument used
    def __init__(self, title, year, author="Unknown Author"):
        super().__init__(title, year)
        self.author = author

    # Method Overriding
    def displayInfo(self):
        print("\n----- Book Details -----")
        print("Title  :", self.title)
        print("Year   :", self.year)
        print("Author :", self.author)


# DVD Class
class DVD(LibraryItem):

    # Default arguments used
    def __init__(self, title, year, duration=0, genre="Unknown"):
        super().__init__(title, year)
        self.duration = duration
        self.genre = genre

    # Method Overriding
    def displayInfo(self):
        print("\n----- DVD Details -----")
        print("Title    :", self.title)
        print("Year     :", self.year)
        print("Duration :", self.duration, "minutes")
        print("Genre    :", self.genre)


# Creating Objects
item1 = Book("Python Programming", 2023, "Guido van Rossum")
item2 = DVD("Inception", 2010, 148, "Sci-Fi")
item3 = Book("Data Structures", 2022)
item4 = DVD("Interstellar", 2014, 169, "Adventure")


# Polymorphism using collection of LibraryItem objects
library_items = [item1, item2, item3, item4]

print("===== Library Items =====")

for item in library_items:
    item.displayInfo()


# Static Counter Display
print("\nTotal Library Items :", LibraryItem.total_items)