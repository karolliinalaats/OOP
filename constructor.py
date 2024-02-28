"""Constructor exercise."""


class Empty:
    """An empty class without constructor."""

    pass


class Person:
    """Represent person with firstname, lastname and age."""

    def __init__(self):
        self.firstname = ""
        self.lastname = ""
        self.age = 0

    pass


class Student:
    """Represent student with firstname, lastname and age."""

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    pass


if __name__ == '__main__':
    # empty usage
    empty = Empty()
    # 3 x person usage
    person1 = Person()
    person2 = person()
    person3 = Person()
    # 3 x student usage
    s1 = Student('John', 'Doe', 15)
    s2 = Student('Alice', 'Cooper', 20)
    s3 = Student('Bob', 'Johnson', 25)
    pass

