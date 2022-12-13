class Person:
    def __init__(self, name, lastname, email):
        self.name = name
        self.lastname = lastname
        self.email = email

    def send_email(self, other, topic, text):
        print("Message was sent")


class Student(Person):
    def __init__(self, name, lastname, email, index):
        super().__init__(name, lastname, email)
        self.index = index


class Staff(Person):
    def __init__(self, name, lastname, email, room):
        super().__init__(name, lastname, email)
        self.room = room


class ResearchStaff(Staff):
    def __init__(self, name, lastname, email, room):
        super().__init__(name, lastname, email, room)
        self.publications = []


class TeachingStaff(Staff):
    def __init__(self, name, lastname, email, room):
        super().__init__(name, lastname, email, room)
        self.lectures = []


class ResearchAndTeaching(ResearchStaff, TeachingStaff):
    def __init__(self, name, lastname, email, room):
        super().__init__(name, lastname, email, room)


# print(ResearchAndTeaching.__mro__)
