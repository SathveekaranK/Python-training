class Person:
    def wake(self):
        print("Person wakes up at 6 AM")

class Student(Person):
    def action(self):
        print("Students goes to school")

s1=Student()
s1.action()
s1.wake()