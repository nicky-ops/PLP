# overloading + operator
class Book:
  def __init__(self, pages):
    self.pages = pages

  def __add__(self, other):
    return self.pages + other.pages

b1 = Book(9000)
b2 = Book(3000)
print(b1 + b2)

# overloading * operator
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __mul__(self, timesheet):
        print('Worked for', timesheet.days, 'days')
        # calculate salary
        return self.salary * timesheet.days


class TimeSheet:
    def __init__(self, name, days):
        self.name = name
        self.days = days


emp = Employee("Jessa", 800)
timesheet = TimeSheet("Jessa", 50)
print("salary is: ", emp * timesheet)