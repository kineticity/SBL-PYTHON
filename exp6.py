class Person:
    def __init__(self, id, name):
        self.ID = id
        self.name = name

    def display(self):
        print("\nID = ",self.ID)
        print("Name = ", self.name)

class Student(Person):
    def __init__(self, x, y, id, name):
        super().__init__(id, name)
        self.sub1 = x
        self.sub2 = y

    def display(self):
        #print("\nStudent ID = ", self.ID)
        #print("Student Name = ", self.name)
        super().display()
        print("Marks in subject 1 = ", self.sub1)
        print("Marks in subject 2 = ", self.sub2)

class Sports:
    def showsports(self, s=None):
        self.sportsmarks = s
        if s!=None:
            print("\nSports marks = ", self.sportsmarks)

class Result(Student, Sports):
    def __init__(self, id, name, x, y):
        super().__init__(x, y, id, name)

    def total(self):
        if self.sportsmarks is not None:
            sum1 = self.sub1 + self.sub2 + self.sportsmarks
        else:
            sum1 = self.sub1 + self.sub2
        print("\nWe have, Total Marks = ", sum1, "\n")

print("Enter the student details:-")
id = input("\nEnter Student ID: ")
name = input("\nEnter Student Name: ")
m1 = int(input("\nEnter marks in first subject: "))
m2 = int(input("\nEnter marks in second subject: "))

obj = Result(id, name, m1, m2)

obj.display()

c = input("\nDo you want to enter sports marks? (y/n): ")
if c=="y":
    sm = int(input("Enter sports marks: "))
    obj.showsports(sm)
else:
    obj.showsports()
obj.total()
