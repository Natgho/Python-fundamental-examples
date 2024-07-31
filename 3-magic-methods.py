# list of magic methods: https://realpython.com/python-magic-methods/
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"I'm {self.name}, and I'm {self.age} years old."

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


if __name__ == '__main__':
    person1 = Person('Sezer', 29)
    person2 = Person('Sezer', 29)
    print(person1)
    print(person2)
    print(f"Are they equal? {person1 == person2}")

