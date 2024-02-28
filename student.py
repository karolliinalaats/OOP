"""Student class with student name and grades."""


class Student:
    """
    Represent a student in a school.

    Attributes:
        name (str): The name of the student.
        id (int): Unique identifier for the student.
        grades (list): List of tuples containing course objects and grades received by the student.
    """

    id_counter = 1

    def __init__(self, name: str):
        """
        Initialize a new Student object.

        Args:
            name (str): The name of the student.
        """
        self.name = name
        self.id = None
        self.grades = []

    def set_id(self, id):
        """
        Set the unique identifier for the student if not already set.

        Args:
            id (int): Unique identifier for the student.
        """
        if self.id is None:
            self.id = id

    def get_id(self):
        """
        Retrieve the unique identifier for the student.

        Returns:
            int: The student's identifier.
        """
        return self.id

    def add_grade(self, course, grade):
        """
        Add a grade for a specific course to the student.

        Args:
            course: The course object.
            grade (int): The grade received by the student.
        """
        self.grades.append((course, grade))

    def get_grades(self):
        """
        Retrieve a list of tuples containing course objects and grades received by the student.

        Returns:
            list: List of tuples (course, grade).
        """
        return self.grades

    def get_average_grade(self):
        """
        Calculate and return the average grade for the student.

        Returns:
            float: The average grade or -1 if no grades are available.
        """
        if not self.grades:
            return -1
        return sum(grade for _, grade in self.grades) / len(self.grades)

    def __repr__(self):
        """
        Return a string representation of the Student object.

        Returns:
            str: The name of the student.
        """
        return self.name