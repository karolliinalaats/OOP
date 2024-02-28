"""School class which stores information about courses and students."""


from student import Student


class School:
    """
    Represent a school that manages students and courses.

    Attributes:
        name (str): The name of the school.
        students (list): List of student objects in the school.
        courses (list): List of course objects offered by the school.
    """

    def __init__(self, name):
        """
        Initialize a new School object.

        Args:
            name (str): The name of the school.
        """
        self.name = name
        self.students = []
        self.courses = []

    def add_course(self, course):
        """
        Add a course to the school.

        Args:
            course: The course object to be added.
        """
        if course not in self.courses:
            self.courses.append(course)

    def add_student(self, student):
        """
        Add a student to the school and assign a unique identifier.

        Args:
            student: The student object to be added.
        """
        if student not in self.students:
            student.set_id(Student.id_counter)
            Student.id_counter += 1
            self.students.append(student)

    def add_student_grade(self, student, course, grade):
        """
        Add a grade for a specific course to a student.

        Args:
            student: The student object.
            course: The course object.
            grade (int): The grade to be added.
        """
        if student in self.students and course in self.courses:
            student.add_grade(course, grade)
            course.add_grade(student, grade)

    def get_students(self):
        """
        Retrieve a list of student objects in the school.

        Returns:
            list: List of student objects.
        """
        return self.students

    def get_courses(self):
        """
        Retrieve a list of course objects offered by the school.

        Returns:
            list: List of course objects.
        """
        return self.courses

    def get_students_ordered_by_average_grade(self):
        """
        Retrieve a list of students ordered by average grade in descending order.

        Returns:
            list: List of student objects.
        """
        return sorted(self.students, key=lambda s: s.get_average_grade(), reverse=True)

