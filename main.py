class student:
    grade = 10
    name = "Sheeraz Ismail"

    def introduction(self):
        print("Hi I am a student")

    def details(self):
        print("My name is", self.name)
        print("I study in Grade", self.grade)

ob = student()
ob.introduction()
ob.details()


