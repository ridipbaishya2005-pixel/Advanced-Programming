class Address:
    def __init__(self, street, city, zip_code):
        self.street = street
        self.city = city
        self.zip_code = zip_code

    def display(self):
        return f"{self.street}, {self.city} - {self.zip_code}"


class Student:
    def __init__(self, name, age, address, courses=None):
        self.name = name
        self._age = None   # protected attribute
        self.age = age     # use setter for validation
        self.address = address  # Composition (HAS-A relationship)

        # Mutable list (shared reference behavior understood)
        self.courses = courses if courses is not None else []

    # Property for age with validation
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value <= 0 or value > 120:
            raise ValueError("Age must be between 1 and 120")
        self._age = value

    # Method to add course (mutable behavior persists)
    def add_course(self, course):
        self.courses.append(course)

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address.display()}")
        print(f"Courses: {', '.join(self.courses)}")


class ScholarshipStudent(Student):
    def __init__(self, name, age, address, scholarship_amount, courses=None):
        super().__init__(name, age, address, courses)
        self.scholarship_amount = scholarship_amount

    # Overriding display method
    def display(self):
        super().display()
        print(f"Scholarship Amount: {self.scholarship_amount}")


# ------------------ Testing ------------------

# Create Address object
addr = Address("Main Street", "Tezpur", "784001")

# Create Student
s1 = Student("Ridip", 20, addr)
s1.add_course("Math")
s1.add_course("Physics")

# Create ScholarshipStudent
s2 = ScholarshipStudent("Aman", 22, addr, 5000)
s2.add_course("Computer Science")

# Display
print("---- Student ----")
s1.display()

print("\n---- Scholarship Student ----")
s2.display()