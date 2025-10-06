class Student:
    def __init__(self, name, student_id, email):
        self.user_name = name
        self.user_id = student_id
        self.user_email = email

    def display_details(self):
        print(f"Name is {self.user_name} id is {self.user_id} email is {self.user_email}")



std1 = Student("Mike", 123456, "mike@gmail.com")
std1.display_details()

std2 = Student("Mary", 987456321, "mary@gmail.com")
std2.display_details()