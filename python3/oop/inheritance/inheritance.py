# Single Inheritance
class Vehicle:
  def info(self):
    print("Parent class")

class Car(Vehicle):
  def car_info(self):
    print("Child class")
    
car = Car()

car.info()
car.car_info()

# Multiple inheritance
class Person:
  def person_info(self, name, age):
    print("Inside person class")
    print(f"Name: {name}, Age: {age}")

class Company:
  def company_info(self, company_name, location):
    print("Inside Company Class")
    print(f"Name: {company_name}, Location: {location}")

class Employee(Person, Company):
  def employee_info(self, salary, skill):
    print("Inside employee child class")
    print(f"Salary: {salary}, Skill: {skill}")

  
emp = Employee()

emp.person_info("Nick", 43)
emp.company_info("Google", "Atlanta")
emp.employee_info(12000, "Data Scientist")