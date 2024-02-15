# class Person:
#     def __int__(self):
#         self.name = "John"
#         self.age = 30
#         self.genda = "Male"
#         self.email = "johnkuya@gmail.com"
#
#
# person = Person()
# person.name = "Chris John"
# person.age = 37
# person.genda = "Male"
# person.email = "johnkuya@gmail.com"
# print(person.name)

class People:
    def __init__(self, name, age, phone, email):
        self.name = name
        self.age = age
        self.phone = phone
        self.email = email


person1 = People("James", "25", "0715431053", "james@gmail.com")
person2 = People("Kochellah", "56", "Male", "kochellah@gmail.com")
print(person1.name)
print(f"My name is {person2.name} and I am {person2.age} years old")
print(f"My name is {person1.name} and I am {person1.age} years old.You can contact me through {person1.phone} or email me through {person1.email} ")
