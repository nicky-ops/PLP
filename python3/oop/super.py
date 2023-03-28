"""
super() function makes the child class inherit all the methods and properties from its parent
"""

class Company:
  def company_name(self):
    return 'Google'

class Employee(Company):
  def employee_info(self):
    c_name = super().company_name()
    print(f"Nik works at {c_name}")


emp = Employee()
emp.employee_info()