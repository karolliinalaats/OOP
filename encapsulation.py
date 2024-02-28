"""Encapsulation exercise."""


class Student:
    def __init__(self, name: str, student_id: int):
        self.__name = name
        self.__id = student_id
        self.__status = "Active"

    def get_id(self) -> int:
        return self.__id

    def set_name(self, name: str):
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def set_status(self, status: str):
        """
        Assigns a new status to the student if it's a valid status.

        Valid statuses: Active, Expelled, Finished, Inactive
        """
        valid_statuses = {"Active", "Expelled", "Finished", "Inactive"}
        if status in valid_statuses:
            self.__status = status

    def get_status(self) -> str:
        return self.__status

