"""Course class with name and grades."""


class Course:
    """
    Represent a course or subject in a school.

    Attributes:
        name (str): The name of the course.
        grades (list): List of tuples containing student objects and their grades for this course.
    """

    def __init__(self, name: str):
        """
        Initialize a new Course object.

        Args:
            name (str): The name of the course.
        """
        self.name = name
        self.grades = []

    def add_grade(self, student, grade):
        """
        Add a student's grade to the course.

        Args:
            student: The student object.
            grade (int): The grade received by the student.
        """
        self.grades.append((student, grade))

    def get_grades(self):
        """
        Retrieve a list of tuples containing student objects and their grades for this course.

        Returns:
            list: List of tuples (student, grade).
        """
        return self.grades

    def get_average_grade(self):
        """
        Calculate and return the average grade for this course.

        Returns:
            float: The average grade or -1 if no grades are available.
        """
        if not self.grades:
            return -1
        return sum(grade for _, grade in self.grades) / len(self.grades)

    def __repr__(self):
        """
        Return a string representation of the Course object.

        Returns:
            str: The name of the course.
        """
        return self.name