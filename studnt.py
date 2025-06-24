class student:
    grade = 10
    name = "Nirjal"
    def introduction(self):
        print("Hi i am a student")
    def details(self):
        print("My name is", self.name)
        print("I study in grad:", self.grade)
ob = student()
ob.introduction()
ob.details()