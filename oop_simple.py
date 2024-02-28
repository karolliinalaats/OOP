"""Simple class."""


class Student:
    """Student class."""

    def __init__(self, name):
        """Student class construct.

        Creates Student type object.

        Parameters:
        name (str) : name of student.
        """
        self.name = name
        self.finished = False